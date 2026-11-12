import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    
    print("\n--- New game started! ---")
    print("I have chosen a number between 1 and 100. Guess it!")

    attempt = 1
    while attempt <= max_attempts:
        remaining = max_attempts - attempt
        print(f"\nAttempt {attempt} of {max_attempts}")
        print(f"Remaining lives: {remaining}")
        
        user_input = input("Your guess: ")
        
        try:
            guess = int(user_input)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100. (Attempt not counted)")
                continue 
        except ValueError:
            print("Invalid input! Please enter numbers only. (Attempt not counted)")
            continue

        if guess == secret_number:
            print("\n🎉 Congratulations! You guessed the correct number.")
            
            if attempt == 1:
                rank = "Excellent"
            elif attempt == 2:
                rank = "Very Good"
            elif attempt == 3:
                rank = "Good"
            elif attempt == 4:
                rank = "Acceptable"
            else:
                rank = "Lucky Win!"
                
            print(f"Your rank: {rank}")
            return 
            
        difference = abs(guess - secret_number)
        
        if difference <= 5:
            guide = "Very close!"
        elif difference <= 15:
            guide = "Close, but still far!"
        else:
            guide = "Very far!"
            
        if guess > secret_number:
            print(f"{guide} The secret number is smaller. (Enter a smaller number)")
        else:
            print(f"{guide} The secret number is larger. (Enter a larger number)")
            
        attempt += 1

    print("\nUnfortunately, you ran out of attempts! 😔")
    print(f"The secret number was {secret_number}.")

while True:
    play_game()
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break
