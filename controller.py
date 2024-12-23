from model import Model
from view import View

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(self, self.root)

    def get_to_path(self): 
        """Return the current destination path from the model."""
        return self.model.get_to_path()
    
    def get_path(self):
        """Return the current path from the model."""
        return self.model.get_path()

    def get_file(self):
        """Return the current file from the model."""
        return self.model.get_file()

    def next_file(self):
        """Cycle to the next file and update the view."""
        self.model.next()
        self.view.update_view()

    def delete_file(self):
        """Delete the currently selected file and update the view."""
        current_file = self.model.get_file()
        if current_file:
            self.model.delete(current_file)
            self.view.update_view()

    def rename_file(self, old_name, new_name):
        """Rename a file and update the view."""
        if old_name and new_name:
            self.model.rename(old_name, new_name)
            self.view.update_view()

    def move_file(self, filename, destination):
        """Move a file to a new location and update the view."""
        if filename and destination:
            self.model.move(filename, destination)
            self.view.update_view()

    def open_file(self):
        """Open the currently selected file."""
        current_file = self.model.get_file()
        if current_file:
            self.model.open(current_file)

    def refresh_files(self):
        """Reload the files and update the view."""
        self.model.refresh()
        self.view.update_view()

    def start(self):
        """Start the application main loop."""
        self.root.mainloop()