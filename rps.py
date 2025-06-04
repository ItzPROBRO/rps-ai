import random
choices = 'rps'
print("Welcome to Rock Paper Scissors!")
while True:
    print("Enter \'r\' for Rock, \'p\' for Paper, \'s\' for Scissors")
    ans = input("Enter your choice: ")
    ans = ans.lower()
    #check if the input is valid
    if ans not in choices:
     print("Invalid choice. Please enter \'r\', \'p\', or \'s\'.")
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
