import os
import shutil
import tempfile
import unittest


class TestRelativePath(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        print(f"{self.temp_dir = }")

        self.rel_temp_dir = os.path.relpath(self.temp_dir)
        print(f"{self.rel_temp_dir = }")

        # touch file
        with open(os.path.join(self.temp_dir, "foo.py"), "w"):
            pass
        print(f"{os.path.join(self.temp_dir, 'foo.py') = }")
        print(f"{os.path.join(self.rel_temp_dir, 'foo.py') = }")
        print(f"{os.path.exists(os.path.join(self.temp_dir, 'foo.py')) = }")
        print(f"{os.path.exists(os.path.join(self.rel_temp_dir, 'foo.py')) = }")
        print(f"{os.path.samefile(os.path.join(self.temp_dir, 'foo.py'), os.path.join(self.rel_temp_dir, 'foo.py')) = }")

        self.addCleanup(shutil.rmtree, self.temp_dir)

    def test_relative_file_path_exists(self):
        self.assertTrue(os.path.exists(os.path.join(self.rel_temp_dir, "foo.py")))
