import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper() 


def play(word):
    word_complete = ['_'] * len(word)
    assumed = False
    assumed_letters = []
    assumed_words = []
    lives = 6
    print("Let's start the Hangman Game!")
    print(display_hangman(lives))
    print(" ".join(word_complete))
    print("\n")
    
    while not assumed and lives > 0:
        guess = input("Please guess a letter or word: ").strip().upper()  # Corrected 'up()' to 'upper()'
        
        if len(guess) == 1 and guess.isalpha():
            if guess in assumed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                lives -= 1
                assumed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word!")
                assumed_letters.append(guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_complete[index] = guess
                if '_' not in word_complete:
                    assumed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in assumed_words:
                print(f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the word.")
                lives -= 1
                assumed_words.append(guess)
            else:
                assumed = True
                word_complete = list(word)
        else:
            print("Not a valid guess.")
        
        print(display_hangman(lives))
        print(" ".join(word_complete))
        print("\n")
    
    if assumed:
        print("Congratulations! You win!")
    else:
        print(f"Sorry, you ran out of lives. The actual word was '{word}'. Try Again!")


def display_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[lives]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N): ").strip().upper() == "Y":
        word = get_word()
        play(word)
    if ('N'):
            print("Thanks for playing")    


if __name__ == "__main__":
    main()
