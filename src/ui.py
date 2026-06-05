import tkinter as tk
from tkinter import ttk
from controller import Controller

class AutoclickerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker")
        self.root.geometry("400x300")
        self.root.configure(bg="#D3D3D3")

        self.controller = Controller()

        self.mode_var = tk.StringVar(value="interval")

        self.create_widgets()

    def create_widgets(self):
        mode_frame = ttk.Frame(self.root)
        mode_frame.pack(pady=10)

        interval_button = ttk.Radiobutton(mode_frame, text="Interval", variable=self.mode_var, value="interval", command=self.update_mode)
        interval_button.grid(row=0, column=0, padx=5)

        rate_button = ttk.Radiobutton(mode_frame, text="Rate", variable=self.mode_var, value="rate", command=self.update_mode)
        rate_button.grid(row=0, column=1, padx=5)

        self.interval_frame = ttk.Frame(self.root)
        self.interval_frame.pack(pady=10)

        self.create_interval_widgets()

        self.rate_frame = ttk.Frame(self.root)

        self.create_rate_widgets()

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        toggle_button = ttk.Button(button_frame, text="Toggle Autoclicker", command=self.controller.toggle_autoclicker)
        toggle_button.grid(row=0, column=0, padx=5)

        quit_button = ttk.Button(button_frame, text="Quit", command=self.root.quit)
        quit_button.grid(row=0, column=1, padx=5)

    def create_interval_widgets(self):
        tk.Label(self.interval_frame, text="Hours:").grid(row=0, column=0)
        self.hours_entry = tk.Entry(self.interval_frame, width=5)
        self.hours_entry.grid(row=0, column=1)

        tk.Label(self.interval_frame, text="Minutes:").grid(row=0, column=2)
        self.minutes_entry = tk.Entry(self.interval_frame, width=5)
        self.minutes_entry.grid(row=0, column=3)

        tk.Label(self.interval_frame, text="Seconds:").grid(row=0, column=4)
        self.seconds_entry = tk.Entry(self.interval_frame, width=5)
        self.seconds_entry.grid(row=0, column=5)

        tk.Label(self.interval_frame, text="Milliseconds:").grid(row=0, column=6)
        self.milliseconds_entry = tk.Entry(self.interval_frame, width=5)
        self.milliseconds_entry.grid(row=0, column=7)

    def create_rate_widgets(self):
        tk.Label(self.rate_frame, text="Rate:").grid(row=0, column=0)
        self.rate_entry = tk.Entry(self.rate_frame, width=10)
        self.rate_entry.grid(row=0, column=1)

        self.unit_var = tk.StringVar(value="ms")
        unit_dropdown = ttk.Combobox(self.rate_frame, textvariable=self.unit_var, values=["ms", "s", "min", "h"], state="readonly")
        unit_dropdown.grid(row=0, column=2)

    def update_mode(self):
        if self.mode_var.get() == "interval":
            self.interval_frame.pack(pady=10)
            self.rate_frame.pack_forget()
        else:
            self.rate_frame.pack(pady=10)
            self.interval_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoclickerUI(root)
    root.mainloop()