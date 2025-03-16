from tkinter import*
import random
app= Tk()
app.geometry('400x340')
app.title("Love Calculator❤️💕")

def calculate():
    #value wii contain digit between 0 to 9
    st_value='0123456789'
    output_digit=2
    output=''.join(random.sample(st_value,output_digit))
    result.config(text=output, fg="darkorange")
   
heading = Label(app, text="💕 Love Calculator ❤️", font=("Arial", 16), fg="red")
heading.pack(pady=10)

slot1 = Label(app, text="Enter your name: ", font=("Arial", 12))
slot1.pack()
name1 = Entry(app, border=5, font=("Arial", 12))
name1.pack(pady=5)

slot2 = Label(app, text="Enter your Friend's name: ", font=("Arial", 12))
slot2.pack()
name2 = Entry(app, border=5, font=("Arial", 12))
name2.pack(pady=5)

button1 = Button(app, text="Calculate", height=2, width=10, command=calculate, bg="violet", font=("Arial", 10))
button1.pack(pady=10)

result = Label(app, text="Percentage between both of you: ", font=("Arial", 12))
result.pack(pady=10)

app.mainloop()

