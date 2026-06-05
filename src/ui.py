import tkinter as tk
from tkinter import ttk, messagebox
from controller import Controller

class AutoclickerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker")
        self.root.geometry("520x380")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.controller = Controller()
        self.mode_var = tk.StringVar(value="interval")

        self.active_color = "#00a2ff"
        self.inactive_color = "#222222"

        self.create_widgets()

    def create_widgets(self):
        mode_frame = tk.Frame(self.root, bg="black")
        mode_frame.pack(pady=12)

        self.interval_button = tk.Button(
            mode_frame,
            text="Interval Mode",
            command=lambda: self.set_mode("interval"),
            width=16,
            bd=0,
            fg="white",
        )
        self.rate_button = tk.Button(
            mode_frame,
            text="Rate Mode",
            command=lambda: self.set_mode("rate"),
            width=16,
            bd=0,
            fg="white",
        )
        self.interval_button.grid(row=0, column=0, sticky="ew")
        self.rate_button.grid(row=0, column=1, sticky="ew")

        self.interval_frame = tk.Frame(self.root, bg="black")
        self.create_interval_widgets()

        self.rate_frame = tk.Frame(self.root, bg="black")
        self.create_rate_widgets()

        self.update_mode()

        button_frame = tk.Frame(self.root, bg="black")
        button_frame.pack(pady=15)

        start_button = ttk.Button(button_frame, text="Start", command=self.start_autoclicker)
        start_button.grid(row=0, column=0, padx=5)

        stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_autoclicker)
        stop_button.grid(row=0, column=1, padx=5)

        quit_button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.pack(side=tk.BOTTOM, pady=12)

    def set_mode(self, mode):
        self.mode_var.set(mode)
        self.update_mode()

    def create_interval_widgets(self):
        tk.Label(self.interval_frame, text="Hours:", bg="black", fg="white").grid(row=0, column=0)
        self.hours_entry = tk.Entry(self.interval_frame, width=5)
        self.hours_entry.grid(row=0, column=1)

        tk.Label(self.interval_frame, text="Minutes:", bg="black", fg="white").grid(row=0, column=2)
        self.minutes_entry = tk.Entry(self.interval_frame, width=5)
        self.minutes_entry.grid(row=0, column=3)

        tk.Label(self.interval_frame, text="Seconds:", bg="black", fg="white").grid(row=0, column=4)
        self.seconds_entry = tk.Entry(self.interval_frame, width=5)
        self.seconds_entry.grid(row=0, column=5)

        tk.Label(self.interval_frame, text="Milliseconds:", bg="black", fg="white").grid(row=0, column=6)
        self.milliseconds_entry = tk.Entry(self.interval_frame, width=5)
        self.milliseconds_entry.grid(row=0, column=7)

    def create_rate_widgets(self):
        tk.Label(self.rate_frame, text="Rate:", bg="black", fg="white").grid(row=0, column=0)
        self.rate_entry = tk.Entry(self.rate_frame, width=10)
        self.rate_entry.grid(row=0, column=1)

        self.unit_var = tk.StringVar(value="ms")
        unit_dropdown = ttk.Combobox(self.rate_frame, textvariable=self.unit_var, values=["ms", "s", "min", "h"], state="readonly")
        unit_dropdown.grid(row=0, column=2)

    def update_mode(self):
        if self.mode_var.get() == "interval":
            self.interval_frame.pack(pady=10)
            self.rate_frame.pack_forget()
            self.interval_button.config(bg=self.active_color, relief="raised")
            self.rate_button.config(bg=self.inactive_color, relief="flat")
        else:
            self.rate_frame.pack(pady=10)
            self.interval_frame.pack_forget()
            self.rate_button.config(bg=self.active_color, relief="raised")
            self.interval_button.config(bg=self.inactive_color, relief="flat")

    def start_autoclicker(self):
        try:
            if self.mode_var.get() == "interval":
                hours = int(self.hours_entry.get() or 0)
                minutes = int(self.minutes_entry.get() or 0)
                seconds = int(self.seconds_entry.get() or 0)
                milliseconds = int(self.milliseconds_entry.get() or 0)
                self.controller.autoclicker.set_interval(hours, minutes, seconds, milliseconds)
            else:
                rate = float(self.rate_entry.get() or 0)
                if rate <= 0:
                    raise ValueError
                self.controller.autoclicker.set_rate(rate, self.unit_var.get())
            self.controller.autoclicker.start()
        except ValueError:
            messagebox.showerror("Invalid input", "Enter valid numeric values.")

    def stop_autoclicker(self):
        self.controller.autoclicker.stop()

def create_ui(root):
    return AutoclickerUI(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = create_ui(root)
    root.mainloop()