# Simple Blockchain in Python 🐍🧱⛓️

Exploring the foundational concepts of blockchain with this simple Python implementation. This project demonstrates the core principles of blockchain, including mining, nonce, SHA-256 hashing, and proof of work.

## Features

- **Block Structure**: Each block contains data, a nonce, a previous hash, and a SHA-256 hash.
- **Proof of Work**: Implements a proof-of-work algorithm to secure the blockchain.
- **Mining**: Demonstrates the mining process, where a nonce is incremented until a valid hash is found.
- **Chain Integrity**: Ensures the integrity and security of the chain by linking blocks with cryptographic hashes.
- **Simple Python Implementation**: Written in Python, making it easy to understand.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3** 🐍 for running the application

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/viniciusfinger/python-blockchain.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd python-blockchain
   ```

3. **Run the project:**
   ```bash
   python3 main.py
   ```

## How It Works

1. **Block Creation**: Each block in the blockchain contains transaction data, a nonce, the previous block's hash, and the current block's hash.
2. **Mining**: To add a block to the blockchain, a proof of work must be found by solving a computational puzzle. This involves finding a nonce that, when combined with the block data, produces a hash with a certain number of leading zeros.
3. **Hashing**: SHA-256 is used to create a secure and unique identifier for each block.
4. **Difficulty**: The difficulty and the proof of work prefix are setted in the `blockchain.py` file, so you can change it and test different possibilities.