# 🧠 Wumpus World Game (Python - OOP)

A terminal-based implementation of the classic **Wumpus World** environment using **Object-Oriented Programming (OOP)** in Python.
This project simulates an intelligent agent navigating a hazardous grid world while using percepts to avoid danger and find the gold.

---

## 🎮 Features

* 🗺️ **Dynamic Grid Generation (4x4)**
* 🧠 **Percept-Based Gameplay**

  * `S` → Stench (Wumpus nearby)
  * `B` → Breeze (Pit nearby)
* 👤 **Agent-Based Movement**
* ❓ **Fog of War System**
* 📍 **Safe Start Zone**

  * No Wumpus or Pits in:

    * `(0,0)` (Start)
    * `(1,0)`
    * `(0,1)`
* 🧩 **OOP Architecture**

  * Clean separation of logic using classes
* 🖥️ **Terminal UI with Live Map Updates**

---

## 🏗️ Project Structure

```
WumpusWorldGame/
│
├── main.py          # Entry point
├── WumpusWorld      # Environment logic (grid, hazards, percepts)
├── Player           # Agent logic (movement, state)
├── Game             # Game loop and UI handling
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wumpus-world.git
cd wumpus-world
```

### 2. Run the Game

```bash
python main.py
```

---

## 🎯 Gameplay Instructions

### Controls:

```
W → Move Up
S → Move Down
A → Move Left
D → Move Right
```

---

## 🧭 Objective

* 🏆 Find the **Gold (G)**
* 💀 Avoid:

  * Wumpus (`W`)
  * Pits (`P`)

---

## 🗺️ Map Legend

| Symbol            | Meaning                |
| ----------------- | ---------------------- |
| `A`               | Agent                  |
| `S`               | Stench (Wumpus nearby) |
| `B`               | Breeze (Pit nearby)    |
| `.`               | Safe visited cell      |
| `?`               | Unknown cell           |
| `AS`, `AB`, `ASB` | Agent + percepts       |

> ⚠️ The actual positions of Wumpus, pits, and gold are hidden during gameplay.

---

## 🧠 Game Logic

* The agent starts at `(0,0)`
* The environment is randomly generated
* Percepts are added to adjacent cells:

  * Wumpus → `S` (Stench)
  * Pit → `B` (Breeze)
* Player must **infer danger** based on percepts

---

## 🔍 Example Gameplay

```
['A', '?', '?', '?']
['?', '?', '?', '?']
['?', '?', '?', '?']
['?', '?', '?', '?']

Move: d

['.', 'AS', '?', '?']
```

---

## 🧪 Debug Mode

At the end of the game, the full grid is revealed:

```
['A', 'S', 'WB', 'S']
['', 'B', 'PS', 'B']
...
```

---

## 🛠️ Future Improvements

* 🏹 Arrow shooting mechanic (kill Wumpus)
* 🧠 AI Agent (logical reasoning)
* 📊 Scoring system
* 🎨 GUI version (Pygame)
* 🧭 Pathfinding visualization

---

## 📚 Concepts Used

* Object-Oriented Programming (OOP)
* Grid-based simulations
* AI Environment Modeling
* Percept-based decision systems

---

## 🤝 Contribution

Feel free to fork the repo and improve the project.
Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Abdul Muneeb Asif**
Roku Developer | Python Enthusiast | Final Year CS Student

---

⭐ If you like this project, consider giving it a star!
