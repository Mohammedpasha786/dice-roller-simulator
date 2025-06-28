#!/usr/bin/env python3
"""
🎲 Dice Roller Simulator
A fun interactive dice rolling program with ASCII animation and suspense!

Author: Python Developer
Version: 1.0
"""

import random
import time
import os
import sys
from typing import Dict

class DiceRoller:
    """A class to simulate dice rolling with visual effects."""
    
    def __init__(self):
        """Initialize the dice roller with ASCII art patterns."""
        self.dice_faces = {
            1: [
                "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"
            ],
            2: [
                "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"
            ],
            3: [
                "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"
            ],
            4: [
                "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"
            ],
            5: [
                "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"
            ],
            6: [
                "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘"
            ]
        }
        
        # Rolling animation frames
        self.rolling_frames = [
            "🎲",
            "🔄",
            "⚡",
            "✨",
            "🎯"
        ]
        
        # Statistics tracking
        self.roll_history = []
        self.roll_count = 0

    def clear_screen(self):
        """Clear the terminal screen for better visual experience."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        """Display the welcome banner."""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                        🎲 DICE ROLLER 🎲                     ║
║                                                              ║
║        Welcome to the Ultimate Six-Sided Die Simulator!     ║
║                                                              ║
║        Press ENTER to roll the dice | Type 'quit' to exit   ║
║        Type 'stats' to see your rolling statistics          ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def countdown(self, seconds: int = 3):
        """Display an exciting countdown before the roll."""
        print("\n🎯 Get ready to roll...")
        time.sleep(0.5)
        
        for i in range(seconds, 0, -1):
            print(f"\r⏰ Rolling in {i}...", end="", flush=True)
            time.sleep(0.8)
        
        print("\r🚀 Rolling NOW!     ", flush=True)
        time.sleep(0.3)

    def rolling_animation(self, duration: float = 2.0):
        """Display a rolling animation to build suspense."""
        print("\n" + "="*50)
        print("🎲 ROLLING THE DICE... 🎲".center(50))
        print("="*50)
        
        end_time = time.time() + duration
        frame_index = 0
        
        while time.time() < end_time:
            # Create rolling effect with random symbols
            frame = self.rolling_frames[frame_index % len(self.rolling_frames)]
            random_dots = "".join(["●" if random.random() > 0.5 else "○" for _ in range(6)])
            
            print(f"\r    {frame} [{random_dots}] {frame}    ", end="", flush=True)
            
            frame_index += 1
            time.sleep(0.15)
        
        print("\r" + " " * 30, end="", flush=True)  # Clear the line

    def display_dice(self, number: int):
        """Display the dice face with the rolled number."""
        print("\n" + "🎊 RESULT 🎊".center(50))
        print("="*50)
        
        # Display the ASCII dice
        for line in self.dice_faces[number]:
            print(f"    {line}")
        
        print(f"\n    🎯 You rolled a {number}! 🎯".center(50))
        print("="*50)

    def celebrate_result(self, number: int):
        """Add celebration effects based on the rolled number."""
        celebrations = {
            1: "🔥 Unlucky start! Try again! 🔥",
            2: "💫 Not bad! Keep rolling! 💫",
            3: "⭐ Getting warmer! ⭐",
            4: "🌟 Good roll! 🌟",
            5: "🎉 Excellent! Almost perfect! 🎉",
            6: "🏆 JACKPOT! Maximum roll! 🏆"
        }
        
        print(f"\n    {celebrations[number]}")
        
        # Special effects for high rolls
        if number >= 5:
            print("    ✨ " + "🎉" * (number - 2) + " ✨")

    def update_statistics(self, roll: int):
        """Update rolling statistics."""
        self.roll_history.append(roll)
        self.roll_count += 1

    def display_statistics(self):
        """Display comprehensive rolling statistics."""
        if not self.roll_history:
            print("\n📊 No rolls yet! Start rolling to see statistics.")
            return
        
        print("\n" + "="*60)
        print("📊 ROLLING STATISTICS 📊".center(60))
        print("="*60)
        
        # Basic stats
        total_rolls = len(self.roll_history)
        average = sum(self.roll_history) / total_rolls
        highest = max(self.roll_history)
        lowest = min(self.roll_history)
        
        print(f"🎲 Total Rolls: {total_rolls}")
        print(f"📈 Average Roll: {average:.2f}")
        print(f"🏆 Highest Roll: {highest}")
        print(f"📉 Lowest Roll: {lowest}")
        
        # Frequency distribution
        print(f"\n🎯 Roll Distribution:")
        for i in range(1, 7):
            count = self.roll_history.count(i)
            percentage = (count / total_rolls) * 100 if total_rolls > 0 else 0
            bar = "█" * int(percentage / 5) + "░" * (20 - int(percentage / 5))
            print(f"  {i}: [{bar}] {count:2d} ({percentage:5.1f}%)")
        
        # Recent rolls
        print(f"\n📋 Last 10 Rolls: {self.roll_history[-10:]}")
        print("="*60)

    def roll_dice(self) -> int:
        """Roll the dice and return the result."""
        return random.randint(1, 6)

    def get_user_input(self) -> str:
        """Get user input with a nice prompt."""
        return input("\n🎮 Press ENTER to roll, 'stats' for statistics, or 'quit' to exit: ").strip().lower()

    def run(self):
        """Main game loop."""
        self.clear_screen()
        self.print_banner()
        
        print("🎊 Welcome! Let's start rolling some dice! 🎊")
        
        while True:
            try:
                user_input = self.get_user_input()
                
                if user_input == 'quit' or user_input == 'q':
                    print("\n👋 Thanks for playing! Goodbye!")
                    if self.roll_history:
                        print(f"🎲 You rolled {len(self.roll_history)} times with an average of {sum(self.roll_history)/len(self.roll_history):.2f}")
                    break
                
                elif user_input == 'stats' or user_input == 's':
                    self.display_statistics()
                    continue
                
                elif user_input == '' or user_input == 'roll' or user_input == 'r':
                    # Start the rolling sequence
                    self.countdown()
                    self.rolling_animation()
                    
                    # Roll the dice
                    result = self.roll_dice()
                    
                    # Display results
                    self.display_dice(result)
                    self.celebrate_result(result)
                    
                    # Update statistics
                    self.update_statistics(result)
                    
                    print(f"\n📊 Roll #{self.roll_count} complete!")
                
                else:
                    print("❓ Invalid input! Press ENTER to roll, 'stats' for statistics, or 'quit' to exit.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted! Thanks for playing!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                print("🔄 Don't worry, let's keep rolling!")

def main():
    """Main function to run the dice roller."""
    print("🎲 Initializing Dice Roller...")
    time.sleep(1)
    
    dice_game = DiceRoller()
    dice_game.run()

if __name__ == "__main__":
    main()
