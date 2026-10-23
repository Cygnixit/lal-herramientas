"""Browser integration tests. pytest -q tests/test_app.py (Chromium + Playwright available)."""
import csv
import io
import json
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'herramientas' / 'aegis-exposure-sheet' / 'index.html'
CATALOG = ROOT / 'index.html'


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
        yield b
        b.close()


@pytest.fixture
def page(browser):
    ctx = browser.new_context(accept_downloads=True)
    ctx.set_offline(True)
    p = ctx.new_page()
    p.on('dialog', lambda d: d.accept())
    p.set_content(APP.read_text('utf-8'))
    yield p
    ctx.close()


def add_entry(p, signal='MX', asset='mail.empresa-ejemplo.test', obs='mx.example.test'):
    p.locator('#activo').fill(asset)
    p.locator('#senal').fill(signal)
    p.locator('#observacion').fill(obs)
    p.locator('#fuente_metodo').fill('Consulta manual simulada')
    p.locator('#responsable').fill('Administración TI')
    p.locator('#save-entry').click()


def save_download(p, selector, tmp_path):
    with p.expect_download() as event:
        p.locator(selector).click()
    download = event.value
    path = tmp_path / download.suggested_filename
    download.save_as(path)
    return path


def test_hidden_controls_are_hidden(page):
    assert page.locator('#cancel-edit').is_hidden()
    assert page.locator('#import-json').is_hidden()


def test_t01_fiction_covers_complete_episode(page):
    page.locator('#demo').click()
    rows = page.evaluate('window.__AES_TEST__.getEntries()')
    assert len(rows) == 8
    assert {r['categoria'] for r in rows} == {'DNS', 'CORREO', 'CT', 'TLS', 'HTTP'}
    assert {'NS','MX','SPF','DKIM','DMARC','Nombre en CT','Certificado TLS','Cabecera Server'} == {r['senal'] for r in rows}
    assert any(r['contraste']=='por_explicar' for r in rows)
    assert all('simulad' in (r['fuente_metodo']+' '+r['observacion']).lower() or 'fictici' in (r['fuente_metodo']+' '+r['observacion']).lower() or 'ejemplo' in r['observacion'].lower() for r in rows)
    assert page.locator('#total').inner_text() == '8'


def test_t02_offline_input_and_download(page,tmp_path):
    assert page.evaluate('navigator.onLine') is False
    page.locator('#dominio').fill('empresa-ejemplo.test')
    add_entry(page)
    add_entry(page,signal='NS',asset='empresa-ejemplo.test')
    result = save_download(page, '#export-json', tmp_path)
    data = json.loads(result.read_text('utf-8'))
    assert data['meta']['dominio']=='empresa-ejemplo.test'
    assert len(data['entries'])==2


def test_t03_json_roundtrip_accents_metadata_edit(page,tmp_path):
    page.locator('#dominio').fill('niñez-ejemplo.test')
    page.locator('#alcance').fill('Revisión autorizada — acta de prueba')
    add_entry(page,obs='Señal <prueba> áéíóú')
    page.locator('#entry-form').locator('#evidencia_tipo').select_option('inferencia')
    assert page.locator('#edit-state').inner_text() == 'Nueva observación'
    exported = save_download(page, '#export-json', tmp_path)
    original = json.loads(exported.read_text('utf-8'))
    page.locator('#new').click()
    assert page.locator('#total').inner_text()=='0'
    page.locator('#import-json').set_input_files(str(exported))
    page.wait_for_function("document.getElementById('total').textContent === '1'")
    assert page.locator('#total').inner_text()=='1'
    after = page.evaluate('window.__AES_TEST__.exportData()')
    assert original == after
    assert after['entries'][0]['observacion']=='Señal <prueba> áéíóú'


def test_t05_invalid_import_keeps_unsaved_work(page,tmp_path):
    page.locator('#dominio').fill('empresa-ejemplo.test')
    add_entry(page)
    before=page.evaluate('window.__AES_TEST__.exportData()')
    for name, content in [('bad.json','{ broken'),('schema.json',json.dumps({'schemaVersion':'999','episodeId':'LAL-T1-E01','meta':{},'entries':[]})),('big.json','A'*(1024*1024+20)),('evil.json',json.dumps({'schemaVersion':'1.0','episodeId':'LAL-T1-E01','meta':{'dominio':'d.test','revisor':'','fecha':'','alcance':''},'entries':[{'id':'a','__proto__':{'x':1}}]}))]:
        f=tmp_path/name;f.write_text(content,encoding='utf-8')
        page.locator('#import-json').set_input_files(str(f))
        page.wait_for_function("document.getElementById('notice').textContent.includes('rechazada')")
        assert page.evaluate('window.__AES_TEST__.exportData()') == before
        assert 'rechazada' in page.locator('#notice').inner_text().lower()


def test_t05_user_text_inert_in_html(page):
    page.locator('#dominio').fill('empresa-ejemplo.test')
    script='<img src=x onerror="window.injected=1">'
    add_entry(page,signal=script,asset='peligro.test',obs='<script>alert(1)</script>')
    assert page.locator('#rows img').count()==0
    assert page.evaluate('window.injected') is None
    assert page.locator('#rows').inner_text().count(script)==1
    assert page.locator('#rows button').count()==2


