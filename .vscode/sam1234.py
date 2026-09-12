# Change this line to match your filename!
import sam123  

print("--- Multi-File Number Guessing Game ---")

# Use sam123 instead of game_logic
secret_number = sam123.generate_secret_number()
attempts = 0

while True:
    guess = int(input("Take a guess: "))
    attempts += 1
    
    # Use sam123 instead of game_logic
    result = sam123.check_guess(guess, secret_number)
    
    if result == "Too low":
        print("Too low! Try a higher number.")
    elif result == "Too high":
        print("Too high! Try a lower number.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
