import tempfile
import unittest
from pathlib import Path
from unittest.mock  import Mock, patch
import pyfakefs as fs
import os
from pyfakefs.fake_filesystem_unittest import TestCase

from src.FileOrganizer.SortDirectory import sort_directory


class TestSortingDirectories(unittest.TestCase):
    #In order to speed up progression, we will be implementing real test files instead of in-memory files
    #It sucks, but it will be ideal for progressing currently
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base = Path(self.temp_dir.name)
        # Create dummy files in temp directory
        (self.base / "test_textfile.txt").write_text("dummy text")
        (self.base / "test_textfile2.txt").write_text("dummy text 2")
        (self.base / "test_image.pdf").write_bytes(b"%PDF-1.4\n%EOF")

    def teatDown(self):
        self.temp_dir.cleanup()



    #Testing to see if the files exist
    def test_if_Files_Exists(self):

            # Combine open flags: Create if not exists (os.O_CREAT) and Write-Only (os.O_WRONLY)


            self.assertTrue((self.base / "test_textfile.txt").exists())
            self.assertTrue((self.base / "test_textfile2.txt").exists())
            self.assertTrue((self.base / "test_image.pdf").exists())


        #self.assertEqual(sort_directory.sort_directory(dummy), False)  # add assertion here

    def test_Sorting_Documents(self):
        sort_directory.sort_directory(str(self.base), str(self.base))
        self.assertTrue((self.base /"Document"/ "test_textfile.txt").exists())
        self.assertTrue((self.base / "Document"/ "test_image.pdf").exists())# Hold on

    def test_existing_folder(self):
        self.assertEqual(True, False)  # Hold on

if __name__ == '__main__':
    unittest.main()