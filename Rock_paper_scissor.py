import random
from tkinter import *

score = 0  

def playgame():
    def show():
        nonlocal root
        global score  #it is used to not define score variable in def function

        user_choice = choice.get()
        options = ["Rock", "Paper", "Scissor"]
        mychoice = random.choice(options)

        print(f"\nYou selected: {user_choice}")
        print("I selected:", mychoice)
        print("Result:", end=" ")

        win = 0
        if user_choice == mychoice:
            print("Tie")
        elif (user_choice == "Rock" and mychoice == "Scissor") or (user_choice == "Paper" and mychoice == "Rock") or (user_choice == "Scissor" and mychoice == "Paper"):
            print("Congrats, You win!")
            win = 1
        else:
            print("You lost\nTry next time!")

        score += win
        print("Your Score:", score)

        root.destroy() 
        
#It is time to design the choice option box for user
    root = Tk()
    root.geometry("220x180")
    root.title("Rock Paper Scissor")

    Label(root, text="Choose your option:").pack(pady=5)

    choice = StringVar(value="Stone")

    Radiobutton(root, text="Rock", variable=choice, value="Rock").pack(anchor="w")
    Radiobutton(root, text="Paper", variable=choice, value="Paper").pack(anchor="w")
    Radiobutton(root, text="Scissor", variable=choice, value="Scissor").pack(anchor="w")

    Button(root, text="Submit", command=show).pack(pady=10)

    root.mainloop()

#loop used to play game again or stop as user wanted
n = 1 
while n != 0:
    playgame()
    try:
        n = int(input("\nDo you want to play again? (1 = Yes, 0 = No,(any other no. also refer \"Yes\")): "))
    except ValueError:
        print("Invalid input. Exiting...")
        break

print("\nFinal score:", score)
