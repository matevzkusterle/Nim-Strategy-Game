# Nim strategy game


Nim is a mathematical game of strategy where two players take turns removing objects (such as stones) from piles. The objective is to be the player who removes the last stone.

In a version of Nim with three piles, containing 3, 5, and 7 stones respectively, the rules are as follows:

## Basic Rules of Nim:


### Initial Setup:
There are three piles of stones with:
- **Pile 1**: 3 stones
- **Pile 2**: 5 stones
- **Pile 3**: 7 stones

### Players:
- There are two players, who alternate turns.

### Taking Turns:
- On each player's turn, they must choose **one pile** and remove **at least one stone** from that pile.
- The player can remove as many stones as they wish, but only from the selected pile. They cannot take stones from multiple piles in a single turn.

### Winning Condition:
- The game continues until all the stones are removed.
- The player who **takes the last stone(s)** wins the game. The last stone can be from any pile, and it doesn’t matter how many are left when it’s their turn.

### Strategy:
- Nim is known for having a "winning strategy" based on the **Nim-sum**, which is a calculation done using the binary XOR (exclusive or) operation on the number of stones in all piles.
- If the Nim-sum (the XOR of the number of stones in all piles) is **0** at the beginning of your turn, your opponent has a winning strategy if they play optimally.
- If the Nim-sum is **non-zero**, you have a winning strategy.


## Running the App

To run the app, follow these steps:

1. Open new terminal (at first another ngrok terminal will open, do not mind it for now).
2. Navigate to the app folder.
3. Run the command:
   ```bash
   python .\backend\main.py
4. Mulitplayer mode (for this you need tho install Ngrok -> instuctions bellow)
   - When we open our folder in VS Code, the ngrok terminal automatically opens.
   - Just open another terminal to start the game, then switch to the previous terminal to open and share the link.



# 🚀 Ngrok Setup Guide for Running a Bottle Server in VS Code

## 🔹 Prerequisites
- Python installed
- Bottle framework installed (`pip install bottle`)
- VS Code installed
- Ngrok installed ([Download here](https://ngrok.com/download))

---

## ✅ Step 1: Install Ngrok (If Not Installed)
### 🔸 Windows
```sh
# Download Ngrok from the official website
https://ngrok.com/download

# Extract the file and place `ngrok.exe` in a known folder (e.g., C:\ngrok\)

# Optionally, add Ngrok to your system PATH
```

### 🔸 Mac/Linux (Terminal Command)
```sh
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```

### 🔸 Verify Ngrok Installation
```sh
ngrok version
```

