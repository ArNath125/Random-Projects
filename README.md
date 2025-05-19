# 🛡️ Cybersecurity Mini Projects

This repository contains beginner-friendly cybersecurity projects created to build foundational knowledge in ethical hacking, system security, and network reconnaissance using Python.

---

## 🔐 Project 1: Password Strength Checker

This tool evaluates the strength of a user's password based on several common security criteria. It helps users understand how secure their passwords are and encourages stronger password habits.

### ✅ Features:
- Hidden password input using `getpass`
- Checks for:
  - Minimum length (8 characters)
  - Uppercase and lowercase letters
  - Digits and special characters
- Strength meter (Weak, Moderate, Strong)

### 💡 Purpose:
Helps understand the concept of password policies and how they contribute to account security.

---

## 🌐 Project 2: Port Scanner with Banner Grabbing

This script performs a basic port scan on a target IP address and retrieves service banners from open ports to identify the services running.

### ✅ Features:
- Scans a list of common ports (21, 22, 80, 443, etc.)
- Resolves domain to IP if a URL is entered
- Grabs and prints basic banners from open ports
- Logs results to a file named `scan_result_<target>.txt`

### 💡 Purpose:
Introduces the concept of reconnaissance and fingerprinting, which are essential steps in ethical hacking and vulnerability assessments.

---

## 🔐 Project 3: File Encryption and Decryption (AES)

This tool allows you to securely encrypt and decrypt files using symmetric encryption with the `cryptography` module (AES under the hood via Fernet). It demonstrates how sensitive data can be protected using proper encryption techniques.

### ✅ Features:
- Generates a secure encryption key (`secret.key`)
- Encrypts any file to `.enc` format
- Decrypts back to original using the same key
- Simple and secure implementation using Python’s `cryptography` library

### 💡 Purpose:
Builds understanding of confidentiality, symmetric key encryption, and secure file handling.

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- `cryptography` module (for Project 3 only)

### Install Required Module

```bash
pip install cryptography
