# Luna Aegis Labs · Herramientas gratuitas

Repositorio público y fuente canónica de código: **`Cygnixit/lal-herramientas`**. La distribución mediante Pages y Release se verifica por separado en `ESTADO.md`.

## Catálogo

| Recurso | Versión | Episodio | Uso |
|---|---|---|---|
| [Aegis Exposure Sheet](herramientas/aegis-exposure-sheet/README.md) | 0.1.1 (candidata en rama) | LAL-T1-E01, Atlas v0.2.3 | Hoja de exposición autorizada, manual, offline |

Para abrir el catálogo localmente, abre `index.html`. Para usar la hoja sin conexión, abre `herramientas/aegis-exposure-sheet/index.html` en el navegador. No requiere instalar nada ni conectarse a servicios externos.

En caso de publicación posterior: catálogo `https://cygnixit.github.io/lal-herramientas/` y código fuente `https://github.com/Cygnixit/lal-herramientas`; **no afirmar disponibilidad hasta comprobarlos**.

## Límites

La herramienta documenta observaciones aportadas por su operador; no analiza ni verifica DNS, SPF, DKIM, DMARC, certificados, cabeceras ni vulnerabilidades de forma automática. El usuario sigue siendo responsable de obtener evidencia bajo autorización y de proteger sus archivos JSON/CSV.

## Desarrollo y pruebas

No hay frameworks ni instalaciones de producción. Las pruebas reproducibles del producto están en [`tests/`](tests/) y sus dependencias son **sólo de desarrollo**: Python + pytest + Playwright + Chromium del sistema de pruebas. Las pruebas no se cargan a visitantes. Consultar `ESTADO.md` para matriz y resultados exactos.

## Licencia y terceros

Código nuevo: MIT, ver [LICENSE](LICENSE). Interfaz con CSS y JavaScript estándar; fuentes del sistema y el carácter Unicode ☾. No se incluyen fuentes comerciales, iconos, imágenes, rastreadores ni bibliotecas de terceros. Los documentos normativos consultados para diseño son referencias, no dependencias ni recursos redistribuidos.

## Publicación

El repositorio público ya existe; la publicación con GitHub Pages y Release requiere configuración y verificación independientes. Publicar únicamente versiones con pruebas aplicables comprobadas, hash SHA-256 del HTML offline y un archivo descargable, sin publicar `video-factory` ni su contenido privado. Los datos del espectador nunca se almacenan en el repositorio.

### Candidata de interfaz 0.1.1

La revisión de diálogos de 0.1.1 se encuentra en la rama `herramientas/aes-confirmaciones-v0.1.1`. `main`/Pages siguen sirviendo 0.1.0 hasta aprobación posterior y cambio controlado. No usar el HTML del catálogo de main para evaluar los nuevos diálogos.