def test_t06_no_network_requests_file_or_catalog(browser):
    ctx=browser.new_context(accept_downloads=True)
    page=ctx.new_page();req=[];page.on('request',lambda r:req.append(r.url))
    page.set_content(APP.read_text('utf-8'));page.locator('#demo').click();page.locator('#filter-category').select_option('CORREO')
    assert not any(u.startswith(('https:', 'http:')) for u in req),req
    assert page.evaluate('typeof fetch')=='function'
    page.set_content(CATALOG.read_text('utf-8'));assert page.locator('h2').inner_text()=='Aegis Exposure Sheet'
    assert not any(u.startswith(('https:', 'http:')) for u in req),req
    ctx.close()


def test_t07_mobile_layout(browser):
    ctx=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True)
    page=ctx.new_page();page.set_content(APP.read_text('utf-8'));assert page.locator('h1').is_visible()
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.locator('#demo').click();assert page.locator('#total').inner_text()=='8'
    page.set_content(CATALOG.read_text('utf-8'));assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    ctx.close()


def test_t08_view_filters_not_exports(page,tmp_path):
    page.locator('#demo').click()
    page.locator('#filter-state').select_option('por_explicar')
    assert page.locator('#rows tr').count()==2
    obj=json.loads(save_download(page,'#export-json',tmp_path).read_text('utf-8'))
    assert len(obj['entries'])==8
    assert page.locator('body').inner_text().lower().count('vulnerabilidad')>=1


def test_csv_generated_and_formulas_prefixed(page,tmp_path):
    page.locator('#dominio').fill('empresa-ejemplo.test')
    add_entry(page,signal='=2+3',asset='-1+2',obs=' @sum(2,3)')
    f=save_download(page,'#export-csv',tmp_path)
    with f.open(encoding='utf-8-sig',newline='') as fi:
        rows=list(csv.reader(fi))
    assert len(rows)==2
    cols=rows[0];d=dict(zip(cols,rows[1]))
    assert d['senal']=="'=2+3"
    assert d['activo']=="'-1+2"
    assert d['observacion']=="' @sum(2,3)"
    assert d['dominio']=='empresa-ejemplo.test'


def test_edit_preserves_id_and_cancels(page):
    page.locator('#dominio').fill('empresa-ejemplo.test');add_entry(page)
    uid=page.evaluate('window.__AES_TEST__.getEntries()[0].id')
    page.locator('#rows button').first.click()
    page.locator('#senal').fill('SPF')
    page.locator('#save-entry').click()
    assert page.evaluate('window.__AES_TEST__.getEntries()[0].id')==uid
    assert page.evaluate('window.__AES_TEST__.getEntries()[0].senal')=='SPF'
    page.locator('#rows button').first.click()
    page.locator('#cancel-edit').click()
    assert page.locator('#edit-state').inner_text()=='Nueva observación'


def test_bad_dates_rejected_in_import(page,tmp_path):
    page.locator('#dominio').fill('empresa-ejemplo.test');add_entry(page)
    obj=page.evaluate('window.__AES_TEST__.exportData()');obj['entries'][0]['fecha_observacion']='2026-02-30'
    f=tmp_path/'invalid-date.json';f.write_text(json.dumps(obj),encoding='utf-8')
    page.locator('#import-json').set_input_files(str(f))
    page.wait_for_function("document.getElementById('notice').textContent.includes('rechazada')")
    assert 'rechazada' in page.locator('#notice').inner_text().lower()
    assert page.locator('#total').inner_text()=='1'


def test_csv_not_formula_in_libreoffice(page,tmp_path):
    lo = __import__("shutil").which('libreoffice')
    if not lo:
        pytest.skip('LibreOffice not installed; T04 not covered in this environment')
    content = page.evaluate("""() => {
          const f=window.__AES_TEST__.csvCell;
          const rows=[['test','raw'], ['equals','=2+3'], ['plus','+1+5'], ['minus','-1+2'], ['at','@SUM(A1:A2)'], ['spaces','  =2+3'], ['line','\\n=2+3'], ['normal','texto seguro']];
          return '\\uFEFF'+rows.map(r=>r.map(f).join(',')).join('\\r\\n')+'\\r\\n';
        }""")
    source = tmp_path / 'injection.csv'
    source.write_text(content, encoding='utf-8')
    destination = tmp_path / 'output'
    destination.mkdir()
    profile = tmp_path / 'lo-profile'
    result = __import__("subprocess").run([lo, f'-env:UserInstallation={profile.as_uri()}', '--headless', '--convert-to', 'xlsx', '--outdir', str(destination), str(source)], capture_output=True, text=True, timeout=20)
    target = destination / 'injection.xlsx'
    assert result.returncode == 0 and target.exists(), result.stderr
    with __import__("zipfile").ZipFile(target) as z:
        xml = z.read('xl/worksheets/sheet1.xml')
    root = __import__("xml.etree.ElementTree",fromlist=["fromstring"]).fromstring(xml)
    ns={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    formulas=root.findall('.//x:f',ns)
    assert formulas==[], f'Unexpected formula nodes: {len(formulas)}'


def test_catalog_guide_link_exists_and_selfcontained():
    guide=ROOT/'herramientas/aegis-exposure-sheet/guia.html'
    assert guide.is_file()
    catalog=CATALOG.read_text('utf-8')
    assert 'herramientas/aegis-exposure-sheet/guia.html' in catalog
    assert 'LAL-T1-E01' in guide.read_text('utf-8')
    assert '<script src=' not in guide.read_text('utf-8')
