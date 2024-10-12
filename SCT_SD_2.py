#random number generator
import customtkinter as ctk
import random

#appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#app window
root = ctk.CTk()
root.geometry("300x400")
root.title("Guessing game")

#logic
global the_num
def setNew():
    global the_num
    the_num = random.randint(0,100)
    if(btn._text != "Start Game"):
        num_ip.delete(0,"end")
    qn.configure(text="?")
    info.configure(text="Try a number\nbetween 0 to 100")

    btn.configure(text="Lock in", command=guess)
    info.grid(row=1, column=0, padx=10, pady=0)
    qn.grid(row=2, column=0,padx=10,pady=6)
    num_ip.grid(row=3,column=0,padx=10,pady=2)
    

def guess():
    n = int(num_ip.get())
    print(the_num)
    if(the_num == n):
        info.configure(text="You guessed it right!\nThe number was:")
        qn.configure(text=str(n))
        btn.configure(text="New Game", command=setNew)
    elif(n>100 or n<0):
        info.configure(text="Out of Bounds\nRange: 0 to 100")
        num_ip.delete(0,"end")
    else:
        if the_num>n:
            info.configure(text="wrong!\nTry a num greater than "+str(n))
        else:
            info.configure(text="wrong!\nTry a num less than "+str(n))
        num_ip.delete(0,"end")

#main app frame
frame = ctk.CTkFrame(master=root)
frame.grid(row=0, column=0, pady=25, padx=35, sticky="nsew")

app_title = ctk.CTkLabel(master=frame, text="guess the number", font=("HP Simplified", 27))
app_title.grid(row=0, column=0, padx=10, pady=3)

info = ctk.CTkLabel(master=frame, text="Try a number\nbetween 0 to 100", font=("Comic Sans MS", 14))

qn = ctk.CTkLabel(master=frame, text="?", font=("Harrington", 80))

num_ip = ctk.CTkEntry(master=frame,placeholder_text="your guess")

btn = ctk.CTkButton(master=frame,text="Start Game", font=("Comic Sans MS", 15, "bold"),command= setNew)
btn.grid(row=4, column=0, padx=10, pady=8)

root.mainloop()