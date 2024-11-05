# Keyslogger - Encrypted Keylogging Proof of Concept  
**Developed by Ramyar Daneshgar**

Keyslogger is a Python-based proof of concept that demonstrates secure keylogging in a controlled environment. The project focuses on data encryption, real-time event handling, and GUI development, illustrating secure design principles for sensitive data processing.

**⚠️ Disclaimer**: For educational and research purposes only. All testing was performed in a secure, authorized environment.

---

## Project Highlights

- **Symmetric Encryption with Fernet**: Keystrokes are encrypted using `cryptography.fernet` symmetric encryption, ensuring secure data handling and storage in an encrypted format.
- **Real-Time Keystroke Capture with GUI Feedback**: Real-time keystroke logging and display implemented with `tkinter`, enabling immediate feedback in both encrypted and human-readable formats.
- **Controlled Logging Lifecycle**: Start/stop functions provide session control, ensuring keylogging occurs only within authorized, secure settings.

## Technical Skills Demonstrated

- **Data Encryption**: Uses symmetric encryption to protect logged data, reinforcing secure data handling practices.
- **Event-Driven GUI Development**: Implements a responsive GUI with `tkinter` for real-time display and user controls.
- **Ethical and Secure Programming**: Adheres to ethical programming standards, emphasizing controlled and authorized use.

## Setup

1. **Dependencies**: Python 3.6+, `pynput`, `cryptography`
   ```bash
   pip install pynput cryptography
   ```

2. **Execution**:
   ```bash
   python keyslogger.py
   ```

   - **Start Keylogger**: Begins capturing and encrypting keystrokes.
   - **Convert to Readable**: Decrypts and formats keystrokes for readability.
   - **Stop Keylogger**: Ends the logging session and halts data capture.

--- 



https://github.com/user-attachments/assets/9e5704a3-2e36-4f7e-9218-6e3b7b46d5f0






