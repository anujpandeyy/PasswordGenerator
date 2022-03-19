import random
import tkinter

main_window = tkinter.Tk()

main_window.title("Password Generator")
main_window.geometry('800x300')
padd = 50
main_window['padx'] = padd
main_window['pady'] = padd
chk = tkinter.IntVar()


def password_generate(leng):
    vaild_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS0123456789"
    password = "".join(random.sample(vaild_char, leng))
    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)


def checkbox_check():
    if chk.get() == 6:
        password_generate(6)
    elif chk.get() == 10:
        password_generate(10)
    elif chk.get() == 12:
        password_generate(12)
    else:
        password_generate(8)


title_text = tkinter.Label(text="Password Generator")
title_text.grid(row=0, column=0)
display_result = tkinter.Entry()
display_result.grid(row=1, column=0)

chkone = tkinter.Radiobutton(main_window, text="6 character", variable=chk, value=6)
chkone.grid(row=2, column=0)

chktwo = tkinter.Radiobutton(main_window, text="10 character", variable=chk, value=10)
chktwo.grid(row=3, column=0)

chkthree = tkinter.Radiobutton(main_window, text="12 character", variable=chk, value=12)
chkthree.grid(row=4, column=0)

pass_generate = tkinter.Button(text="Generate", command=checkbox_check)
pass_generate.grid(row=5, column=0)
main_window.mainloop()
