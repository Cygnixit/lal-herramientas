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
