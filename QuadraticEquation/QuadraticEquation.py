from tkinter import *

def btn(event):
    x = table_name.get()
    x1 = table_name1.get()
    x2 = table_name2.get()
    Label(text="Дискриминант:", fg="dark blue").grid(row=2, column=6)
    D = int(x1)**2-4*int(x)*int(x2)
    label1 = Label(text=D)
    label1.grid(row=2, column=7)

    if D > 0:
        b = int(x1) - int(x1)*2

        x_1 = (b + D) / 2*int(x)
        Label(text="Первый x:", fg="dark green").grid(row=4, column=7)
        label_2 = Label(text=x_1)
        label_2.grid(row=4, column=9)
        x_2 = (b - D) / 2*int(x)
        Label(text="Второй x:", fg="dark green").grid(row=5, column=7)
        label_3 = Label(text=x_2)
        label_3.grid(row=5, column=9)

    elif D == 0:
        b = int(x1) - int(x1)*2

        x_1 = b / 2*int(x)
        Label(text="Первый x:", fg="dark green").grid(row=4, column=7)
        label_1 = Label(text=x_1)
        label_1.grid(row=4, column=9)
        Label(text="Второй x:", fg="dark green").grid(row=5, column=7)
        label_3 = Label(text="Отсуствует.")
        label_3.grid(row=5, column=9)
    else:
        Label(text="x:", fg="red").grid(row=5, column=7)
        label_1 = Label(text="Дискриминант меньше нуля, корни отсуствуют.")
        label_1.grid(row=5, column=8)

root = Tk()
root.geometry("600x200")
root.title("Solving a quadratic equation.")
#Запрос на число "а":
Label(text="Введите 'a':", fg="dark red").grid(row=0, column=0)
table_name = Entry(width=10)
table_name.grid(row=0, column=1, columnspan=3)
#Запрос на число "b":
Label(text="Введите 'b':", fg="dark red").grid(row=2, column=0)
table_name1= Entry(width=10)
table_name1.grid(row=2, column=1, columnspan=3)
#Запрос на число "c":
Label(text="Введите 'c':", fg="dark red").grid(row=3, column=0)
table_name2= Entry(width=10)
table_name2.grid(row=3, column=1, columnspan=3)
# КнопОчка...
button = Button(text="Решить", bg="gray", fg="white")
button.grid(row=2, column=5)

button.bind("<Button-1>",btn)
root.mainloop()