# dice-roller-simulator
# 🎲 Dice Roller Simulator

A fun and interactive Python program that simulates rolling a standard six-sided die with ASCII animation, countdown effects, and comprehensive statistics tracking!

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 🎯 Features

### Core Functionality
- **🎲 Realistic Dice Rolling**: Generate random numbers 1-6
- **⏰ Suspenseful Countdown**: 3-second countdown before each roll
- **🎬 ASCII Animation**: Rolling animation with visual effects
- **🎨 Beautiful Dice Display**: ASCII art representation of dice faces
- **🎊 Celebration Effects**: Different celebrations based on roll results

### Enhanced Experience
- **📊 Statistics Tracking**: Comprehensive roll statistics and history
- **🎯 Distribution Analysis**: Visual frequency charts for each number
- **🏆 Performance Metrics**: Average, highest, lowest rolls
- **📋 Roll History**: Track your last 10 rolls
- **🎮 Interactive Interface**: Easy-to-use command system

### Technical Features
- **🖥️ Cross-Platform**: Works on Windows, macOS, and Linux
- **🎨 Visual Effects**: Clear screen, colorful output, smooth animations
- **⚡ Performance**: Optimized for smooth user experience
- **🛡️ Error Handling**: Robust error handling and user input validation

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- Terminal/Command Prompt

### Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/dice-roller.git
cd dice-roller
```

2. **Run the program:**
```bash
python dice_roller.py
```

3. **Start rolling:**
   - Press **ENTER** to roll the dice
   - Type **'stats'** to view statistics
   - Type **'quit'** to exit

## 🎮 How to Use

### Basic Commands
- **ENTER** or **'roll'** - Roll the dice
- **'stats'** or **'s'** - Display statistics
- **'quit'** or **'q'** - Exit the program
- **Ctrl+C** - Emergency exit

### Example Session
```
🎲 DICE ROLLER 🎲
Welcome to the Ultimate Six-Sided Die Simulator!

🎮 Press ENTER to roll, 'stats' for statistics, or 'quit' to exit: 

🎯 Get ready to roll...
⏰ Rolling in 3...
⏰ Rolling in 2...
⏰ Rolling in 1...
🚀 Rolling NOW!

🎲 ROLLING THE DICE... 🎲
==================================================
    ✨ [●○●○●○] ✨    

🎊 RESULT 🎊
==================================================
    ┌─────────┐
    │  ●   ●  │
    │    ●    │
    │  ●   ●  │
    └─────────┘

    🎯 You rolled a 5! 🎯
==================================================

    🎉 Excellent! Almost perfect! 🎉
    ✨ 🎉🎉🎉 ✨

📊 Roll #1 complete!
```

## 📊 Statistics Features

The program tracks comprehensive statistics including:

- **Total Rolls**: Number of dice rolls performed
- **Average Roll**: Mean value of all rolls
- **Highest/Lowest**: Best and worst rolls
- **Distribution Chart**: Visual representation of frequency
- **Recent History**: Last 10 rolls for quick reference

### Sample Statistics Output
```
📊 ROLLING STATISTICS 📊
============================================================
🎲 Total Rolls: 25
📈 Average Roll: 3.52
🏆 Highest Roll: 6
📉 Lowest Roll: 1

🎯 Roll Distribution:
  1: [████░░░░░░░░░░░░░░░░] 4 (16.0%)
  2: [██░░░░░░░░░░░░░░░░░░] 2 ( 8.0%)
  3: [████████░░░░░░░░░░░░] 8 (32.0%)
  4: [██████░░░░░░░░░░░░░░] 6 (24.0%)
  5: [██░░░░░░░░░░░░░░░░░░] 2 ( 8.0%)
  6: [██████░░░░░░░░░░░░░░] 3 (12.0%)

📋 Last 10 Rolls: [3, 4, 1, 6, 3, 4, 2, 3, 5, 4]
============================================================
```

## 🎨 Visual Features

### ASCII Dice Faces
Each number is represented with beautiful ASCII art:

```
1:          2:          3:
┌─────────┐ ┌─────────┐ ┌─────────┐
│         │ │  ●      │ │  ●      │
│    ●    │ │         │ │    ●    │
│         │ │      ●  │ │      ●  │
└─────────┘ └─────────┘ └─────────┘

