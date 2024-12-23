from tkinter import *
from model import Model
from view import View
from controller import Controller

def main():
    # Initialize
    root = Tk()
    root.title("Mini Manager")
    
    controller = Controller(root)
    controller.start()

if __name__ == '__main__':
    main()