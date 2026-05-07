import random
from timeit import default_timer

LINE = "-" * 40

def main():
    game_counter = 0
    Game_stats = []    
    
    GAMING = True
    while GAMING:
        timer_start = default_timer()
        
        # function that converts seconds into minutes and convers it into mm:ss format
        def format_time(total_seconds):
            minutes = int(total_seconds // 60)
            seconds = int(total_seconds % 60)
            return f"{minutes:02}:{seconds:02}"
        
        # function below generates non-repeating 4 digits in a list
        # then joins the number into a one 4 digit number (int)
        def generate_number():
            number = random.sample(range(0, 9), 4)
            while number[0] == 0:
                number = random.sample(range(0, 9), 4)
            str_number = map(str, number)
            secret_num = "".join(str_number)
            return secret_num
        
        #This function breaks the input into a list and returns it
        def get_digit(num):
            return list(str(num))
        
        # This function checks duplicity of a number, returns True if there is NOT a duplicate
        # It is used for the user input, the generate_number() function handles the generated number duplicity already
        def duplicity_check(number):
            number_list = get_digit(number)
            number_set = set(number_list)
            if len(number_list) == len(number_set):
                return True
        
        hidden_num = generate_number()
               
        #This function counts bulls and cows
        def number_of_bull_cow(num, guess):
            bull_cow = [0,0]
            guess_check = get_digit(guess)
            hidden_check = get_digit(hidden_num)
            for i, j in zip(guess_check, hidden_check):
                if i in hidden_check:
                    if i == j:
                        bull_cow[0] += 1
                    else:
                        bull_cow[1] += 1
            return bull_cow
        
        print("Hi there!")
        print(LINE)
        print("I've generated a random 4 digit number for you.")
        print("Let's play a bulls and cows game.")
        print(LINE)
        guessing = True
        num_guesses = 0
        
        while guessing:    
            guess = input("Enter a number:")
            if guess == "exit":
                print("Terminating the program")
                guessing = False
                GAMING = False
            if len(str(guess)) != 4:
                print("Guessing number has 4 digits, try again.")
                print(LINE)
                continue
            if not guess.isdigit():
                print("Please input a valid 4 digit number.")
                print(LINE)
                continue
            if str(guess[0]) == "0":
                print("Hidden number never begins with 0. Try again.")
                print(LINE)
                continue
            if not duplicity_check(guess):
                print("Hidden number does not contain any duplicates. Try again")
                print(LINE)
                continue
                
            num_guesses += 1
            bull_cow = number_of_bull_cow(hidden_num, guess)        
            
            print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
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
                Game_stats.append(current_game)
                print(f"Game history:")
                for game in Game_stats:
                    print(f"Game {game['Game']} : {game['Guesses']} guesses and time taken was {game['Time taken']}")
                break        
        
        while guessing:
            question = input("Would you like to play again? (Y/n):")
            if question == "Y":
                break
            if question == "n":
                print("Very well, see you next time!")
                GAMING = False
                break
            else:
                print("Please input correct letter")
                continue
    
if __name__ == "__main__":
    main()   
    