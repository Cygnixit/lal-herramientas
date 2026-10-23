"""Genera entregables reproducibles con Python stdlib, sin dependencias externas."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

root = Path(__file__).resolve().parents[1]
source = root / 'herramientas' / 'aegis-exposure-sheet' / 'index.html'
destination = root / 'dist'
destination.mkdir(exist_ok=True)
html_name = 'Aegis-Exposure-Sheet-v0.1.0.html'
zip_name = 'Aegis-Exposure-Sheet-v0.1.0.zip'
html = source.read_bytes()
license_text = (root / 'LICENSE').read_bytes()
(destination / html_name).write_bytes(html)


def add_stable_member(archive: ZipFile, name: str, data: bytes) -> None:
    info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


with ZipFile(destination / zip_name, 'w') as archive:
    add_stable_member(archive, html_name, html)
    add_stable_member(archive, 'LICENSE.txt', license_text)

checksums = '\n'.join(
    f'{sha256((destination / name).read_bytes()).hexdigest()}  {name}'
    for name in (html_name, zip_name)
) + '\n'
(destination / 'SHA256SUMS.txt').write_text(checksums, encoding='utf-8')
print(checksums)
