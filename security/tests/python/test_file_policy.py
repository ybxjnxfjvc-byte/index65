import unittest,sys,io,zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'lab'))
from file_policy import validate_file,safe_zip_members
class T(unittest.TestCase):
 def test_traversal(self): self.assertFalse(validate_file('../secret.png',10))
 def test_size(self): self.assertFalse(validate_file('x.png',9_000_000)); self.assertTrue(validate_file('x.png',100))
 def test_zip_slip(self):
  b=io.BytesIO();
  with zipfile.ZipFile(b,'w') as z:z.writestr('../evil.png',b'x')
  self.assertFalse(safe_zip_members(b.getvalue()))
if __name__=='__main__':unittest.main()