4:          5:          6:
┌─────────┐ ┌─────────┐ ┌─────────┐
│  ●   ●  │ │  ●   ●  │ │  ●   ●  │
│         │ │    ●    │ │  ●   ●  │
│  ●   ●  │ │  ●   ●  │ │  ●   ●  │
└─────────┘ └─────────┘ └─────────┘
```

### Animation Effects
- **Rolling Animation**: Dynamic symbols and changing patterns
- **Countdown Timer**: Build suspense with 3-2-1 countdown
- **Celebration Effects**: Special animations for high rolls
- **Progress Bars**: Visual statistics representation

## 🔧 Technical Implementation

### Code Structure
```python
class DiceRoller:
    - __init__(): Initialize dice faces and animation frames
    - roll_dice(): Core random number generation
    - countdown(): Pre-roll countdown animation
    - rolling_animation(): Visual rolling effects
    - display_dice(): ASCII art dice display
    - celebrate_result(): Post-roll celebrations
    - update_statistics(): Track roll history
    - display_statistics(): Comprehensive stats display
    - run(): Main game loop
```

### Key Features
- **Object-Oriented Design**: Clean, maintainable code structure
- **Type Hints**: Enhanced code readability and IDE support
- **Error Handling**: Robust exception handling for user experience
- **Cross-Platform**: Compatible with Windows, macOS, and Linux
- **Memory Efficient**: Optimized for performance and resource usage

## 🎲 Dice Rolling Logic

### Random Number Generation
```python
def roll_dice(self) -> int:
    """Roll the dice and return the result."""
    return random.randint(1, 6)
```

### Fair Probability
- Each number (1-6) has equal probability: **16.67%**
- Uses Python's `random.randint()` for cryptographically secure randomness
- No bias or patterns in number generation

## 🎯 Customization Options

### Easy Modifications
1. **Change Animation Speed**: Modify `time.sleep()` values
2. **Add More Dice Faces**: Extend the `dice_faces` dictionary
3. **Custom Celebrations**: Modify the `celebrations` dictionary
4. **Different Colors**: Add ANSI color codes for terminal colors
5. **Sound Effects**: Integrate with `playsound` library

### Example Customizations
```python
# Add colors (works on most terminals)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
ENDC = '\033[0m'

# Custom celebration for rolling 6
if number == 6:
    print(f"{YELLOW}🏆 JACKPOT! Maximum roll! 🏆{ENDC}")
```

## 📋 Requirements

### System Requirements
- **Python**: 3.6 or higher
- **OS**: Windows, macOS, or Linux
- **Terminal**: Any terminal with UTF-8 support
- **Memory**: < 10 MB
- **Storage**: < 1 MB

### Python Modules Used
- `random` - Random number generation
- `time` - Timing and delays
- `os` - Operating system interface
- `sys` - System-specific parameters
- `typing` - Type hints support

All modules are part of Python's standard library - no external dependencies!

## 🛠️ Development & Testing

### Running Tests
```bash
# Basic functionality test
python dice_roller.py

# Test with different Python versions
python3.6 dice_roller.py
python3.7 dice_roller.py
python3.8 dice_roller.py
```

### Code Quality
- **PEP 8 Compliant**: Follows Python style guidelines
- **Type Hints**: Enhanced code documentation
- **Docstrings**: Comprehensive function documentation
- **Error Handling**: Robust exception management

## 📸 Screenshots & Demo

### Terminal Output Example
```
╔══════════════════════════════════════════════════════════════╗
║                        🎲 DICE ROLLER 🎲                     ║
║                                                              ║
║        Welcome to the Ultimate Six-Sided Die Simulator!     ║
║                                                              ║
║        Press ENTER to roll the dice | Type 'quit' to exit   ║
║        Type 'stats' to see your rolling statistics          ║
╚══════════════════════════════════════════════════════════════╝

🎊 Welcome! Let's start rolling some dice! 🎊

🎮 Press ENTER to roll, 'stats' for statistics, or 'quit' to exit: 

🎯 Get ready to roll...
🚀 Rolling NOW!

==================================================
🎲 ROLLING THE DICE... 🎲
==================================================

🎊 RESULT 🎊
==================================================
    ┌─────────┐
    │  ●   ●  │
    │  ●   ●  │
    │  ●   ●  │
    └─────────┘

    🎯 You rolled a 6! 🎯
==================================================

    🏆 JACKPOT! Maximum roll! 🏆
    ✨ 🎉🎉🎉🎉 ✨

📊 Roll #1 complete!
```

## 🚀 Deployment & Distribution

### Creating Executable
```bash
# Using PyInstaller
pip install pyinstaller
pyinstaller --onefile dice_roller.py

# The executable will be in the 'dist' folder
```

### GitHub Repository Setup
1. Initialize repository: `git init`
2. Add files: `git add dice_roller.py README.md`
3. Commit: `git commit -m "Initial commit: Dice Roller Simulator"`
4. Push to GitHub: `git push origin main`

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Commit** your changes: `git commit -am 'Add feature'`
4. **Push** to the branch: `git push origin feature-name`
5. **Submit** a Pull Request

### Contribution Ideas
- Add sound effects
- Implement multiple dice rolling
- Create GUI version with tkinter
- Add save/load statistics feature
- Implement different dice types (d4, d8, d10, d20)

