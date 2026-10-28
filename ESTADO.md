# ESTADO — Luna Aegis Labs · Herramientas

**Actualización:** 2026-10-28. **Producto:** Aegis Exposure Sheet **0.1.1**. **Episodio asociado:** LAL-T1-E01 / Atlas v0.2.3.

| Dimensión | Veredicto |
|---|---|
| Autorización | APPROVED — Jorge autorizó la distribución pública de 0.1.1 |
| Integración | PASS — [PR #1](https://github.com/Cygnixit/lal-herramientas/pull/1) fusionada en `main` |
| Pruebas funcionales | PASS — 20/20 automatizadas, JSON 0.1.0 reimportado 8/8 y prueba de Brave satisfactoria |
| T02: uso offline | PASS — 6/6 criterios en Brave con Internet desconectado y URL `file:///`, según Jorge |
| GitHub Pages | PASS — [run 40730741561](https://github.com/Cygnixit/lal-herramientas/actions/runs/40730741561) final `completed/success`; Jorge verificó interfaz del catálogo y descarga ZIP |
| GitHub Release | PASS — [Aegis Exposure Sheet v0.1.1](https://github.com/Cygnixit/lal-herramientas/releases/tag/aegis-exposure-sheet-v0.1.1), ID `426991548`, pública y no preliminar |
| T09: distribución pública | **APROBADA CON OBSERVACIÓN** — descarga ZIP confirmada por Jorge en ventana privada de Brave, hashes de assets reportados por GitHub correctos |
| Videos | SIN PUBLICAR — ni el largo LAL-T1-E01 Atlas v0.2.3 ni el corto V01 v0.1.3 avanzan de estado por esta publicación |

## Distribución

- [Usar herramienta online](https://cygnixit.github.io/lal-herramientas/herramientas/aegis-exposure-sheet/)
- [Catálogo público](https://cygnixit.github.io/lal-herramientas/)
- [GitHub Release oficial](https://github.com/Cygnixit/lal-herramientas/releases/tag/aegis-exposure-sheet-v0.1.1)
- [Descargar ZIP offline + licencia MIT](https://github.com/Cygnixit/lal-herramientas/releases/download/aegis-exposure-sheet-v0.1.1/Aegis-Exposure-Sheet-v0.1.1.zip)
- [Descargar HTML autónomo](https://github.com/Cygnixit/lal-herramientas/releases/download/aegis-exposure-sheet-v0.1.1/Aegis-Exposure-Sheet-v0.1.1.html)
- [Sumas SHA-256](https://github.com/Cygnixit/lal-herramientas/releases/download/aegis-exposure-sheet-v0.1.1/SHA256SUMS-v0.1.1.txt)

El **catálogo ofrece solamente dos rutas principales**: «Abrir herramienta» y «ZIP + licencia». Los enlaces a Instrucciones y Ver SHA-256 permanecen auxiliares. El archivo HTML individual se conserva como adjunto técnico de la Release, no como botón redundante.

## Evidencias y hashes

- Fuente canónica de la aplicación: [herramientas/aegis-exposure-sheet/index.html](herramientas/aegis-exposure-sheet/index.html), Git blob `84e256511697d78c9158152d7462084c283c5f71`.
- HTML (29,737 B), SHA-256: `d9a2cd3fdfa09b49e1591fcaeb4f1006973432932dc124d8d3042163c61abaf0`.
- ZIP + licencia MIT (31,069 B), SHA-256: `472e3bdb2e7ec0ea97e9a357b2a9450edcf1d4c315ba930a33b37b2e26c11133`.
- SHA256SUMS-v0.1.1.txt (197 B), SHA-256 del adjunto: `1b95d36175f18729ef9344621f387907c7c4bced5b8812d21c2ba543d48bcc9b`.
- GitHub API confirma `draft=false`, `prerelease=false`, tres assets `state=uploaded`, digests SHA256 HTML/ZIP idénticos a los anteriores. Tag `aegis-exposure-sheet-v0.1.1` apunta al commit `7313b7455e861400b1c5c0881710c5720fa5a9da`.
- Jorge ejecutó `certutil -hashfile` sobre el ZIP descargado de Pages y confirmó coincidencia exacta.
- Jorge confirmó además: «El ZIP se descargó correctamente desde esa ventana privada», tras seguir la prueba de descarga desde los Assets de la Release sin iniciar sesión.

**Observación de auditoría:** no se repitió `certutil` sobre la copia nueva descargada desde la Release en modo privado. Eso no invalida la observación de acceso anónimo ni el digest que proporciona GitHub, pero no debe describirse como un segundo hash calculado localmente. T09 se cierra **aprobado con observación**, no como auditoría de seguridad completa.

## Límites, seguridad y editorial

La herramienta documenta manualmente señales de DNS, correo, CT, TLS, HTTP e inventario autorizado; **no escanea ni consulta DNS/CT/TLS/HTTP**, no detecta CVE ni diagnostica vulnerabilidades. El trabajo se conserva mediante exportación JSON; cerrar sin exportar pierde cambios. Los archivos JSON/CSV pueden contener información corporativa sensible. La mitigación de fórmulas CSV tiene evidencia limitada de LibreOffice, no de todos los lectores. El sistema de la herramienta no utiliza backend ni analítica propia, aunque GitHub Pages puede registrar visitas HTTP. Sólo usar con autorización.

La aprobación de la herramienta **no publica ni aprueba el video largo Atlas**. El corto vertical V01 no incorpora herramienta ni descarga directa; según la [regla editorial de Video Factory](https://github.com/Cygnixit/video-factory/blob/main/colaboracion/cortos-y-herramientas.md), podrá remitir al video largo cuando se publique. El cierre editorial requiere aprobación de Jorge por separado.

## Operación y continuidad

**DAMVE:** D: autorización 2026-10-28. A: Jorge probó Brave, GitHub realizó despliegue y publicó Release. M: integridad del producto, uso online/offline, descarga anónima y hashes. V: funcional y T02 PASS, T09 APROBADA CON OBSERVACIÓN. E: este archivo y los [checkpoints privados de Video Factory](https://github.com/Cygnixit/video-factory/tree/main/colaboracion/herramientas).

**Siguiente acción concreta:** entregar al equipo editorial del canal el paquete de enlaces oficial y textos de CTA para el **video largo**, respetando los gates del episodio; no producir nueva versión ni publicar videos sin decisión expresa.
