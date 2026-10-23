# Pruebas — Aegis Exposure Sheet 0.1.0

**Unidad:** TASK-HERR-LAL-T1-E01-002. **Fecha:** 2026-10-23. **Estado:** 14 PASS locales, aceptación de publicación pendiente.

## Entorno real y comando

- Debian 13 en contenedor, Python 3.13.5, pytest, Playwright Sync API, Chromium 144.0.7559.96 y LibreOffice 25.2.3.2.
- Ejecutado en la fuente local que coincide exactamente por hash Git blob con app/catálogo/tests subidos a este repositorio: pytest -q tests/test_app.py --disable-warnings → **14 passed in 11.31 s**.
- La ejecución sobre un checkout recién clonado de GitHub no fue efectuada, no atribuirle ese PASS.
- Las dependencias de pytest, Playwright y Chromium son exclusivas de pruebas, no de ejecución para usuarios. Los scripts requieren Chromium en /usr/bin/chromium y LibreOffice para el caso CSV.
- Empaquetador: python tests/build_release.py; se verificaron dos ejecuciones consecutivas con hashes idénticos de HTML y ZIP.

## Criterios

| ID | Resultado real | Límite |
|---|---|---|
| T01 | PASS | Ocho señales ficticias: NS, MX, SPF, DKIM, DMARC, CT, TLS y HTTP, con discrepancia de inventario por explicar |
| T02 | PARTIAL | Flujos offline y guardado JSON en contexto Playwright sin red; la navegación directa file:// fue bloqueada por ERR_BLOCKED_BY_ADMINISTRATOR |
| T03 | PASS | JSON reimportado con metadatos, acentos y observaciones idénticos |
| T04 | PASS limitado | CSV descargado; 8 casos adversariales convertidos a XLSX por LibreOffice 25.2, 0 nodos fórmula; no probado en Excel/Safari |
| T05 | PASS | Texto con HTML/script inerte; importaciones inválidas, demasiado grandes o fecha imposible no alteran hoja |
| T06 | PASS limitado | Cero solicitudes HTTP(S) en los flujos Chromium observados con set_content; Pages todavía no comprobado |
| T07 | PASS limitado | Emulación escritorio 1280 px y móvil 390 px; no comprobados equipos reales ni todos los navegadores |
| T08 | PASS | Sólo captura/contraste manual, filtros no afectan exportación y sin diagnóstico automático de vulnerabilidades |
| T09 | PENDING | GitHub Pages, Release y descarga pública anónima no creados/comprobados |

## Integridad y límites

- App HTML del checkout GitHub idéntica por Git blob hash al origen ejecutado localmente (27311 bytes).
- Reproducible: HTML SHA-256 f285f0c8c70b1c12a86c69ddf0d032c0eb438462316b1b786a7a2cd615e84e79.
- ZIP determinista SHA-256 5615178a3887286a5da5013a8a98ac05f94cd2282aa14ea6503616dbb4d74fc7.
- CSV no garantiza inmunidad ante todas las fórmulas o lectores, importaciones regionales o reexportación.
- No hay telemetría ni consulta de infraestructura; el espectador debe guardar expresamente JSON; no se probó auditoría independiente de ciberseguridad.
- NO declarar distribución hasta T02 y T09 verificadas.
