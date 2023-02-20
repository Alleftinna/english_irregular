import tkinter as tk  # import tkinter lib with tk name
import get_word  # import other project file

size = '900x400'  # str
window = tk.Tk()  # create main window
frame = tk.Frame(window, bg='gray')  # Create a frame for buttons in main window
frame_text = tk.Frame(window, bg='gray')  # Create a frame for text in main window
sleep_time = 4000  # Delay in ms for auto words switch mode

# This function sets current words when it called
def set_words():
    words = get_word.get_rand()

    label_verbs['text'] = words  # Set attribute text to words sting

#  This function sets auto words switch mode
def set_autoload():
    if check_variable.get():  # If check boks is active
        next_word_button['state'] = tk.DISABLED  # Set NEXT_WORD button disable
        words = get_word.get_rand()  # Get next words
        label_verbs['text'] = words  # Set current words
        window.after(sleep_time, set_autoload)  # Recall set_autoload function
    else:  # If not check_box active - set NEXT_WORD button active
        next_word_button['state'] = tk.ACTIVE


check_variable = tk.BooleanVar()  # Variable for check_button

window.title('Irregular Verbs')
window.config(bg='gray')
window.geometry(size)  # Set size @size = '900x400'  # str@

label_verbs = tk.Label(frame_text, text=get_word.get_rand(),  # Set label with words
                       bg='gray',
                       font=('TimesNewRoman', '25', 'bold')
                       )
next_word_button = tk.Button(frame, text='Следующее слово',  # set NEXT_WORD BUTTON
                             bg='gray',
                             activebackground='gray',
                             command=set_words,

                             )
check_box = tk.Checkbutton(frame, text="Автоматически",  # set check box button
                           bg='gray',
                           variable=check_variable,
                           command=set_autoload,
                           disabledforeground='gray',
                           selectcolor='gray',
                           activebackground='gray',
                           highlightcolor='gray'

                           )

frame_text.pack(pady=140)  # Place frame for text

frame.pack(pady=10)  # Set frame for buttons
label_verbs.pack()  # Place text lable
check_box.pack(side='right')  # Place check_box
next_word_button.pack(side='left')  # set NEXT_WORD_BUTTON

if __name__ == "__main__":  # main condition
    window.mainloop()
