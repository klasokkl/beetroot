import unittest
import os
import tempfile
from contextlib import redirect_stdout
from task1 import FileManager  # замените на имя файла с классом

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.temp_file.close()

        FileManager.operation_counter = 0
        if os.path.exists(FileManager.log_file):
            os.remove(FileManager.log_file)

    def tearDown(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)
        if os.path.exists(FileManager.log_file):
            os.remove(FileManager.log_file)


    def test_write_and_read(self):
        with FileManager(self.temp_file_name, "w", encoding="utf-8") as f:
            f.write("Hello")

        with FileManager(self.temp_file_name, "r", encoding="utf-8") as f:
            content = f.read()
        
        self.assertEqual(content, "Hello")
        self.assertEqual(FileManager.operation_counter, 2)  

    def test_logs_created(self):
        with FileManager(self.temp_file_name, "w", encoding="utf-8") as f:
            f.write("Test log")

        with open(FileManager.log_file, "r", encoding="utf-8") as log:
            logs = log.read()
        
        self.assertIn("Opened file", logs)
        self.assertIn("Wrote", logs)
        self.assertIn("Closed file", logs)


    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            with FileManager(self.temp_file_name, "invalid_mode") as f:
                pass

    def test_exception_inside_with(self):
        try:
            with FileManager(self.temp_file_name, "w", encoding="utf-8") as f:
                f.write("Before error")
                raise RuntimeError("Test error")
        except RuntimeError as e:
            self.assertEqual(str(e), "Test error")

        with open(FileManager.log_file, "r", encoding="utf-8") as log:
            logs = log.read()
        self.assertIn("Closed file", logs)
        self.assertIn("Exception: RuntimeError", logs)

    def test_counter_increment(self):
        with FileManager(self.temp_file_name, "w", encoding="utf-8") as f:
            f.write("One")
            f.write("Two")
        self.assertEqual(FileManager.operation_counter, 2)

    def test_read_empty_file(self):
        with FileManager(self.temp_file_name, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "")
        self.assertEqual(FileManager.operation_counter, 1)


if __name__ == "__main__":
    unittest.main()
