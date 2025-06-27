# Private-Public Key Generator

A **Bitcoin private key generator** with `P = k * G`, built in Python using the **secp256k1** elliptic curve. This project allows you to generate a private key, compute the corresponding public key, and understand how ECDSA keys work in Bitcoin.

---

## Features

- Generates a random private key  
- Calculates the corresponding public key using `P = k * G`  
- Uses the secp256k1 curve, as standardized in Bitcoin  
- Pure Python, minimal dependencies  

---

## Installation

Make sure you have **Python 3** installed.

Install the required Python library:

```bash
pip install ecdsa
```
Once you installed it on your terminal (Command Prompt for windows) you can execute the program you can clone the repository.
```bash
git clone https://github.com/Cornelius1124/private-key-generator.git
```
After executing the bash code you can run 
```bash
cd private-key-generator
```
Then will show
```bash
Microsoft Windows [Version 10.0.22631.5472]
(c) Microsoft Corporation. All rights reserved.

C:\Users\hp>cd private-key-generator

C:\Users\hp\private-key-generator>
```
And now you can obtain Private-Public key by
```bash
python generator_key_2.py
```



