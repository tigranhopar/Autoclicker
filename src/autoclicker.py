import pyautogui
import keyboard
import threading
import time

class AutoClicker:
    def __init__(self):
        self.running = False
        self.interval = 0.8  # Default interval in seconds

    def start(self):
        self.running = True
        threading.Thread(target=self.autoclicker, daemon=True).start()

    def stop(self):
        self.running = False

    def autoclicker(self):
        while True:
            if self.running:
                pyautogui.click()
                time.sleep(self.interval)
            else:
                time.sleep(0.1)

    def set_interval(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
        self.interval = total_seconds

    def set_rate(self, rate, time_unit):
        if time_unit == 'ms':
            self.interval = rate / 1000
        elif time_unit == 's':
            self.interval = rate
        elif time_unit == 'min':
            self.interval = rate * 60
        elif time_unit == 'h':
            self.interval = rate * 3600

autoclicker = AutoClicker()