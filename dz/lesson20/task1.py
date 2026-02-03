import os
from functools import wraps

class FileManager:
    log_file = "file_manager.log"  
    operation_counter = 0          

    def __init__(self, filename, mode="r", encoding=None):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self._log(f"Opened file '{self.filename}' in mode '{self.mode}'")
        return self  

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            self._log(f"Closed file '{self.filename}'")
        if exc_type:
            self._log(f"Exception: {exc_type.__name__}: {exc_val}")
        return False

    def read(self, *args, **kwargs):
        result = self.file.read(*args, **kwargs)
        self._increment_counter()
        self._log(f"Read {len(result)} characters from '{self.filename}'")
        return result

    def write(self, data):
        self.file.write(data)
        self._increment_counter()
        self._log(f"Wrote {len(data)} characters to '{self.filename}'")

    def _increment_counter(self):
        FileManager.operation_counter += 1

    def _log(self, message):
        with open(FileManager.log_file, "a", encoding="utf-8") as log:
            log.write(message + "\n")

with FileManager("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!")

with FileManager("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print("ok", FileManager.operation_counter)
