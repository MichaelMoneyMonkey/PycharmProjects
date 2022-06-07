import tkinter

# Give tkinter a name
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

# Column 1
# Label 1
label1 = tkinter.Label(text="is equal to")
label1.grid(column=0, row=1)
label1.config(padx=10, pady=10)


# Column 2
# Entry1
input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

# Label Km
label_km = tkinter.Label(text="0")
label_km.grid(column=1, row=1)

# Button
def button_clicked():
    print("I got clicked")
    user_input = float(input_miles.get())
    result = user_input * 1.609
    result_two_decimals = round(result, 2)
    label_km.config(text=result_two_decimals)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# Column 3
# Label 2
label2 = tkinter.Label(text="Miles")
label2.grid(column=2, row=0)
label2.config(padx=10, pady=10)

# Label 3
label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)
label3.config(padx=10, pady=10)












# Keep the window open
window.mainloop()