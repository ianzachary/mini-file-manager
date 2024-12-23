import os
from tkinter import *
from tkinter import ttk

class View:
    def __init__(self, controller, root):
        self.controller = controller
        self.nodes = dict()

        # Initialize panes
        self.panes = PanedWindow(root, orient=VERTICAL, sashpad=5)
        self.p1 = LabelFrame(self.panes, padx=10, pady=10, text='Current File:  ', height=100, width=200)
        self.p2 = LabelFrame(self.panes, padx=10, pady=10, text='Destination:  ', height=100, width=200)

        # Create UI elements for panes
        self._setup_pane1()
        self._setup_pane2()

        # Pack panes
        self.panes.add(self.p1)
        self.panes.add(self.p2)
        self.panes.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)

    def _setup_pane1(self):
        self.p1.grid_anchor(W)
        self.p1.grid_columnconfigure(0, weight=1)
        self.p1.grid_rowconfigure(0, weight=1)

        # Current file display
        self.curr_file = Text(self.p1, relief=SUNKEN, width=60, height=1, wrap=NONE, bg="#1E1E1E")
        self.curr_file.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
        self.curr_file.insert('1.0', self.controller.get_file())
        
        # Buttons
        self.delete_button = ttk.Button(self.p1, text='Delete', command=self.controller.delete_file)
        self.delete_button.grid(row=1, column=0, padx=10, sticky=W)
        # self.rename_button = ttk.Button(self.p1, text='Rename', command=self.controller.rename_file)
        # self.rename_button.grid(row=1, column=0, padx=5, sticky=W)
        self.open_button = ttk.Button(self.p1, text='Open', default=ACTIVE, command=self.controller.open_file)
        self.open_button.grid(row=1, column=0, padx=10, sticky=E)

    def _setup_pane2(self):
        # Treeview for directories
        self.tree = ttk.Treeview(self.p2, show='tree')
        self.p2.columnconfigure(0, weight=1)
        self.p2.rowconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky=NSEW, padx=2.5)
        
        # Bind Treeview events
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<<TreeviewSelect>>', self.select_node)

        # Destination directory display
        self.destination_display = Text(self.p2, relief=SUNKEN, width=60, height=1, wrap=NONE, bg="#1E1E1E")
        self.destination_display.grid(row=2, column=0, sticky=NSEW)
        self.destination_display.insert('1.0', "(Select from Tree)")

        # Buttons (next file, move)
        self.next_button = ttk.Button(self.p2, text='Next File', default=NORMAL, command=self.controller.next_file)
        self.next_button.grid(row=3, column=0, padx=10, sticky=W)
        self.move_button = ttk.Button(self.p2, text='Move', default=ACTIVE, command=self.controller.move_file)
        self.move_button.grid(row=3, column=0, padx=10, sticky=E)
        
        # Initialize tree with root directory
        self.refresh_tree()

    def refresh_tree(self):
        """Refresh the directory tree structure."""
        self.tree.delete(*self.tree.get_children())  # Clear existing nodes
        abspath = os.path.abspath(self.controller.get_to_path())
        self.insert_node('', abspath, abspath)

    def insert_node(self, parent, text, abspath):
        """Insert a node into the tree view."""
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')  # Add a dummy child to show expandable nodes

    def select_node(self, e):
        """Handle selecting a node in the tree view."""
        node = self.tree.focus()
        abspath = self.nodes.get(node, None)
        if abspath:
            self.destination_display.delete('1.0', END)
            self.destination_display.insert('1.0', abspath)

    def open_node(self, e):
        """Handle expanding a node in the tree view."""
        node = self.tree.focus()
        abspath = self.nodes.get(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))  # Remove dummy children
            for p in os.listdir(abspath):
                if not (p.startswith('.') or p.startswith('~$')):
                    self.insert_node(node, p, os.path.join(abspath, p))

    def update_view(self):
        """Refresh or update all UI elements based on the controller state."""
        # Refresh current file display
        self.curr_file.delete('1.0', END)
        self.curr_file.insert('1.0', self.controller.get_file())