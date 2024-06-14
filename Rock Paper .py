import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the user's and computer's choices and the result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    """Ask the user if they want to play another round."""
    while True:
        again = input("Do you want to play another round? (yes/no): ").lower()
        if again in ['yes', 'no']:
            return again == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """Main function to run the Rock, Paper, Scissors game."""
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        
        if not play_again():
            break
    
    print("\nThanks for playing! Final score:")
    print(f"You: {user_score} - Computer: {computer_score}")

if __name__ == "__main__":
    main()
