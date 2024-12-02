# Keyslogger - Encrypted Keylogging Proof of Concept  
**Developed by Ramyar Daneshgar**

Keyslogger is a Python-based proof of concept showcasing secure and ethical keylogging techniques in a controlled environment. It emphasizes encryption, real-time event handling, and intuitive GUI design, demonstrating best practices for sensitive data processing.

**⚠️ Disclaimer**: This project is strictly for educational and research purposes. All testing has been conducted in secure, authorized environments. Unauthorized use is prohibited.

---

## Key Features

- **Secure Data Encryption**: Utilizes `cryptography.fernet` symmetric encryption to ensure all logged data is stored securely in an encrypted format.
- **Real-Time Keystroke Capture**: Captures keystrokes in real time and displays encrypted and decrypted outputs via a responsive GUI built with `tkinter`.
- **Session Control**: Start, stop, and manage logging sessions seamlessly, ensuring keylogging occurs only when explicitly authorized.

---

## Technical Highlights

- **Advanced Encryption**: Demonstrates secure data handling by encrypting keystrokes during capture and storage.  
- **GUI Development**: Implements an event-driven interface using `tkinter` for intuitive user interaction and real-time feedback.  
- **Ethical Keylogging Practices**: Focuses on controlled, authorized use cases to reinforce secure programming principles.

---

## Setup and Usage

### Prerequisites  
1. Install Python 3.6+  
2. Required packages:  
   ```bash
   pip install pynput cryptography


