"""Genera paquete HTML, ZIP MIT y SHA-256. Depende sólo de la biblioteca estándar."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
source = root / "herramientas/aegis-exposure-sheet/index.html"
out = root / "dist"
out.mkdir(exist_ok=True)
name = "Aegis-Exposure-Sheet-v0.1.0.html"
data = source.read_bytes()
(out / name).write_bytes(data)
zip_name = "Aegis-Exposure-Sheet-v0.1.0.zip"
with ZipFile(out / zip_name, "w", ZIP_DEFLATED) as archive:
    archive.writestr(name, data)
    archive.writestr("LICENSE.txt", (root / "LICENSE").read_bytes())
checksums = "\n".join(f"{sha256((out/n).read_bytes()).hexdigest()}  {n}" for n in [name, zip_name]) + "\n"
(out / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8")
print(checksums)
