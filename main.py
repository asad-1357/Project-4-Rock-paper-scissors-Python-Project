import random

def play():
    try:
        participant = input("Enter your choice: 'r' for rock, 'p' for paper, 's' for scissors:\t").lower()

        if participant not in ['r', 'p', 's']:
            return "Invalid input! Please enter 'r', 'p', or 's'."

        computer = random.choice(['r', 's', 'p'])
        print(f"Computer chose: {computer}")

        if participant == computer:
            return "It's a Tie!"
        if is_win(participant, computer):
            return "You won!"
        return "ohh ! You lost!"

    except KeyboardInterrupt:
        return "\nGame interrupted by user."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def is_win(player, opponent):        
    if(player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
      return True

print(play())
