# 🛡️ Cybersecurity Mini Projects

This repository contains beginner-friendly cybersecurity projects built with Python to explore core concepts like ethical hacking, encryption, vulnerability analysis, and secure communication.

---

## 🔐 Project 1: Password Strength Checker

This tool checks the strength of a user's password and encourages strong password habits.

### ✅ Features:
- Hidden password input using `getpass`
- Checks for:
  - Minimum length
  - Uppercase, lowercase, digits, special characters
- Strength meter: Weak, Moderate, or Strong

---

## 🌐 Project 2: Port Scanner with Banner Grabbing

Scans common TCP ports on a host and grabs banners to identify services running on those ports.

### ✅ Features:
- Scans common ports (1–1024)
- Banner grabbing using socket
- Domain/IP support
- Results saved to a file

---

## 🔐 Project 3: File Encryption & Decryption

Encrypt and decrypt any file using AES symmetric encryption (`Fernet` from `cryptography`).

### ✅ Features:
- AES key generation and reuse
- File encryption (any type)
- Secure decryption
- CLI-based file selection

---

## 📁 Project 4: Secure File Transfer with Authentication & Hybrid Encryption

A secure simulation of encrypted file transfer with password-based authentication.

### ✅ Features:
- Password authentication (with `bcrypt` hashing)
- Hybrid encryption:
  - AES for file encryption
  - RSA for secure key exchange
- Client-server architecture using Python sockets
- Optional notebook-based implementation

### 💡 Concepts Covered:
- Hybrid encryption (used in HTTPS)
- Fernet + RSA usage
- Secure client-server communications

---

## 🧪 Project 5: Vulnerability Scanner using Nmap

Performs automated scanning for open ports, running services, OS information, and potential vulnerabilities using Nmap.

### ✅ Features:
- Open port and version detection (`-sV`)
- Operating system detection (`-O`)
- Vulnerability detection (`--script vuln`)
- HTTP-specific scans (`--script http-*`)
- Real-time scan progress & formatted results

### ⚠️ Requirements:
- `nmap` must be installed on your system
- Run with elevated privileges for `-O` and some scripts

### 💡 Concepts Covered:
- Reconnaissance and footprinting
- OS fingerprinting
- Script-based vulnerability detection
- HTTP scanning and enumeration

---

## 🚀 Getting Started

### Prerequisites

Install Python packages:
```bash
pip install cryptography bcrypt python-nmap
