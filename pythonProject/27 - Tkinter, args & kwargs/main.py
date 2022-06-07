import tkinter

# Give tkinter a name
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# .grid = incompatible with .pack
my_label.grid(column=0, row=0)
my_label.config(padx=40, pady=40)

# Change text of label: option 1
my_label["text"] = "New Text"
# Change text of label: option 2
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="Click me", command=button_clicked)
# button.place(x=10, y=80)
button.grid(column=1, row=1)

# Button 2
button2 = tkinter.Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)












# Keep the window open
window.mainloop()