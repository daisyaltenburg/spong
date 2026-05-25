# 🕹️ Spong & Breakout

A small Python game project using **pygame**.
This project started with a Pong-style game called **Spong**, then expanded into a simple **Breakout** game.

---

## 🎮 Games in This Project

### 🏓 Spong

Spong is a two-player Pong-style game.

Features:

* Two paddles
* Moving ball
* Wall bouncing
* Paddle collision
* Score tracking
* Custom colours
* Keyboard controls

Controls:

| Player       | Keys                      |
| ------------ | ------------------------- |
| Left paddle  | `W` / `S`                 |
| Right paddle | `Up Arrow` / `Down Arrow` |
| Quit         | `Esc`                     |

Run it with:

```bash
python pong.py
```

---

### 🧱 Breakout

Breakout is a paddle-and-brick game based on the same ideas as Pong.

Features:

* One paddle
* Bouncing ball
* Brick grid
* Bricks disappear when hit
* Score counter
* Lives counter
* Win and game-over conditions

Controls:

| Action     | Key           |
| ---------- | ------------- |
| Move left  | `Left Arrow`  |
| Move right | `Right Arrow` |
| Quit       | `Esc`         |

Run it with:

```bash
python breakout.py
```

---

## 🐍 Python Setup

This project uses Python and pygame.

The environment was created with:

```bash
python3 -m venv .venv --system-site-packages
```

Activate the environment with:

```bash
source .venv/bin/activate
```

Run a game with:

```bash
python pong.py
```

or:

```bash
python breakout.py
```

---

## 📦 Requirements

This project needs:

* Python 3
* pygame

On Ubuntu, pygame was installed with:

```bash
sudo apt install python3-pygame
```

The virtual environment was created using `--system-site-packages` so it can use the Ubuntu-installed pygame package.

---

## 🧠 What I Learned

During this project, I learned how to:

* Create Python files
* Run Python programs from the terminal
* Use a Python virtual environment
* Install and use pygame
* Draw shapes on the screen
* Move objects with keyboard input
* Detect collisions
* Keep score
* Use Git to save changes
* Push code to GitHub using SSH

---

## 🛠️ Git Commands Used

Some Git commands used in this project:

```bash
git status
git add .
git commit -am "first files"
git push
```

---

## 🌈 Custom Changes

Things changed while building the game:

* Renamed the game window to **Spong**
* Changed paddle colours
* Changed the background colour
* Created a pygame environment
* Added the project to GitHub
* Created an SSH key called **Daisy's Key**

---

## 🚀 Future Ideas

Possible improvements:

* Add sound effects 🔊
* Add a start screen 🎬
* Add a pause button ⏸️
* Add difficulty levels ⭐
* Add better colours and animations 🌈
* Add a high-score system 🏆
* Add single-player AI for Spong 🤖
* Add more brick patterns for Breakout 🧱

---

## 📁 Project Files

```text
spong/
├── pong.py
├── breakout.py
├── README.md
└── .venv/
```

The `.venv` folder is the Python environment and usually should not be uploaded to GitHub.

---

## 📝 Notes

This project is part of learning Python, pygame, Git, GitHub, SSH keys, and basic game development.

The goal is to keep improving the games step by step while tracking progress in GitHub.

---

## ✨ Project Status

Current status: **Working and improving** 🚧
