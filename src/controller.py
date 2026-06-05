import tkinter as tk
from tkinter import ttk
from autoclicker import AutoClicker

class Controller:
    def __init__(self, root):
        self.root = root
        self.autoclicker = AutoClicker()
        self.mode = "interval"  # Default mode
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Autoclicker GUI")
        self.root.geometry("400x300")
        
        self.mode_frame = ttk.Frame(self.root)
        self.mode_frame.pack(pady=10)

        self.interval_button = ttk.Button(self.mode_frame, text="Interval Mode", command=self.set_interval_mode)
        self.interval_button.pack(side=tk.LEFT, padx=5)

        self.rate_button = ttk.Button(self.mode_frame, text="Rate Mode", command=self.set_rate_mode)
        self.rate_button.pack(side=tk.LEFT, padx=5)

        self.settings_frame = ttk.Frame(self.root)
        self.settings_frame.pack(pady=10)

        self.interval_label = ttk.Label(self.settings_frame, text="Set Interval (h:m:s:ms):")
        self.interval_label.grid(row=0, column=0)

        self.hours_entry = ttk.Entry(self.settings_frame, width=5)
        self.hours_entry.grid(row=0, column=1)

        self.minutes_entry = ttk.Entry(self.settings_frame, width=5)
        self.minutes_entry.grid(row=0, column=2)

        self.seconds_entry = ttk.Entry(self.settings_frame, width=5)
        self.seconds_entry.grid(row=0, column=3)

        self.milliseconds_entry = ttk.Entry(self.settings_frame, width=5)
        self.milliseconds_entry.grid(row=0, column=4)

        self.rate_label = ttk.Label(self.settings_frame, text="Set Rate:")
        self.rate_label.grid(row=1, column=0)

        self.rate_entry = ttk.Entry(self.settings_frame, width=5)
        self.rate_entry.grid(row=1, column=1)

        self.unit_var = tk.StringVar(value="ms")
        self.unit_dropdown = ttk.Combobox(self.settings_frame, textvariable=self.unit_var, values=["ms", "s", "min", "h"])
        self.unit_dropdown.grid(row=1, column=2)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_autoclicker)
        self.start_button.pack(pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def set_interval_mode(self):
        self.mode = "interval"
        self.rate_entry.config(state='disabled')
        self.hours_entry.config(state='normal')
        self.minutes_entry.config(state='normal')
        self.seconds_entry.config(state='normal')
        self.milliseconds_entry.config(state='normal')

    def set_rate_mode(self):
        self.mode = "rate"
        self.rate_entry.config(state='normal')
        self.hours_entry.config(state='disabled')
        self.minutes_entry.config(state='disabled')
        self.seconds_entry.config(state='disabled')
        self.milliseconds_entry.config(state='disabled')

    def start_autoclicker(self):
        if self.mode == "interval":
            hours = int(self.hours_entry.get() or 0)
            minutes = int(self.minutes_entry.get() or 0)
            seconds = int(self.seconds_entry.get() or 0)
            milliseconds = int(self.milliseconds_entry.get() or 0)
            interval = (hours * 3600 + minutes * 60 + seconds) + milliseconds / 1000
            self.autoclicker.set_interval(interval)
        else:
            rate = int(self.rate_entry.get() or 0)
            unit = self.unit_var.get()
            self.autoclicker.set_rate(rate, unit)

        self.autoclicker.start()

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()