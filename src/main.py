import tkinter as tk
from tkinter import ttk
from ui import create_ui
from autoclicker import AutoClicker

def main():
    root = tk.Tk()
    root.title("autoclicker")
    root.geometry("560x330")
    root.configure(bg='white')

    create_ui(root)

    root.mainloop()

if __name__ == "__main__":
    main()