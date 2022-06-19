# Peforms the following tasks:
# - Conversion on single numbers

from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main():
    wn = Tk()
    wn.title('Base Converter')

    font_style = Font(family='Courier', size=20)

    entry_exp = Entry(master=wn, width=30, font=font_style)
    label_eq = Label(master=wn, text=' = ', font=font_style)
    label_result = Label(master=wn, text='0', font=font_style)    

    entry_exp.grid(row=0, column=0)
    label_eq.grid(row=0, column=1)
    label_result.grid(row=0, column=2)

    button_calc = Button(master=wn, text='Calculate', font=font_style, command=lambda : converter(entry_exp, label_result))

    button_calc.grid(row=1)

    wn.mainloop()


def converter(entry_obj, label_result):
    """ Converts the number into all bases. """

    text = entry_obj.get()
    digits = text[2:]

    if '0b' in text:
        decimal = int(digits, 2)
    elif '0o' in text:
        decimal = int(digits, 8)
    elif '0d' in text:
        decimal = int(digits)
    elif '0x' in text:
        decimal = int(digits, 16)

    binary_num = bin(decimal)
    octal_num = oct(decimal)
    decimal_num = f'0d{decimal}'
    hex_num = hex(decimal)

    label_result['text'] =  f'{binary_num}, {octal_num}, {decimal_num}, {hex_num}'


if __name__ == '__main__':
    main()
