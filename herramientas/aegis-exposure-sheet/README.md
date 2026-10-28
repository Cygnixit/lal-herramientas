# Aegis Exposure Sheet 0.1.1

**Episodio:** LAL-T1-E01, Atlas v0.2.3 — mapa de exposición externa (DNS, correo, CT, TLS, HTTP e inventario). **Licencia:** MIT.

## Propósito

Hoja de exposición autorizada que permite documentar manualmente las señales públicas y contrastarlas con lo que tu organización cree tener publicado. Dirigida a responsables de seguridad, administradores de TI y estudiantes con laboratorios propios.

## Uso

1. Abre [la aplicación](index.html) desde el catálogo o guarda el HTML en tu computadora y ábrelo localmente.
2. Indica dominio autorizado, responsable, fecha y alcance. **No introduzcas secretos ni credenciales.**
3. Añade señales manuales, fuente y fecha, expectativa de inventario, propietario, justificación, clasificación y siguiente validación. Usa «Cargar ejemplo ficticio» para practicar sin consultar infraestructura.
4. Exporta la hoja como **JSON** para conservar todo el trabajo; importa ese mismo JSON para retomarlo. La pestaña no almacena un respaldo permanente.
5. Si necesitas una tabla, exporta **CSV** y revísala antes de enviarla. No se aplican los filtros de la interfaz a la exportación.

La [guía de uso](guia.html) ofrece un recorrido con definiciones de estados.

## Límites y privacidad

No realiza consultas DNS, CT, TLS ni HTTP; no escanea redes, identifica CVE ni diagnostica vulnerabilidades o intrusiones. Un nombre en CT puede ser histórico; un selector DKIM arbitrario no encontrado no equivale a falta de DKIM; una cabecera Server no acredita versión ni CVE.

Todos los datos son locales durante el uso; no hay API, cookies, analítica ni dependencias externas. **Cerrar sin exportar JSON pierde cambios.** CSV incorpora una mitigación limitada de fórmulas comprobada en LibreOffice, no universal en Excel/otros lectores. Los archivos exportados pueden revelar información corporativa; consérvalos y compártelos bajo autorización.

JSON versión de esquema 1.0, máximo 250 observaciones y archivo de importación hasta 1 MiB. Los campos de importación se validan; los fallos dejan intacta la hoja abierta.

## Pruebas y versiones

Consulta [evidencias](../../tests/RESULTADOS.md) y el estado actual en [ESTADO](../../ESTADO.md). La versión del HTML, su SHA-256 y pruebas son independientes del estado de publicación del video.

[Código](https://github.com/Cygnixit/lal-herramientas/tree/main/herramientas/aegis-exposure-sheet) · [Comunicar un problema](https://github.com/Cygnixit/lal-herramientas/issues) — no pegar datos internos en Issues.

## Confirmaciones personalizadas · 0.1.1

Nueva hoja, recuperación JSON válida, exportación CSV, reemplazo por el ejemplo y eliminación de registros usan un diálogo propio, sin `window.confirm()`. Cancelar o pulsar Escape conserva los datos y el estado anterior. El selector del archivo JSON sigue siendo nativo por seguridad. Se conserva `schemaVersion: "1.0"`; el JSON exportado en 0.1.0 puede reimportarse. **Integrada en main el 2026-10-28**; GitHub Release permanece como distribución adicional aún pendiente.

## Archivos oficiales en el repositorio

[Descargar HTML 0.1.1](../../dist/Aegis-Exposure-Sheet-v0.1.1.html) · [ZIP con licencia MIT](../../dist/Aegis-Exposure-Sheet-v0.1.1.zip) · [SHA-256](../../dist/SHA256SUMS-v0.1.1.txt). Son los archivos versionados del catálogo; la descarga externa y la GitHub Release se acreditan por separado. La prueba offline T02 fue aprobada por Jorge en Brave con Internet desconectado (seis criterios).
