import random
choices = 'rps'
print("Welcome to Rock Paper Scissors!")

while True:
    print("Enter \'r\' for Rock, \'p\' for Paper, \'s\' for Scissors or \'?\' to commands.")
    ans = input("Enter your choice: ")
    ans = ans.lower()

    if ans == 'q':
        print("Thanks for playing!")
        break
    
    if ans == '?':
        print("Commands:")
        print("r - Rock")
        print("p - Paper")
        print("s - Scissors")
        print("q - Quit")
        print("w - Print choices string")
        print("reset - Reset learning")
        print("*************************************************")
        continue


    if ans == 'w':
        print("Current string of choices is")
        print(choices)
        print("*************************************************")
        continue

    if ans == 'reset':
        choices = 'rps'
        print("Choices reset.")
        print("*************************************************")
        continue

    #check if the input is valid
    if ans not in choices:
     print("Invalid choice. Enter '?' for help.")
     continue
    else:
        #print(choices) add this if you want to see the choices
        if ans == "r":
            print("You chose: Rock")
        elif ans == "p":
            print("You chose: Paper")
        elif ans == "s":
            print("You chose: Scissors")
        
        choices+=ans
        comp = random.choice(choices)
        if comp == "r":
            print("Computer chose: Paper")
        elif comp == "p":
            print("Computer chose: Scissors")
        elif comp == "s":
            print("Computer chose: Rock")
        else:
            print("*************************************************")
            continue

        if ans == comp:
            print("You lost!")
        elif ans == "r" and comp == "p":
            print("You won!")
        elif ans == "p" and comp == "s":
            print("You won!")
        elif ans == "s" and comp == "r":
            print("You won!")
        else:
            print("its tie")
        print("*************************************************")
