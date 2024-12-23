import os
import shutil
import subprocess
from collections import deque

class Model:
    def __init__(self, path='/Users/ianalgenio/Downloads', to_path='/Users/ianalgenio'):
        self.path = path
        self.to_path = to_path
        self.files = deque()
        self._load_files()

    def _load_files(self):
        """Load files from the directory into the deque."""
        self.files.clear()
        for entry in os.listdir(self.path):
            if not (entry.startswith('.') or entry.startswith('~$')):  # Ignore hidden, temporary files
                self.files.append(entry)
                
    def get_to_path(self):
        """Get the current directory path."""
        return self.to_path
    
    def get_path(self):
        """Get the current directory path."""
        return self.path

    def get_file(self):
        """Get the current file at the front of the deque."""
        return self.files[0] if self.files else None

    def next(self):
        """Move to the next file in the deque, cycling to the front if needed."""
        if self.files:
            self.files.rotate(-1)  # Rotate left to move the first item to the back
        return self.get_file()

    def delete(self, filename):
        """Delete a file from the filesystem and remove it from the deque."""
        file_path = os.path.join(self.path, filename)
        if filename in self.files:
            self.files.remove(filename)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

    def rename(self, old, new):
        """Rename a file in the filesystem and update the deque."""
        old_path = os.path.join(self.path, old)
        new_path = os.path.join(self.path, new)
        if old in self.files:
            os.rename(old_path, new_path)
            self.files[self.files.index(old)] = new

    def open(self, filename):
        """Open a file or directory using the default system application."""
        file_path = os.path.join(self.path, filename)
        if filename in self.files:
            subprocess.call(('open', file_path))

    def move(self, origin, dest):
        """Move a file or directory to a new location."""
        origin_path = os.path.join(self.path, origin)
        dest_path = os.path.join(self.path, dest)
        if origin in self.files:
            shutil.move(origin_path, dest_path)
            self.files.remove(origin)  # Remove from current list after moving
            self._load_files()  # Refresh files to include the moved file if within the same directory

    def refresh(self):
        """Reload the files in the directory to reflect any external changes."""
        self._load_files()