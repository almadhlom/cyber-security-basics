# Introduction to Encryption Basics

Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext) to prevent unauthorized access. It is a fundamental concept in cybersecurity used to ensure data confidentiality.

## Types of Encryption

### 1. Symmetric Encryption
* Uses the **same secret key** to both encrypt and decrypt the data.
* Fast and efficient, but requires a secure way to share the key between users.
* **Common Algorithms:** AES (Advanced Encryption Standard), DES, Blowfish.

### 2. Asymmetric Encryption (Public-Key Cryptography)
* Uses a **pair of keys**: a **Public Key** (which anyone can use to encrypt data) and a corresponding **Private Key** (kept secret by the owner to decrypt data).
* Highly secure for communication over public networks because the private key is never shared.
* **Common Algorithms:** RSA, ECC (Elliptic Curve Cryptography).

## Common Use Cases
* Securing website traffic via HTTPS (SSL/TLS protocols)
* Encrypting sensitive stored data (File/Disk encryption)
* Secure communication apps (End-to-End Encryption in chat apps)
