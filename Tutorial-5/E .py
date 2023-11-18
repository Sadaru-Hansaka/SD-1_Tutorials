
from random_word import RandomWords

def play_guess_the_word(secret_word):
    while True:
        turns = 6
        guesses = ""
        
        print("Let's play Guess the Word")
        print(f"You have {turns} turns and the word has {len(secret_word)} letters.\nGuess the word!")
        print("_ " * len(secret_word))
        
        while turns > 0:
            guess = input("Guess a letter: ").lower()  # Convert guess to lowercase
            
            # Take only the first character if the user inputs a word
            guess = guess[0] if len(guess) > 0 else guess
            
            guesses += guess
            
            found = False
            for letter in secret_word:
                if letter in guesses:
                    print('', letter, '', end='')
                else:
                    print(' _ ', end='')
                    found = True
            
            print()
            
            if found:
                turns -= 1
            
            if all(letter in guesses for letter in secret_word):
                print("You've guessed the word! Well done!")
                break
        
        if turns == 0:
            print("Sorry, you're out of turns. The word was:", secret_word)
    
        choice=input("\nWould you like to play again?(y/n) : ")
        if choice=="n":
            break
        elif choice=="y":
            continue
        else:
            break

words = RandomWords()
secret_word = words.get_random_word()

play_guess_the_word(secret_word)
