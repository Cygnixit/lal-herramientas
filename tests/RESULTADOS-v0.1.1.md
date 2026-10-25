# QA candidata · Aegis Exposure Sheet 0.1.1

**Estado:** VALIDACIÓN LOCAL APROBADA CON OBSERVACIONES / SIN RELEASE / NO PUBLICADA EN PAGES.
**Episodio asociado:** video largo LAL-T1-E01 / Atlas v0.2.3. El vertical v0.1.3 no lleva recurso propio.
**Solicitud:** observaciones de Jorge del 2026-10-24 sobre diálogos nativos al crear hoja nueva y recuperar JSON; continuación autorizada («Adelante»).

## Cambios bajo prueba

- `<dialog>` autocontenido, títulos y textos contextualizados, roles descriptivos y foco inicial en **Cancelar**.
- Reemplaza las confirmaciones `window.confirm()` de: nueva hoja, recuperación JSON válida, CSV, ejemplo sobre datos existentes y eliminación de registro.
- Cancelar o Escape preservan registros y metadatos. Confirmar mantiene las acciones previas. Archivo JSON incompatible se rechaza ANTES de confirmar.
- El selector de archivos del navegador/OS continúa siendo nativo; no se simula ni se altera.
- Ningún escáner, consulta DNS/HTTP o dependencia añadida. `schemaVersion: 1.0`, compatibilidad de JSON 0.1.0 conservada.

## Evidencia efectivamente ejecutada

Entorno: contenedor Linux/Debian 13, Python 3.13.5, pytest 9.0.2, Playwright Sync, Chromium 144.0.7559.96 y LibreOffice 25.2.3.2. Se extrajo el ZIP de fuentes de 0.1.0, con hashes blob coincidentes con la fuente canónica de GitHub, y se aplicó el parche mínimo de 0.1.1.

`pytest -q tests/test_app.py --disable-warnings` → **20 passed in 15.03 s**, sin fallos en la última ejecución. Las primeras ejecuciones fallaron por aserciones hechas antes del evento `close` del diálogo y por funciones no disponibles de la API de Playwright; las pruebas se ajustaron para esperar estados finales sin cambiar la CSP. No se transfieren aquellos errores transitorios como fallos de la versión entregada.

Pruebas adicionales: se importó el archivo JSON real entregado por Jorge `aegis-exposure-sheet-empresa-ejemplo.test(1).json` desde 0.1.0. Tras aceptar el nuevo diálogo, **8/8 registros, metadatos y todos los campos preservados; 0 peticiones de red registradas** en el flujo offline con `page.set_content()`. Captura del diálogo guardada como evidencia local de la conversación; no se publica por defecto.

SHA-256 de archivos de prueba generados localmente desde las fuentes:
```text
d9a2cd3fdfa09b49e1591fcaeb4f1006973432932dc124d8d3042163c61abaf0  Aegis-Exposure-Sheet-v0.1.1.html
4b1594144d7eccb4b245b339226535f9dbcd17223c00824ca0adc53b8f1702ea  Aegis-Exposure-Sheet-v0.1.1.zip
```
El ZIP tiene timestamps y permisos constantes. El paquete **no** está adjunto a una Release ni es una descarga pública anunciada.

## Pendientes y límites

- T02 `file://` real sigue pendiente en Brave o navegador sin política del contenedor `ERR_BLOCKED_BY_ADMINISTRATOR`.
- Firefox, Safari, Edge real y accesibilidad por lector de pantalla no probados.
- CSV sólo comprobado de forma limitada en LibreOffice (no garantía universal en Excel).
- Validar manualmente Cancelar/Escape y recuperación de JSON en Brave con esta candidata antes de aprobar merge a `main`.
- **No modificar `main` ni publicar en Pages/Release sin autorización posterior expresa.** La candidata está aislada en rama y el sitio público 0.1.0 permanece intacto.
