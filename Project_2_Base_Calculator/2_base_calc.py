# Peforms the following tasks:
# - Conversion on single numbers

from tkinter import Tk, Entry, Label, Button, Spinbox
from tkinter.font import Font

def main():
    # Create the window and set the title
    wn = Tk()
    wn.title('Base Converter')

    # Create a font style: Optional
    font_style = Font(family='Courier', size=20)

    # Create the widgets
    # We used these ones however there are different widgets you can use to get the same result
    entry_number = Entry(master=wn, font=font_style)
    base_input_selector = Spinbox(master=wn, values=('Hexidecimal', 'Decimal', 'Octal', 'Binary'), font=font_style)
    base_output_selector = Spinbox(master=wn, values=('Hexidecimal', 'Decimal', 'Octal', 'Binary'), font=font_style)
    button_encode = Button(master=wn, text='Encode', font=font_style, command=lambda : converter(entry_number, base_input_selector, base_output_selector, label_result))
    label_result = Label(master=wn, text='-', font=font_style)

    # Pack them vertically starting at top
    # Padx and pady are the padding on the x and y axis
    padx = 10
    pady = 5

    entry_number.grid(row=0, column=0, padx=padx, pady=pady, sticky='ewns')
    base_input_selector.grid(row=1, column=0, padx=padx, pady=pady, sticky='ew')
    base_output_selector.grid(row=2, column=0, padx=padx, pady=pady, sticky='ew')
    button_encode.grid(row=3, column=0, padx=padx, pady=pady, sticky='ew')
    label_result.grid(row=4, column=0, padx=padx, pady=pady, sticky='ew')

    # Alternative way to pack them vertically
    # entry_number.pack(fill='x', padx=padx, pady=pady)
    # base_input_selector.pack(fill='x', padx=padx, pady=pady)
    # base_output_selector.pack(fill='x', padx=padx, pady=pady)
    # button_encode.pack(fill='x', padx=padx, pady=pady)
    # label_result.pack(fill='x', padx=padx, pady=pady)

    # Start the main loop to listen for events such as button clicks or entry changes
    wn.mainloop()

def converter(entry, input_base, output_base, output_label):
    """
    Converts a number from one base to another.
    """
    # Get the number from the entry
    number = entry.get()

    # Get the input base
    input_base = input_base.get()

    # Get the output base
    output_base = output_base.get()

    # Convert the number to decimal
    if input_base == 'Binary':
        number = int(number, 2)
    elif input_base == 'Octal':
        number = int(number, 8)
    elif input_base == 'Decimal':
        number = int(number, 10)
    elif input_base == 'Hexadecimal':
        number = int(number, 16)

    # Convert the number to the output base
    if output_base == 'Binary':
        number = bin(number)[2:]
    elif output_base == 'Octal':
        number = oct(number)[2:]
    elif output_base == 'Decimal':
        number = int(number)
    elif output_base == 'Hexadecimal':
        number = hex(number)[2:].upper()

    # Display the result
    output_label.config(text=number)

    # Other way to display the result
    output_label['text'] = number


if __name__ == '__main__':
    main()
