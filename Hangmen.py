import os

game = True
lives = 5
print("- Hangmen -")
print("")
print("Welcome to the Hangmen game!")
print("This is a game for 2 players, hence the name.")
print("")

print("Player 1, enter the word for the game:")
word = input().lower()
print("")

print("Your word has been entered successfully.")
letters = list(word)
print("")
print("Your word has been saved as:", word)
print("")

vector = letters
empty_vector = [""] * len(letters)
repeated_letters = [""] * len(letters)

print("Pass the turn to Player 2 who will guess the word.")
print("")
print("Press ENTER when you are ready.")
input()

clear = lambda: os.system('cls')
clear()

print("")
print("Welcome, Player 2!")
print("")

while game and lives > 0 and len(letters) > 0:

    print("The current state of the word is:")
    print(empty_vector)
    print("")
    
    print("Player 2, what would you like to do? Guess the word or a letter?")
    print("A) Guess the word.")
    print("B) Guess a letter.")
    choice = input().lower()
    
    if choice == "a":
        print("")
        print("Enter your word guess:")
        guessed_word = input().lower()

        if guessed_word == word:
            print("")
            print("You guessed the word correctly!")
            print("Congratulations! And tell Player 1 they are too predictable, they should try harder next time.")
            game = False
          
        else:
            print("")
            print("Oops! That was not the correct word. You've lost a life.")
            print("")
            lives -= 1
            print("Remaining lives:", lives)
            print("")

          
    elif choice == "b":
        print("")
        print("Enter your letter guess:")
        guessed_letter = input().lower()
        print("")
        
        if guessed_letter in repeated_letters:
            print("You already guessed this letter before, and it is in the word.")
            print("")
            print("Remaining lives:", lives)
            print("")
            
        elif guessed_letter in letters:
            print("The letter is in the word.")
            print("")
            print("Remaining lives:", lives)
            print("")
            letters = [s.replace(guessed_letter, '') for s in letters]
            letters = [s for s in letters if s]
            
            for idx, char in enumerate(vector):
                if char == guessed_letter:
                    empty_vector[idx] = guessed_letter
                    
            repeated_letters.append(guessed_letter)
            
        else:
            print("Oops! That letter is not in the word. You've lost a life.")
            print("")
            lives -= 1
            print("Remaining lives:", lives)
            print("")
    
    else:
        print("The command entered was not recognized. Please try again.")
        print("")

if len(letters) == 0 or not game:
    print("")
    print("------------------------------------------------------------")
    print("")
    print("The word was:", word)
    print("")
    print("You won, congratulations! :)")
    print("")
    print("Press ENTER to close this window.")
    input()
elif lives == 0:
    print("")
    print("------------------------------------------------------------")
    print("")
    print("Sorry, you've lost. Better luck next time :(")
    print("- Game Over -")
    print("")
    print("Press ENTER to close this window.")
    input()
