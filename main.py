
import random
from graphics import *



word_list = [

    # Easy Words
    "apple", "ball", "cat", "dog", "egg", "fish", "gate", "hat",
    "ice", "jar", "key", "lamp", "moon", "net", "owl", "pen",
    "queen", "rain", "sun", "tree", "van", "window", "zebra",

    # Animals
    "tiger", "lion", "elephant", "giraffe", "penguin", "dolphin",
    "shark", "rabbit", "monkey", "panda", "kangaroo", "wolf",
    "fox", "bear", "camel", "eagle", "falcon", "parrot",

    # Food
    "pizza", "burger", "sandwich", "spaghetti", "chocolate",
    "pancake", "cookie", "noodles", "watermelon", "banana",
    "strawberry", "pineapple", "popcorn", "cupcake",

    # Technology
    "computer", "keyboard", "internet", "python", "programming",
    "software", "hardware", "database", "monitor", "laptop",
    "algorithm", "robot", "network", "server", "cybersecurity",

    # Space
    "planet", "galaxy", "asteroid", "satellite", "astronaut",
    "meteor", "comet", "telescope", "universe", "spaceship",

    # Fantasy
    "dragon", "wizard", "castle", "knight", "sorcerer",
    "phoenix", "vampire", "treasure", "adventure", "mystery",

    # Countries & Places
    "canada", "brazil", "india", "france", "germany",
    "tokyo", "london", "paris", "mountain", "desert",
    "volcano", "ocean", "forest", "island",

    # School Subjects
    "mathematics", "science", "history", "geography",
    "chemistry", "physics", "biology", "literature",

    # Hard Words
    "xylophone", "awkward", "mnemonic", "quarantine",
    "pneumonia", "cryptography", "encyclopedia",
    "microprocessor", "transformation", "responsibility",

    # Gaming
    "minecraft", "fortnite", "roblox", "controller",
    "playstation", "xbox", "nintendo", "speedrun",

    # Random Fun
    "lightning", "thunder", "rainbow", "diamond",
    "fireworks", "hurricane", "invisible", "champion",
    "legendary", "powerful", "victory", "dangerous"
]




lives = 6
chosen_word = random.choice(word_list)

correct_letters = []
game_over = False


print(logo)


placeholder = ""

for letter in chosen_word:
    placeholder += "_ "

print(WHITE + "Word to guess: " + RESET + placeholder)


while not game_over:

    print(HANGMAN_STAGES[lives])

    guess = input(YELLOW + "\nGuess a letter: " + RESET).lower()

    
    if guess in correct_letters:
        print(MAGENTA + "You already guessed that letter!" + RESET)
        continue

    display = ""

    
    for letter in chosen_word:

        if letter == guess:
            display += letter + " "
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter + " "

        else:
            display += "_ "

    print("\n" + CYAN + display + RESET)

    
    if guess not in chosen_word:
        lives -= 1
        print(RED + f"\nWrong! Lives left: {lives}" + RESET)

        if lives == 0:
            game_over = True
            print(HANGMAN_STAGES[lives])
            print(lose_art)
            print(RED + f"The word was: {chosen_word}" + RESET)

    
    if "_" not in display:
        game_over = True
        print(win_art)

