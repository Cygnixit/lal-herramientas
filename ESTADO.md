# ESTADO — Luna Aegis Labs · Herramientas

Actualizado: 2026-10-23. Producto: Aegis Exposure Sheet **0.1.0**. Episodio: **LAL-T1-E01 / Atlas v0.2.3**.

| Dimensión | Estado |
|---|---|
| Autorización | ACCEPTED — Jorge autorizó implementación y distribución pública con $0, pero sólo después de pruebas aplicables |
| Implementación | COMPLETE — código del producto, catálogo, guía, licencia MIT y pruebas incorporados a este repositorio |
| Validación | PARTIAL — 14 pruebas PASS locales; falta apertura directa file:// en navegador sin bloqueo |
| Revisión | PENDING — validación externa del flujo offline |
| Publicación Pages | DEPLOY_SUCCEEDED — GitHub Pages main/(root) configurado por Jorge; workflow terminado SUCCESS; URL final no accesible/verificable desde esta sesión |
| GitHub Release | PENDING — aún sin tag/release/assets comprobados |

## Fuente canónica

https://github.com/Cygnixit/lal-herramientas

Aegis Exposure Sheet: herramientas/aegis-exposure-sheet/index.html.
El código de Video Factory permanece en su repositorio separado y privado/no modificado. Este repositorio contiene la única fuente editable del producto. Los archivos de distribución generados en la carpeta dist son derivados; no mantener otra fuente editable en video-factory.

## Pruebas y checkpoints verificables

- App y catálogo en GitHub tienen exactamente los hashes Git blob de las versiones probadas localmente. El archivo de pruebas test_app.py también coincide.
- Prueba local del 2026-10-23: pytest -q tests/test_app.py --disable-warnings -> 14 passed in 11.31s (Debian 13, Python 3.13.5, Chromium 144, LibreOffice 25.2).
- T02: Chromium del entorno bloquea file:// con ERR_BLOCKED_BY_ADMINISTRATOR. Interacción offline mediante set_content pasó, pero T02 completa **no** está acreditada.
- T04: CSV probado en LibreOffice, sin fórmulas XML en ocho casos adversariales. Excel y otros importadores no probados.
- T09: workflow Pages **success** comprobado (run 40011728358, commit de despliegue 9a1bf1d033730695f4a5218257c8e3dbff3ce8c0); navegación pública y descarga anónima no verificadas desde este entorno. Release y hash remoto pendientes.
- Empaquetador reproducible tras corrección de timestamps ZIP; generar mediante python tests/build_release.py.
- SHA-256 esperado del HTML offline: f285f0c8c70b1c12a86c69ddf0d032c0eb438462316b1b786a7a2cd615e84e79.
- SHA-256 del ZIP determinista: 5615178a3887286a5da5013a8a98ac05f94cd2282aa14ea6503616dbb4d74fc7.

Consultar tests/RESULTADOS.md para pasos y límites.

## Distribución siguiente

1. Probar en una computadora sin las restricciones del contenedor que el HTML descargado se abre mediante file:// estando offline; crear ejemplo, guardar JSON, recargar página, recuperar JSON; registrar OS/navegador/resultado.
2. **Configuración Pages realizada por Jorge:** main / (root), HTTPS obligatorio. Ejecución de Actions concluida SUCCESS: https://github.com/Cygnixit/lal-herramientas/actions/runs/40011728358 (2026-10-23).
3. **Comprobar en navegador ajeno a la sesión** catálogo https://cygnixit.github.io/lal-herramientas/ y herramienta https://cygnixit.github.io/lal-herramientas/herramientas/aegis-exposure-sheet/ sin inicio de sesión. El comprobador web de esta sesión no pudo acceder, aunque el workflow terminó SUCCESS; no afirmar validación final.
4. Generar los tres archivos dist mediante Python y crear GitHub Release de nombre Aegis Exposure Sheet 0.1.0, tag aegis-exposure-sheet-v0.1.0. Adjuntar HTML, ZIP y SHA256SUMS.txt. Conector de esta sesión no dispone de creación de Releases/assets; requiere interfaz web o acceso adicional.
5. Verificar descarga anónima y SHA-256 obtenido; sólo entonces marcar PUBLISHED y actualizar exclusivamente colaboracion/herramientas/ de Video Factory.

Esta publicación NO aprueba ni publica el video LAL-T1-E01.

## Candidata 0.1.1 en rama aislada — 2026-10-24

Rama: `herramientas/aes-confirmaciones-v0.1.1`. Base de main: `db199dce1b0e0ab43879ff91563eb3e5fa4b8dff`.
Nueva UX de confirmación: HTML autónomo sin confirmaciones nativas de JavaScript (el selector de archivos del sistema no se cambia). **20 pruebas PASS** locales en Chromium/Debian + reimportación del JSON original aportado por Jorge 8/8 intacto. Ver [pruebas de candidata](tests/RESULTADOS-v0.1.1.md). HTML SHA-256 `d9a2cd3fdfa09b49e1591fcaeb4f1006973432932dc124d8d3042163c61abaf0`; ZIP SHA-256 `4b1594144d7eccb4b245b339226535f9dbcd17223c00824ca0adc53b8f1702ea`.
**No existe Release 0.1.1 ni despliegue desde esta rama; main y Pages no alterados.** T02 apertura file:// real y revisión de Jorge pendientes.

## Veredicto de prueba humana — 2026-10-25

Jorge confirmó en el chat tras descargar y probar la candidata 0.1.1: **«Ya hice las pruebas y todo funcionó bien.»** Se registra **UAT_FUNCIONAL_APROBADA_SEGÚN_REPORTE_DE_JORGE** para los diálogos propios (Nueva hoja, Cancelar/Escape, recuperación JSON y flujo de uso solicitado). Es una **confirmación humana declarada**, no evidencia capturada por un runner ni un informe detallado de compatibilidad. No se deduce que todos los navegadores, privacidad o la desconexión completa de Internet hayan sido comprobados.

La ejecución automatizada previa de esta candidata conserva **20/20 PASS** sobre el HTML exacto del commit de código `12e30ccfe5cb7541ac2219ccd2c9c0ce714b2e1f`; el archivo de producto NO se modificó al registrar este veredicto. Los gates externos T02 de apertura directa offline con desconexión explícita y T09 de Release pública con descarga/hash verificados **siguen sin cierre documental**.

**Decisión:** candidata 0.1.1 APTA PARA PROPONER INTEGRACIÓN, aún **NO INTEGRADA ni PUBLICADA**. `main` y Pages permanecen en 0.1.0; crear Release, desplegar e incorporar 0.1.1 requiere decisión de publicación posterior de Jorge. El corto V01 no recibe herramienta.
