import random

max_number = input("Enter highest number: ")

available_numbers = []
npc_random_number: int

for x in range(1, int(max_number)+1):
    available_numbers.append(x)

npc_random_number = random.choice(available_numbers)

game_running = True

while game_running:
    user_guess = int(input("Your guess: "))
    if user_guess == npc_random_number:
        print("CORRECT! YOU WIN!")
        game_running = False
    elif user_guess > npc_random_number:
        print("Your guess is too strong, please guess a lower number.")
    elif user_guess < npc_random_number:
        print("Your guess is too weak, guess higher please!!!")
