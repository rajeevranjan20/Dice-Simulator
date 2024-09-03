import tkinter as tk
from PIL import Image,ImageTk
import random

root=tk.Tk()
root.geometry('600x600')
root.title('Hey Can you Roll the Dice')

BlankLine=tk.Label(root,text="")
BlankLine.pack()

HeadingLabel=tk.Label(root,text='Hello!😎',fg='light green',bg='grey',font='Helvetica 16 bold italic')
HeadingLabel.pack()

dice=['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel=tk.Label(root,image=DiceImage)
ImageLabel.image=DiceImage


ImageLabel.pack(expand=True)


def rolling_dice():
    DiceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image=DiceImage

button=tk.Button(root,text='Roll the Dice',fg='blue',command=rolling_dice)  
button.pack(expand=True)

root.mainloop()