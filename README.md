# 🛡️ Cybersecurity Mini Projects

This repository contains beginner-friendly cybersecurity projects focused on ethical hacking, system security, encryption, and network reconnaissance — all built with Python.

---

## 🔐 Project 1: Password Strength Checker

This tool evaluates the strength of a user's password based on multiple criteria and gives a strength score.

### ✅ Features:
- Hidden input using `getpass`
- Checks for:
  - Length
  - Uppercase, lowercase, digits, special characters
- Displays strength (Weak, Moderate, Strong)

---

## 🌐 Project 2: Port Scanner with Banner Grabbing

Scans common TCP ports on a given host and grabs banners to identify running services.

### ✅ Features:
- Scans a list of common ports (21, 22, 80, 443, etc.)
- Banner grabbing using raw socket read
- Logs results to a file

---

## 🗝️ Project 3: File Encryption & Decryption

Encrypts and decrypts files using AES encryption via the Python `cryptography` library.

### ✅ Features:
- Generates and stores AES keys (`Fernet`)
- Encrypts any binary/text file
- Decrypts back to original file
- Simple key reuse via `secret.key`

---

## 📁 Project 4: Secure File Transfer with Authentication & Hybrid Encryption

A simulated file transfer system with:
- ✅ Hashed password authentication (`bcrypt`)
- ✅ Hybrid encryption (RSA to exchange AES key, AES to encrypt file)
- ✅ Encrypted transmission over socket simulation

### ✅ Features:
- **User login** with hashed passwords
- **RSA** key generation and secure AES key exchange
- **AES** (Fernet) used for encrypting the file content
- **Client–Server structure** simulated via Python scripts or notebook

### 💡 Learning Highlights:
- Public/private key encryption
- Symmetric key file encryption
- Secure password storage and verification
- Realistic layering of authentication + encryption

---

## 🚀 Getting Started

### Requirements
```bash
pip install cryptography bcrypt
