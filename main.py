__name__ = "__main__"

## Python dependencies
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

## Self-Written Packages
from Physics import *

## Program entry point
if __name__ == "__main__":
    ##? GUI setup
    window = tk.Tk()
    window.title('Sci Tools by Matteo')
    # window.iconbitmap()
    window.geometry('600x400')

    ## Window Properties
    window.minsize(600, 400)
    window.attributes('-topmost', True)
    
    

    ##? run GUI
    window.mainloop()