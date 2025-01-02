# Mini File Management Application

This project is a small, personal **file management application** built with **Tkinter**, a Python library for graphical user interfaces. It was orginally created to help streamline the process of moving downloaded files to their appropriate directories on my ~~regrettably~~ well-organized local drive.

The application was developed on and for macOS Sequoia 15.1.1 (24B91), tailored to my personal use cases and workflow. However, installation information is still provided below should you want to use this!

## Architecture

The application follows a **Model-View-Controller (MVC)** architecture:

- **Model**: Handles the main logic (i.e., file pathing, operations like moving, deleting files).
- **View**: The simple graphical user interface is created using Tkinter, displaying the current file to be organized, the treeview of directories, and buttons for file operation actions.
- **Controller**: Manages the interaction between the Model and the View, taking user inputs from the view (button clicks, treeview selection) and updating the model accordingly.

This architecture was chosen to promote separation of concerns, making the code easier to maintain and extend. The MVC pattern helps keep things organized, so changes to the UI can be made without messing with the underlying logic, and vice versa. While this project doesn’t __necessarily__ require this architecture, it was selected as a way to practice using it and improve the structure of the code in general.

### Features

- **Current File Display**: Shows the selected file from the file system.
- **Treeview Navigation**: Navigate the file system with an expandable treeview. View directory contents, expand/collapse nodes, and select files or directories.
- **File Movement**: Move files to new directories by selecting a destination from the treeview.
- **File Actions**: Easily delete, rename, and open files with button clicks.
- **Event Handling**: Event bindings handle node expansion and file selection, triggering UI updates for smooth interaction.
- **Dynamic Updates**: UI updates in real-time based on user selection, reflecting the current file and destination path.
- **Responsive Layout**: Interface automatically adjusts to window resizing for optimal display.

## Installation

To run the application, you need Python 3.x and the **Tkinter** library. Tkinter is typically pre-installed with Python, but if it is not installed, you can install it by following the instructions provided in [Tkinter's official documentation](https://docs.python.org/3/library/tkinter.html).

1. Clone this repository:
   ```bash
   git clone https://github.com/ianzachary/mini-file-manager.git
   cd mini-file-manager
   ```

2. Ensure Python 3.x is installed.

3. Install Tkinter (if not already installed):
   - On **Windows**, Tkinter is included by default with Python.
   - On **macOS**, Tkinter should be installed with Python, but if not, you can install it via Homebrew:
     ```bash
     brew install python-tk
     ```
   - On **Linux**, you may need to install Tkinter manually:
     ```bash
     sudo apt-get install python3-tk
     ```
4. Configure the application: 
     - The application is designed to manage files from a specified source directory (`path`) and move them to a target directory, which is selected via the GUI from the parent directory (`to_path`). For example, these directories were set as follows:
       - Default `path`: `/Users/ianalgenio/Downloads`
       - Default `to_path`: `/Users/ianalgenio`

      - To change these, modify them directly in the `Model` class.

5. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Current File Pane**: The `Current File` pane shows the currently selected file. Use the buttons (`Delete`, `Rename`, and `Open`) to perform actions on the current file.
   
2. **Directory Treeview**: The `Destination` pane displays a treeview of the file system. Navigate the tree by expanding or collapsing nodes. Select a folder to set it as the destination for moving the file.
   
3. **Move File**: The `Move` button allows you to move the current file to the selected destination directory. The selected directory will be displayed in the `Destination` text box.

4. **File Navigation**: The directory tree allows users to expand nodes and select subdirectories.

## License

This project is licensed under the MIT License - see the LICENSE file for details.