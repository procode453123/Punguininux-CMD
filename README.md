# Punguininux - Command Line Utility and Entertainment Suite

Welcome to **Punguininux**, a versatile command-line tool combining system management, file operations, mini-games, drawing utilities, and more. Designed for fun and functionality, this software offers a wide array of features accessible directly from your terminal.

---

## Features

- **System Commands & File Management**
  - Navigate directories (`cd`, `pwd`)
  - Create/delete folders (`mkdir`, `rm`)
  - List files (`ls`, `dir`, `tree`)
  - Read/write files (`cat`, `touch`)
  - Rename files (`mv`)
  - Execute programs (`start`)
  - Clear screen (`clear`, `cls`)

- **Network & System Utilities**
  - Network scanning with `nmap` (`scan`)
  - Display system info (`system`, `sys`)
  - Show current time (`time`, `temps`)
  - Open web browser (`internet`, `web`)

- **Entertainment & Creative Tools**
  - Play Hangman game (`game`, `jeu`)
  - Draw shapes (`dessin`)
  - Interactive painting (`paint`)
  - Display help and version info (`help`, `version`)
  - Show credits and creator info
  
- **Additional Features**
  - Execute calculations (`calc`)
  - Launch executables (`start <exe>`)
  - Navigate through menus
  - Network scanning (requires `nmap` installed)

---

## Requirements

- Python 3.x
- Optional: [nmap](https://nmap.org/) for network scanning
- Windows or Unix-based OS

---

## Installation

1. Download the `punguininux.py` script.
2. Ensure Python 3 is installed on your system.
3. (Optional) Install `nmap` for network scanning:
   - Windows: Download from [nmap.org](https://nmap.org/download.html)
   - Linux: Use package manager (e.g., `sudo apt install nmap`)

4. Run the script via command line:
```bash
python punguininux.py
```

---

## Usage

Once launched, you'll see a prompt indicating your current directory. Enter commands as described in the help menu.

### Example Commands
- `help` or `?` — Display available commands
- `ls` or `dir` — List files
- `cd <directory>` — Change directory
- `cat <file>` — Read a file
- `mkdir <folder_name>` — Create a new folder
- `game` — Play Hangman
- `dessin` — Draw shapes
- `paint` — Draw interactively
- `scan` — Perform network scan
- `internet` — Open Google in browser
- `time` — Show current time
- `exit` — Quit the program

---

## Notes

- Some features require additional setup (like `nmap`).
- The drawing functions use the `turtle` module and open a separate window.
- The program handles basic errors gracefully, providing feedback.

---

## License

This project is provided as-is. Use responsibly, especially when executing system commands and network scans.

---

## Contact

For support or feedback, contact: [merlincaelan@gmail.com](mailto:merlincaelan@gmail.com)

---

## Happy Commanding! 🚀
