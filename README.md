# 🧠 Brain Buster – Memory Matching Game

Welcome to **Brain Buster**, a terminal-based memory game written in Python. This classic card-flip matching game challenges players to test their memory by revealing and matching hidden pairs on a grid.

---

## 🎮 Game Description

In **Brain Buster**, players flip hidden tiles to find pairs. The game includes a scoring system based on performance, an anti-cheating mechanism, and various grid sizes to increase difficulty. Players can choose between different interaction modes or give up and reveal the grid.

---

## 🧩 Features

- ✅ Interactive CLI interface  
- ✅ Grid sizes: 2x2, 4x4, or 6x6  
- ✅ Turn-based matching logic  
- ✅ Option to reveal single elements (with penalty)  
- ✅ Cheating detection and scoring rules  
- ✅ Dynamic grid generation with randomized pairs  
- ✅ Replayable: start new games anytime  

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/brain-buster.git
   cd brain-buster
   ```

2. **Ensure Python 3 is installed**:
   ```bash
   python3 --version
   ```

---

## ▶️ Usage

Run the game via the command line:

```bash
python3 game.py
```

You can optionally provide a grid size:

```bash
python3 game.py 4  # Starts a 4x4 game
```

---

## 🎯 Gameplay Options

Once the game launches, you'll see a menu with the following options:

1. **Select two elements** – Try to match a pair.  
2. **Uncover one element** – Reveal one cell (adds penalty).  
3. **Give up** – Reveal the full grid.  
4. **New game** – Start a fresh game with a chosen grid size.  
5. **Exit** – Close the game.  

The grid is labeled with **columns A-Z** and **rows 0–(n-1)** for input clarity (e.g., `A0`, `B2`).

---

## 🧮 Scoring System

- **Score = (Minimum Guesses / Actual Guesses) × 100**
- Using *Option 2* (reveal one cell) adds 2 to your guess count.
- Using only Option 2 or revealing all cells results in a score of **0**.
- Matching all pairs earns a congratulatory message and your score.

---

## 📁 File Structure

```bash
src
  ├── game.py     # Main game loop and CLI interaction
  └── grid.py     # Grid logic, generation, and helper methods
```

---

## 📦 Dependencies

No external dependencies are required. Built with the Python standard library only.
