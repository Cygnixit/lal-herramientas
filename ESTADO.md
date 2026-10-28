# ESTADO — Luna Aegis Labs · Herramientas

**Actualización:** 2026-10-28. **Producto:** Aegis Exposure Sheet **0.1.1**. **Episodio asociado:** LAL-T1-E01 / Atlas v0.2.3.

| Dimensión | Veredicto |
|---|---|
| Autorización | **APPROVED** — Jorge autorizó expresamente integración y distribución de 0.1.1 el 2026-10-28 |
| Integración | **COMPLETE** — [PR #1](https://github.com/Cygnixit/lal-herramientas/pull/1) fusionada con `main` |
| Validación funcional | **PASS** — 20/20 pruebas automatizadas, JSON 0.1.0 compatible (8/8), UAT positiva reportada por Jorge |
| T02 offline | **PASS en Brave** — 6/6 operaciones con Internet desconectado y URL `file:///`, reportado por Jorge |
| Distribución en repositorio | **COMPLETE** — HTML y ZIP + LICENSE, sumas SHA-256, catálogo enlazado a archivos versionados |
| GitHub Pages | **DEPLOY AUTOMÁTICO** — GitHub Actions debe indicar SUCCESS en la revisión final; acceso anónimo aún pendiente de validación |
| GitHub Release | **PENDING** — sin tag/Release con los tres adjuntos (la entrega en Pages/repositorio no equivale a una Release) |
| T09 distribución pública | **PARTIAL** — faltan acceso/descargas anónimas, cotejo SHA externo y GitHub Release |
| Video largo y corto | **NO PUBLICADOS** — la distribución de la herramienta es un gate distinto del editorial |

## Fuente canónica y versión

Repositorio de código fuente único: [Cygnixit/lal-herramientas](https://github.com/Cygnixit/lal-herramientas). Archivo de aplicación: [index.html](herramientas/aegis-exposure-sheet/index.html). Fuente HTML de **0.1.1** es idéntica a la probada (Git blob SHA `84e256511697d78c9158152d7462084c283c5f71`). Se integró a `main` mediante [PR #1](https://github.com/Cygnixit/lal-herramientas/pull/1), commit de integración `dcfaca7f47bbd3b35b2c5aee21b15393c628fae3`. No copiar código editable a Video Factory.

Versión online esperada: https://cygnixit.github.io/lal-herramientas/herramientas/aegis-exposure-sheet/

Descargas versionadas servidas desde el repositorio y por Pages si despliega correctamente:

- [HTML autónomo v0.1.1](dist/Aegis-Exposure-Sheet-v0.1.1.html) y [versión Pages](https://cygnixit.github.io/lal-herramientas/dist/Aegis-Exposure-Sheet-v0.1.1.html).
- [ZIP v0.1.1 con LICENSE MIT](dist/Aegis-Exposure-Sheet-v0.1.1.zip) y [versión Pages](https://cygnixit.github.io/lal-herramientas/dist/Aegis-Exposure-Sheet-v0.1.1.zip).
- [SHA256SUMS-v0.1.1.txt](dist/SHA256SUMS-v0.1.1.txt). El archivo `dist/SHA256SUMS.txt` apunta a la versión actual 0.1.1.

```text
d9a2cd3fdfa09b49e1591fcaeb4f1006973432932dc124d8d3042163c61abaf0  Aegis-Exposure-Sheet-v0.1.1.html
472e3bdb2e7ec0ea97e9a357b2a9450edcf1d4c315ba930a33b37b2e26c11133  Aegis-Exposure-Sheet-v0.1.1.zip
```

El ZIP contiene únicamente HTML 0.1.1 y licencia MIT, sin dependencias; usa ZIP_STORED con metadatos fijos, generable mediante `python tests/build_release.py`. **Archivo ZIP anterior comprimido con hash `4b159414...` sustituido en distribución**. Se comprobó `ZipFile.testzip()` y SHA-256 del HTML extraído. El ZIP almacenado Git blob `4a6583210c358a9a169fe1d635a220d30e12624e` coincide con la generación local.

## Evidencia y alcance

- [Pruebas de regresión 0.1.1](tests/RESULTADOS-v0.1.1.md): **20/20 PASS** (Chromium/Playwright, Linux Debian), diálogos propios, cancelar/Escape sin borrar datos, filtros, CSV limitado y JSON seguro.
- UAT humana (2026-10-25): Jorge reportó correctamente su prueba en Brave.
- T02 humana (2026-10-28): Jorge reportó **6/6 PASS** al abrir HTML local vía `file:///`, desconectar Internet, cargar 8 registros, exportar JSON, nueva hoja (0), importar JSON (8) y cancelar hoja nueva (8).
- Verificación adicional 2026-10-28: smoke Chromium offline mediante `page.set_content`, ejemplo=8, cancelar mantiene=8, confirmar nueva=0, **0 solicitudes de red**.
- Sin promesa de compatibilidad completa con Firefox/Safari/Edge ni auditoría de accesibilidad instrumentada. CSV sólo probado de forma limitada en LibreOffice; requiere cautela en otros programas.

El recurso **no escanea**, no hace consultas DNS/CT/TLS/HTTP ni diagnostica CVE o intrusiones; sólo ayuda a documentar evidencia manual de activos propios o autorizados. No transmite formularios a un backend, ni utiliza rastreo de producto, pero GitHub Pages puede registrar accesos HTTP. Los datos se guardan sólo por exportación JSON del usuario; cerrar sin guardar pierde cambios. Archivos JSON/CSV pueden contener información corporativa.

## Próximos gates

1. Obtener **SUCCESS** de Pages para el commit final y validar navegación anónima de catálogo, HTML online y los enlaces de descarga (fuera de sesión GitHub). El éxito del build por sí solo no acredita las descargas.
2. Descargar HTML y ZIP sin sesión desde las URLs publicadas y verificar SHA-256 contra los dos hashes anteriores.
3. Crear la **GitHub Release oficial `aegis-exposure-sheet-v0.1.1`** con los tres assets (HTML, ZIP, `SHA256SUMS-v0.1.1.txt`). El conector GitHub instalado no permite crear Releases ni adjuntar assets; operación separada mediante interfaz GitHub o herramienta autorizada.
4. Registrar T09 **PASS** y entonces comunicar al Canal los enlaces definitivos. No adelantar anuncios ni publicar/modificar el episodio largo Atlas ni el corto V01 por aprobar esta herramienta. El corto sólo puede remitir al largo, sin herramienta propia.

## DAMVE

**D:** autorización de Jorge del 2026-10-28. **A:** integración en GitHub, revisión y empaquetado sin coste. **M:** HTML 0.1.1 canónico, uso online/descarga, verificación hashes. **V:** funcional T02 PASS; distribución T09 PARCIAL hasta acceso y Release confirmados. **E:** este archivo + checkpoint de Video Factory `colaboracion/herramientas/`.
