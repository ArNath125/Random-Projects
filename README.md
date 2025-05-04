# 🛡️ Cybersecurity Mini Projects

This repository contains beginner-friendly cybersecurity projects created to build foundational knowledge in ethical hacking, system security, and network reconnaissance.

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
- Scans ports 1 to 1024
- Resolves domain to IP if a URL is entered
- Grabs and prints basic banners from open ports
- Logs results to a file named `scan_results.txt`

### 💡 Purpose:
Introduces the concept of reconnaissance and fingerprinting, which are essential steps in ethical hacking and vulnerability assessments.

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- No external libraries required (uses `socket`, `re`, `getpass`, `datetime`, etc.)

### How to Run

```bash
# Run Password Strength Checker
python password_strength_checker.py

# Run Port Scanner
python port_scanner.py
