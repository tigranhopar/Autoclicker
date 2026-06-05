import tkinter as tk
from tkinter import ttk
from controller import Controller

HOTKEY_PRESETS = [
    ("F6", "f6"),
    ("F7", "f7"),
    ("F8", "f8"),
    ("F9", "f9"),
    ("F10", "f10"),
    ("\\", "\\"),
    ("`", "`"),
    ("§", "§"),
    ("-", "-"),
    ("=", "="),
    ("[", "["),
    ("]", "]"),
]

KEYSYM_TO_HOTKEY = {
    "backslash": "\\",
    "grave": "`",
    "section": "§",
    "minus": "-",
    "equal": "=",
    "bracketleft": "[",
    "bracketright": "]",
    "space": "space",
    "Return": "enter",
    "Escape": "escape",
    "Tab": "tab",
}

HOTKEY_TO_DISPLAY = {
    "f6": "F6",
    "f7": "F7",
    "f8": "F8",
    "f9": "F9",
    "f10": "F10",
    "\\": "\\",
    "`": "`",
    "§": "§",
}

class AutoclickerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker")
        self.root.geometry("560x330")
        self.root.configure(bg="black")

        self.controller = Controller(on_status_change=self._on_autoclicker_status_change)

        self.mode_var = tk.StringVar(value="interval")
        self.listening_for_hotkey = False
        self._hotkey_capture_bind_id = None

        self.create_widgets()

    def create_widgets(self):
        quit_button = ttk.Button(self.root, text="Quit", command=self.quit)
        quit_button.pack(side=tk.BOTTOM, pady=15)

        header_frame = tk.Frame(self.root, bg="black")
        header_frame.pack(fill=tk.X, padx=15, pady=(10, 0))

        self.status_label = tk.Label(
            header_frame,
            text="Stopped",
            bg="black",
            fg="#e74c3c",
            font=("Helvetica", 12, "bold"),
        )
        self.status_label.pack(side=tk.RIGHT)

        mode_frame = tk.Frame(self.root, bg="black")
        mode_frame.pack(pady=10)

        self.mode_button = ttk.Button(mode_frame, text="Switch to Rate", command=self.toggle_mode)
        self.mode_button.grid(row=0, column=0, padx=5)

        self.interval_frame = tk.Frame(self.root, bg="black")
        self.create_interval_widgets()

        self.rate_frame = tk.Frame(self.root, bg="black")
        self.create_rate_widgets()

        self.update_mode()
        self.create_hotkey_widgets()

    def toggle_mode(self):
        if self.mode_var.get() == "interval":
            self.mode_var.set("rate")
            self.mode_button.config(text="Switch to Interval")
        else:
            self.mode_var.set("interval")
            self.mode_button.config(text="Switch to Rate")
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

    def create_hotkey_widgets(self):
        hotkey_frame = tk.Frame(self.root, bg="black")
        hotkey_frame.pack(pady=15, fill="x")

        tk.Label(hotkey_frame, text="Toggle Hotkey:", bg="black", fg="white").grid(row=0, column=0, padx=5)

        self.hotkey_display_var = tk.StringVar(
            value=self._hotkey_to_display(self.controller.hotkey)
        )
        self.hotkey_field = tk.Frame(
            hotkey_frame,
            bg="#2a2a2a",
            highlightbackground="#666",
            highlightthickness=1,
            width=160,
            height=28,
        )
        self.hotkey_field.grid(row=0, column=1, padx=5)
        self.hotkey_field.grid_propagate(False)

        self.hotkey_label = tk.Label(
            self.hotkey_field,
            textvariable=self.hotkey_display_var,
            bg="#2a2a2a",
            fg="white",
            anchor="w",
            padx=8,
        )
        self.hotkey_label.pack(fill=tk.BOTH, expand=True)

        for widget in (self.hotkey_field, self.hotkey_label):
            widget.bind("<Button-1>", self.start_hotkey_capture)

        presets_button = ttk.Menubutton(hotkey_frame, text="Presets")
        presets_menu = tk.Menu(presets_button, tearoff=0)
        for label, hotkey in HOTKEY_PRESETS:
            presets_menu.add_command(
                label=label,
                command=lambda h=hotkey, d=label: self.apply_hotkey_preset(h, d),
            )
        presets_button["menu"] = presets_menu
        presets_button.grid(row=0, column=2, padx=5)

    def _hotkey_to_display(self, hotkey):
        return HOTKEY_TO_DISPLAY.get(hotkey, hotkey.upper() if len(hotkey) > 1 else hotkey)

    def _event_to_hotkey(self, event):
        keysym = event.keysym
        if keysym.startswith("F") and keysym[1:].isdigit():
            return keysym.lower()
        if keysym in KEYSYM_TO_HOTKEY:
            return KEYSYM_TO_HOTKEY[keysym]
        if event.char and event.char.isprintable():
            return event.char
        return None

    def start_hotkey_capture(self, _event=None):
        if self.listening_for_hotkey:
            return
        self.listening_for_hotkey = True
        self.hotkey_display_var.set("Press a key...")
        self._hotkey_capture_bind_id = self.root.bind(
            "<KeyPress>", self._on_hotkey_capture, add="+"
        )

    def _on_hotkey_capture(self, event):
        if not self.listening_for_hotkey:
            return

        if event.keysym == "Escape":
            self._cancel_hotkey_capture()
            return "break"

        hotkey = self._event_to_hotkey(event)
        if not hotkey:
            return "break"

        self._stop_hotkey_capture()
        self.hotkey_display_var.set(self._hotkey_to_display(hotkey))
        self.controller.set_hotkey(hotkey)
        return "break"

    def _cancel_hotkey_capture(self):
        self._stop_hotkey_capture()
        self.hotkey_display_var.set(self._hotkey_to_display(self.controller.hotkey))

    def _stop_hotkey_capture(self):
        self.listening_for_hotkey = False
        if self._hotkey_capture_bind_id is not None:
            self.root.unbind("<KeyPress>", self._hotkey_capture_bind_id)
            self._hotkey_capture_bind_id = None

    def apply_hotkey_preset(self, hotkey, display):
        self._cancel_hotkey_capture()
        self.hotkey_display_var.set(display)
        self.controller.set_hotkey(hotkey)

    def _on_autoclicker_status_change(self, running):
        self.root.after(0, lambda: self.update_status(running))

    def update_status(self, running):
        if running:
            self.status_label.config(text="Running", fg="#2ecc71")
        else:
            self.status_label.config(text="Stopped", fg="#e74c3c")

    def quit(self):
        self.controller.cleanup()
        self.root.quit()

    def update_mode(self):
        if self.mode_var.get() == "interval":
            self.interval_frame.pack(pady=10)
            self.rate_frame.pack_forget()
        else:
            self.rate_frame.pack(pady=10)
            self.interval_frame.pack_forget()

def create_ui(root):
    return AutoclickerUI(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = create_ui(root)
    root.mainloop()