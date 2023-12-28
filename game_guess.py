import random

def get_guest():
    return list(input("What is your guess?"))

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clue(code_generate, code_guess):
    if (code_guess == code_generate):
        return "CODE CRACKED!"
    
    clues = []

    for ind, num in enumerate(code_guess):
        if num == code_generate[ind]:
            clues.append("MATCH")
        elif num in code_generate:
            clues.append("CLOSE")

    if clues == []:
        return ['NOPE']
    else:
         return clues
    
print("Welcome to the CODE BREAKER game!")

secret_code = generate_code()
clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guest()
    clue_report = generate_clue(guess, secret_code)

    print("Guess result is:")

    for clue in clue_report:
        print(clue)
