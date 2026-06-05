import threading
import time
import tkinter as tk
from tkinter import messagebox

import pyautogui


class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoclicker")
        self.running = False

        self.interval_var = tk.StringVar(value="0.5")
        self.clicks_var = tk.StringVar(value="100")
        self.status_var = tk.StringVar(value="Stopped")

        tk.Label(root, text="Interval (sec)").grid(row=0, column=0, padx=8, pady=8)
        tk.Entry(root, textvariable=self.interval_var, width=10).grid(row=0, column=1, padx=8, pady=8)

        tk.Label(root, text="Click count").grid(row=1, column=0, padx=8, pady=8)
        tk.Entry(root, textvariable=self.clicks_var, width=10).grid(row=1, column=1, padx=8, pady=8)

        tk.Button(root, text="Start", command=self.start_clicking, width=10).grid(row=2, column=0, padx=8, pady=8)
        tk.Button(root, text="Stop", command=self.stop_clicking, width=10).grid(row=2, column=1, padx=8, pady=8)

        tk.Label(root, textvariable=self.status_var).grid(row=3, column=0, columnspan=2, pady=8)

    def start_clicking(self):
        if self.running:
            return

        try:
            interval = float(self.interval_var.get())
            count = int(self.clicks_var.get())
            if interval <= 0 or count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a positive number for interval and click count.")
            return

        self.running = True
        self.status_var.set("Running")
        threading.Thread(target=self.click_loop, args=(interval, count), daemon=True).start()

    def click_loop(self, interval, count):
        for i in range(count):
            if not self.running:
                break
            pyautogui.click()
            self.status_var.set(f"Clicked {i + 1}/{count}")
            time.sleep(interval)

        self.running = False
        self.status_var.set("Stopped")

    def stop_clicking(self):
        self.running = False
        self.status_var.set("Stopping...")


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
