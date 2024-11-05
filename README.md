# Keyslogger - Secure Keylogging Proof of Concept for Security Research  
**Developed by Ramyar Daneshgar**

Keyslogger is a Python-based proof of concept designed to demonstrate secure keylogging within an ethical, controlled framework. This project highlights core competencies in data encryption, GUI design, and real-time data processing—all critical skills for secure software development.

**⚠️ Disclaimer**: This tool is intended exclusively for educational and security research purposes. All usage and testing were conducted in a secure, authorized environment.

---

## Key Project Highlights

- **End-to-End Encrypted Data Storage**: Keystrokes are encrypted using `cryptography.fernet` before being logged, ensuring secure handling of sensitive information and showcasing robust data protection practices.
- **Real-Time Monitoring GUI**: A `tkinter` interface provides instant feedback on captured keystrokes, viewable in both encrypted and human-readable formats—demonstrating real-time processing and GUI expertise.
- **Controlled and Ethical Keylogging**: Start/stop functionality ensures logging only occurs within an authorized, controlled environment, aligning with ethical programming standards.

## Technical Skills Demonstrated

- **Advanced Encryption Techniques**: Demonstrated expertise in secure data handling by implementing symmetric encryption to protect sensitive information.
- **Python GUI Development**: Designed an intuitive, responsive GUI to enable seamless interaction and data visualization in real-time.
- **Secure, Ethical Programming**: Developed with a strong focus on ethical considerations, emphasizing responsible usage and security practices for sensitive tools.

## Setup and Usage

1. **Requirements**: Python 3.6+, with `pynput` and `cryptography` libraries.
   ```bash
   pip install pynput cryptography
   ```

2. **Running the Application**:
   ```bash
   python keyslogger.py
   ```

   - **Start Keylogger**: Begin logging keystrokes in an encrypted format.
   - **Convert to Readable Format**: View keystrokes in a readable format for analysis.
   - **Stop Keylogger**: End the session securely.

---

### Ethical Considerations

- **Educational and Security Research Focus**: Developed strictly as a learning tool for ethical security research.
- **Strict Adherence to Legal Guidelines**: Unauthorized keylogging is illegal; this tool was designed to showcase ethical programming in controlled environments only.


