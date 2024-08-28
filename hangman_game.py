import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    
    word_completion = ['_'] * len(word)
    assumed = False
    assumed_letters = []
    assumed_words = []
    lives = 6
    print("Let's start Hangman Game!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not assumed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in assumed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                assumed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                assumed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if ['_'] not in word_completion:
                    assumed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in assumed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                lives -= 1
                assumed_words.append(guess)
            else:
                assumed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
    if assumed:
        print("Congratulations!, You win!")
    else:
        print("Sorry, you ran out of lives. The actual word was " + word + ". Try Again!")


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
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
