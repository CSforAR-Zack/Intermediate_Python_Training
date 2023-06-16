from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main() -> None:
    wn = Tk()
    wn.title('Calculator')

    font_style = Font(family='Courier', size=20)

    entry_exp = Entry(master=wn, width=30, font=font_style)
    label_eq = Label(master=wn, text=' = ', font=font_style)
    label_result = Label(master=wn, text='0', font=font_style)
    button_calc = Button(master=wn, text='Calculate', font=font_style, command=lambda : calculate(entry_exp, label_result))

    # Layout for Grid
    #     0 1 2
    #   - - - - -
    #  0| x x x |
    #  1| x x x |
    #  2| x x x |
    #   - - - - -

    entry_exp.grid(row=0, column=0)
    label_eq.grid(row=0, column=1)
    label_result.grid(row=0, column=2)
    button_calc.grid(row=1)

    wn.mainloop()


def calculate(entry_obj, label_result):
    """Evaluate the expression in the entry widget.
    Update the label with the result on row 0.
    """

    # Note: Potential security risk using eval().
    # eval() will evaluate python code injected through input...
    # e.g. print("Cows are cool!")
    expression = entry_obj.get()
    result = eval(expression)
    label_result['text'] = result


if __name__ == '__main__':
    main()