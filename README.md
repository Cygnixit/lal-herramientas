# Luna Aegis Labs · Herramientas gratuitas

Repositorio público y fuente canónica de código: **`Cygnixit/lal-herramientas`**. La distribución mediante Pages y Release se verifica por separado en `ESTADO.md`.

## Catálogo

| Recurso | Versión | Episodio | Uso |
|---|---|---|---|
| [Aegis Exposure Sheet](herramientas/aegis-exposure-sheet/README.md) | 0.1.1 (integrada en main) | LAL-T1-E01, Atlas v0.2.3 | Hoja de exposición autorizada, manual, offline |

Para abrir el catálogo localmente, abre `index.html`. Para usar la hoja sin conexión, abre `herramientas/aegis-exposure-sheet/index.html` en el navegador. No requiere instalar nada ni conectarse a servicios externos.

Catálogo de GitHub Pages: https://cygnixit.github.io/lal-herramientas/ (verificar acceso anónimo tras cada despliegue). Entregables versionados: [HTML 0.1.1](dist/Aegis-Exposure-Sheet-v0.1.1.html), [ZIP + licencia MIT](dist/Aegis-Exposure-Sheet-v0.1.1.zip), [SHA-256](dist/SHA256SUMS-v0.1.1.txt).

## Límites

La herramienta documenta observaciones aportadas por su operador; no analiza ni verifica DNS, SPF, DKIM, DMARC, certificados, cabeceras ni vulnerabilidades de forma automática. El usuario sigue siendo responsable de obtener evidencia bajo autorización y de proteger sus archivos JSON/CSV.

## Desarrollo y pruebas

No hay frameworks ni instalaciones de producción. Las pruebas reproducibles del producto están en [`tests/`](tests/) y sus dependencias son **sólo de desarrollo**: Python + pytest + Playwright + Chromium del sistema de pruebas. Las pruebas no se cargan a visitantes. Consultar `ESTADO.md` para matriz y resultados exactos.

## Licencia y terceros

Código nuevo: MIT, ver [LICENSE](LICENSE). Interfaz con CSS y JavaScript estándar; fuentes del sistema y el carácter Unicode ☾. No se incluyen fuentes comerciales, iconos, imágenes, rastreadores ni bibliotecas de terceros. Los documentos normativos consultados para diseño son referencias, no dependencias ni recursos redistribuidos.

## Publicación

El repositorio público ya existe; la publicación con GitHub Pages y Release requiere configuración y verificación independientes. Publicar únicamente versiones con pruebas aplicables comprobadas, hash SHA-256 del HTML offline y un archivo descargable, sin publicar `video-factory` ni su contenido privado. Los datos del espectador nunca se almacenan en el repositorio.

### Integración autorizada 0.1.1 — 2026-10-28

Jorge autorizó distribuir la versión 0.1.1 luego de las 20 pruebas automatizadas, su UAT y el protocolo offline T02 (6/6 en Brave, Internet desconectado, `file:///`). Integración mediante [PR #1](https://github.com/Cygnixit/lal-herramientas/pull/1). La versión se ofrece como aplicación web, HTML autónomo y ZIP con LICENSE. La **GitHub Release** con assets y verificación de descargas anónimas siguen siendo comprobaciones independientes; consultar [ESTADO](ESTADO.md).
