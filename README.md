# 🏦 Banking System (Menu Driven)

## 📌 Overview
This is a simple Python-based banking system designed for learning purposes.  
The program allows users to create accounts, deposit money, withdraw funds, and delete accounts using a text-based menu interface.

Account information is temporarily stored using Python dictionaries across modules.

---

## ✨ Features

- Create new account with PIN authentication
- Deposit money into existing account
- Withdraw money with PIN verification
- Delete an account securely
- Error-handling for invalid credentials

---

## 🛠 Technologies & Tools Used

| Component | Details |
|----------|---------|
| Programming Language | Python 3.x |
| Data Structure | Dictionaries |
| Approach | Modular Programming |
| IDE (optional) | VS Code / PyCharm / IDLE |

---

## 🚀 Installation & Run Instructions

1. Download or clone the project folder.
2. Ensure that Python **3.x** is installed.
3. Open a terminal or IDE and run:

---

## 🧪 Instructions for Testing

Follow the steps below to verify that the system works correctly:

---

### 1️⃣ Test Account Creation
- Run the program
- Choose option **1 - Create Account**
- Enter a name, PIN, and initial balance
- Expected Result: The account should be added successfully and visible when performing further operations.

---

### 2️⃣ Test Money Deposit
- Choose option **4 - Deposit Money**
- Enter an existing account name, valid PIN, and amount
- Expected Result: Balance should increase correctly.

---

### 3️⃣ Test Money Withdrawal
- Choose option **3 - Withdraw Money**
- Enter account name, valid PIN, and amount to withdraw
- Expected Result: Balance decreases (only if sufficient funds exist).

---

### 4️⃣ Verify PIN Security
- Try depositing or withdrawing using an incorrect PIN
- Expected Result: System must display: **"Wrong PIN"** and prevent changes.

---

### 5️⃣ Test Account Deletion
- Choose option **2 - Delete Account**
- Enter correct name and PIN
- Expected Result: Account should be removed and no longer accessible.

---

### 6️⃣ Invalid Input Testing
Try the following:
- Enter a wrong option number
- Leave fields blank
- Enter a withdrawal amount greater than balance  

Expected Result: The system should handle errors without crashing.

---

If all tests work as expected, the program is considered functional.

---
