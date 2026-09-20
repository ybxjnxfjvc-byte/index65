from pathlib import Path,PurePosixPath
import io,zipfile
ALLOWED={'.png':8_000_000,'.jpg':8_000_000,'.jpeg':8_000_000,'.pdf':12_000_000,'.csv':2_000_000,'.md':2_000_000}
def validate_name(name):
 p=PurePosixPath(name.replace('\\','/'))
 if p.is_absolute() or '..' in p.parts:return False
 return Path(p.name).suffix.lower() in ALLOWED
def validate_file(name,size): return validate_name(name) and size<=ALLOWED[Path(name).suffix.lower()]
def safe_zip_members(data:bytes):
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  return all(validate_name(i.filename) for i in z.infolist() if not i.is_dir())
