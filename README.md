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

4. For mulitplayer mode:
   When we open our folder in VS Code, the ngrok terminal automatically opens. Just open another terminal to start the game, then swith to previous terminal to open and share the link.
