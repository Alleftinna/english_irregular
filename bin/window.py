import tkinter as tk
import get_word






size = '900x400'
window = tk.Tk()
frame = tk.Frame(window, bg='gray')
frame_text = tk.Frame(window, bg='gray')
sleep_time = 4000


def set_words():
    words = get_word.get_rand()

    lable_verbs['text'] = words


def set_autoload():
    if check_variable.get():
        rand_verb_button['state'] = tk.DISABLED
        words = get_word.get_rand()
        lable_verbs['text'] = words
        window.after(sleep_time, set_autoload)
    else:
        rand_verb_button['state'] = tk.ACTIVE


check_variable = tk.BooleanVar()

window.title('Irregular Verbs')
window.config(bg='gray')
window.geometry(size)

a = 'Читать     read    red     red'
lable_verbs = tk.Label(frame_text, text=get_word.get_rand(),
                       bg= 'gray',
                       font=('TimesNewRoman', '25', 'bold')
                       )
rand_verb_button = tk.Button(frame, text='Следующее слово',
                             bg='gray',
                             activebackground='gray',
                             command=set_words,

                             )
check_box = tk.Checkbutton(frame, text="Автоматически",
                           bg='gray',
                           variable=check_variable,
                           command=set_autoload,
                           disabledforeground='gray',
                           selectcolor='gray',
                           activebackground='gray',
                           highlightcolor='gray'


                           )

frame_text.pack(pady=140)

frame.pack( pady=10)
lable_verbs.pack()
check_box.pack(side='right')
rand_verb_button.pack(side='left')


if __name__ == "__main__":
    window.mainloop()
