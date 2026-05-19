import random

from timeit import default_timer

LINE = "-" * 40

def format_time(total_seconds: float) -> str:
    """Converts seconds into minutes, mm:ss format"""
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes:02}:{seconds:02}"


def generate_number():
    """Generates non-repeating 4 digits"""
    number = random.sample(range(0, 9), 4)
    while number[0] == 0:
        number = random.sample(range(0, 9), 4)
    str_number = map(str, number)
    secret_num = "".join(str_number)
    return secret_num


def get_digit(num: str) -> list[str]:
    """Breaks the input into a list and returns it"""
    return list(str(num))


def duplicity_check(number: str) -> bool:
    """Checking duplicity of a number"""
    number_list = get_digit(number)
    number_set = set(number_list)
    if len(number_list) == len(number_set):
        return True

     
def number_of_bull_cow(num: str, guess: str) -> list[int, int]:
    """Counting bulls and cows"""
    bull_cow = [0,0]
    guess_check = get_digit(guess)
    hidden_check = get_digit(num)
    for i, j in zip(guess_check, hidden_check):
        if i in hidden_check:
            if i == j:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow


def bull_or_bulls(incoming_guess: str) -> str:
    if incoming_guess[0] == 1:
        return "bull"
    else:
        return "bulls"


def cow_or_cows(incoming_guess: str) -> str:
    if incoming_guess[1] == 1:
        return "cow"
    else:
        return "cows"


def main():
    game_counter = 0
    gaming = True
    hidden_num = generate_number()
    game_stats = []
            
    while gaming:
        timer_start = default_timer()
        
        print("Hi there!")
        print(LINE)
        print("I've generated a random 4 digit number for you.")
        print("Let's play a bulls and cows game.")
        print(LINE)
        guessing = True
        num_guesses = 0
        
        while guessing:
            guess = input("Enter a number:")
            if guess.lower() == "exit":
                print("Terminating the program")
                guessing = False
                gaming = False
                break
            if len(str(guess)) != 4:
                print("Secret number has exactly 4 digits. Please input 4 digit number.")
                print(LINE)
                continue
            if not guess.isdigit():
                print("Only 4 digit number is a valid input. Please input 4 digit number.")
                print(LINE)
                continue
            if str(guess[0]) == "0":
                print('Hidden number never begins with a "0" digit. Please input another 4 digit number.')
                print(LINE)
                continue
            if not duplicity_check(guess):
                print("Hidden number does not contain any duplicate digits. Please input 4 digit number without any duplicate digits.")
                print(LINE)
                continue
                
            num_guesses += 1
            bull_cow = number_of_bull_cow(hidden_num, guess)                        
            
            print(f"{bull_cow[0]} {bull_or_bulls(bull_cow)}, {bull_cow[1]} {cow_or_cows(bull_cow)}")
            print(LINE)
            if bull_cow[0] == 4:
                timer_end = default_timer()
                time_delta = timer_end - timer_start
                time = format_time(time_delta)
                print(f"You guessed the number! It was {guess} and it took you {num_guesses} tries and took you {time} (mins:seconds)!")
                game_counter += 1
                current_game = {
                    "Game": game_counter,
                    "Guesses": num_guesses,
                    "Time taken": time
                }
                game_stats.append(current_game)
                print(f"Game history:")
                for game in game_stats:
                    print(f"Game {game['Game']} : {game['Guesses']} guesses and time taken was {game['Time taken']}")
                break
        
        while True:
            if not gaming:
                break
            question = input("Would you like to guess another number? (Y/n):")
            if question.lower() == "exit":
                gaming = False
                break
            if question.lower() == "y":
                hidden_num = generate_number()
                break
            if question.lower() == "n":
                print("Very well, see you next time!")
                gaming = False
                break
            else:
                print("Please input correct letter")
                continue
    
if __name__ == "__main__":
    main()