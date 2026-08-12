
# 🎮 Hangman Game Challenge

## 📋 Objective

Build the classic Hangman word-guessing game using Python. You'll practice string manipulation, loops, conditionals, and random selection as you create an interactive game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### Task 1: Create the Game Structure

**Description:**
Set up the basic structure of your Hangman game by initializing the necessary variables and functions to run the game loop.

**Requirements:**
- Create a list of words that can be randomly selected for the game
- Initialize variables to track the current word, guessed letters, remaining attempts, and game status
- Set up the main game loop that continues until the game is won or lost
- Implement a function to display the current progress (_ _ _ format for unrevealed letters)

**Example:**
```
Secret word: PYTHON
Current progress: _ _ _ _ _ _
Guesses remaining: 6
```

### Task 2: Implement Letter Guessing

**Description:**
Add functionality for players to guess letters and update the game state based on their guesses.

**Requirements:**
- Accept letter input from the player
- Check if the letter is in the secret word
- Update the word progress when letters are guessed correctly
- Track incorrect guesses and decrease remaining attempts
- Prevent duplicate guesses and provide feedback

### Task 3: Handle Win and Lose Conditions

**Description:**
Complete the game by implementing logic to detect when the player has won or lost and display appropriate messages.

**Requirements:**
- Display a win message when the player guesses all letters before running out of attempts
- Display a lose message when the player exhausts all attempts
- Show the secret word in either case
- Prompt the player if they want to play again
