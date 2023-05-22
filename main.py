from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result.config(text=str(km))

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=80)
window.config(pady=20, padx=20)

# Miles Input
input = Entry(width=7)
input.insert(END, string=0)
input.grid(row=0, column=1)

# "Miles" label
miles = Label(text="Miles")
miles.grid(row=0, column=2)

# "is equal to" label
isequalto = Label(text="is equal to")
isequalto.grid(row=1, column=0)

# "result" label
result = Label(text="0")
result.grid(row=1, column=1)

# "Km" label
Km = Label(text="Km")
Km.grid(row=1, column=2)

# "Calculate" button
cal = Button(text="Calculate", command=miles_to_km)
cal.grid(row=2, column=1)




window.mainloop()
