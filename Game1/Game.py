import random

def guess_the_number():
       # Generate a random number between 1 and 100
       number_to_guess = random.randint(1, 100)
       attempts = 0
       max_attempts = 10

       print("Welcome to 'Guess the Number'!")
       print("I have selected a number between 1 and 100.")
       print(f"You have {max_attempts} attempts to guess it.")

       while attempts < max_attempts:
           try:
               # Get user input
               guess = int(input("Enter your guess: "))
               attempts += 1

               # Check the guess
               if guess < number_to_guess:
                   print("Too low! Try again.")
               elif guess > number_to_guess:
                   print("Too high! Try again.")
               else:
                   print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                   break
           except ValueError:
               print("Please enter a valid integer.")

       if attempts == max_attempts:
           print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

   # Run the game
if __name__ == "__main__":
       guess_the_number()
   