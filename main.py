import random
import gui

def guess():
    try:
        user_guess = int(gui.entry.get())
        computer_guess = random.randint(1,1000)
        if computer_guess == user_guess:
            gui.reward.configure(text='You Won',text_color='#00FF00')
        elif computer_guess >= user_guess:
            gui.reward.configure(text='Your number is smaller',text_color='#FF0000')
        elif computer_guess <= user_guess:
            gui.reward.configure(text='Your number is bigger',text_color='#FF0000')
    except ValueError:
        gui.reward.configure(text='You have put not a number value',text_color='#FFFF00')
        
if __name__ == '__main__':
    gui.root.mainloop()