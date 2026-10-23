# Luna Aegis Labs · Herramientas gratuitas

Repositorio canónico previsto: `Cygnixit/lal-herramientas`. La existencia de este árbol **local** no demuestra que ya se haya creado o publicado un repositorio remoto.

## Catálogo

| Recurso | Versión | Episodio | Uso |
|---|---|---|---|
| [Aegis Exposure Sheet](herramientas/aegis-exposure-sheet/README.md) | 0.1.0 | LAL-T1-E01, Atlas v0.2.3 | Hoja de exposición autorizada, manual, offline |

Para abrir el catálogo localmente, abre `index.html`. Para usar la hoja sin conexión, abre `herramientas/aegis-exposure-sheet/index.html` en el navegador. No requiere instalar nada ni conectarse a servicios externos.

En caso de publicación posterior: catálogo `https://cygnixit.github.io/lal-herramientas/` y código fuente `https://github.com/Cygnixit/lal-herramientas`; **no afirmar disponibilidad hasta comprobarlos**.

## Límites

La herramienta documenta observaciones aportadas por su operador; no analiza ni verifica DNS, SPF, DKIM, DMARC, certificados, cabeceras ni vulnerabilidades de forma automática. El usuario sigue siendo responsable de obtener evidencia bajo autorización y de proteger sus archivos JSON/CSV.

## Desarrollo y pruebas

No hay frameworks ni instalaciones de producción. Las pruebas reproducibles del producto están en [`tests/`](tests/) y sus dependencias son **sólo de desarrollo**: Python + pytest + Playwright + Chromium del sistema de pruebas. Las pruebas no se cargan a visitantes. Consultar `ESTADO.md` para matriz y resultados exactos.

## Licencia y terceros

Código nuevo: MIT, ver [LICENSE](LICENSE). Interfaz con CSS y JavaScript estándar; fuentes del sistema y el carácter Unicode ☾. No se incluyen fuentes comerciales, iconos, imágenes, rastreadores ni bibliotecas de terceros. Los documentos normativos consultados para diseño son referencias, no dependencias ni recursos redistribuidos.

## Publicación

Se necesita un repositorio público bajo `Cygnixit` y permisos de administración para Pages y Release. Publicar únicamente versiones con pruebas aplicables comprobadas, hash SHA-256 del HTML offline y un archivo descargable, sin publicar `video-factory` ni su contenido privado. Los datos del espectador nunca se almacenan en el repositorio.