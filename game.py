import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def display_aesthetic_blob(result):
    blobs = {
        "It's a tie!": "🔵🟢🟡............ It's a tie..........! 🟡🟢🔵",
        "You win!": "🌟✨🎉 .........You win!......... 🎉✨🌟",
        "Computer wins!": "💻🤖 ..........Computer wins!........🤖💻"
    }
    print(blobs[result])

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        display_aesthetic_blob(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
