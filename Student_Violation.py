import tkinter as tk
from tkinter import ttk

def button_func():
    print(E1.get())
    print(E2.get())
    print(E3.get())
    print(E4.get())
    table.insert(parent = '', index = 0, values = (
    E1.get(),
    E2.get(),
    E3.get(),
    E4.get()
    ))

#remove 
def remove_multiple():
    y = table.selection()
    for item in y:
        table.delete(item)




# window
window = tk.Tk()
window.geometry("1320x620")
window.title('Student Violation Record')

#frame
frame = ttk.Frame(window, width= 300, height= 500, borderwidth= 10, relief= tk.GROOVE)
frame.pack_propagate(False)
frame.place(x=20,y=50)

#label for the frame/master

label =ttk.Label(frame, text= "Student Name:",font=('Arial',10,'bold'))
label.place(x=0,y=0)
label =ttk.Label(frame, text= "Section:",font=('Arial',10,'bold'))
label.place(x=0,y=40)
label =ttk.Label(frame, text= "ID Number",font=('Arial',10,'bold'))
label.place(x=0,y=80)
label =ttk.Label(frame, text= "Student Violation:",font=('Arial',10,'bold'))
label.place(x=0,y=120)


#Gender with list

gender = ('Male', 'Female')
Gender_string =tk.StringVar()
combo = ttk.Combobox(frame, textvariable= Gender_string)
combo['values'] = gender
combo.place(x=135,y=160)
combo.bind('<<ComboboxSelected>>', lambda event: print(Gender_string.get()))



#user input E stand for entry
E1 = ttk.Entry(frame)
E1.place(x=150,y=0)
E2 = ttk.Entry(frame)
E2.place(x=150,y=40)
E3 = ttk.Entry(frame)
E3.place(x=150,y=80)
E4 = ttk.Entry(frame)
E4.place(x=150,y=120)

#Add button
button = ttk.Button(frame, text= 'Add', command = button_func)
button.place(x=100,y=200)

#delete button
button = ttk.Button(frame, text= 'Remove', command = remove_multiple) 
button.place(x=100,y=225)

#frame 2 table
frame2 = ttk.Frame(window, width= 820, height= 300, borderwidth= 10, relief= tk.GROOVE)
frame2.pack_propagate(True)
frame2.place(x=350,y=250)

#table
table = ttk.Treeview(frame2, column = ('first','second','third', 'fourth'), show = 'headings')
table.heading('first', text = 'Student Name')
table.heading('second', text = 'Section')
table.heading('third', text = 'ID Number')
table.heading('fourth', text = 'Violation')
table.pack()

table.insert(parent = '', index = 0, values = ('Africano, Luigi V','BET-CPET-1B','TUPM-23-2355','N/A'))
table.insert(parent = '', index = 0, values = ('Armendi, Francis M','BET-CPET-1B','TUPM-23-3344','N/A'))
table.insert(parent = '', index = 0, values = ('Cuerda, Bea Bianca B. ','BET-CPET-1B','TUPM-23-3453','N/A'))
table.insert(parent = '', index = 0, values = ('De Guzman, Jose Miguel T.','BET-CPET-1B','TUPM-23-3454','N/A'))
table.insert(parent = '', index = 0, values = ('Dela Cruz, Kean Jarrelle P. ','BET-CPET-1B','TUPM-23-3344','N/A'))
table.insert(parent = '', index = 0, values = ('Dizon, Christian Edward R.','BET-CPET-1B','TUPM-23-5676','N/A'))
table.insert(parent = '', index = 0, values = ('Esguerra, Earl Cedric C.','BET-CPET-1B','TUPM-23-8970','N/A'))
table.insert(parent = '', index = 0, values = ('Espineda, Racel F.','BET-CPET-1B','TUPM-23-4854','N/A'))
table.insert(parent = '', index = 0, values = ('Espino, Lance Andrie B.','BET-CPET-1B','TUPM-23-3423','N/A'))
table.insert(parent = '', index = 0, values = ('Gadin, Rogene Lyle C','BET-CPET-1B','TUPM-23-1211','N/A'))
table.insert(parent = '', index = 0, values = ('Gullon, Rodrigo L.','BET-CPET-1B','TUPM-23-2211','N/A'))
table.insert(parent = '', index = 0, values = ('Iniquillo, Marc Oliver C. ','BET-CPET-1B','TUPM-23-1122','N/A'))
table.insert(parent = '', index = 0, values = ('Jaducana, Jelo Arviel C.','BET-CPET-1B','TUPM-23-3321','N/A'))
table.insert(parent = '', index = 0, values = ('Lacdao, Justin Zeus V.','BET-CPET-1B','TUPM-23-1132','N/A'))
table.insert(parent = '', index = 0, values = ('Lorenzo, Jamielyza P.','BET-CPET-1B','TUPM-23-2313','N/A'))
table.insert(parent = '', index = 0, values = ('Mendiola, Jofryl Drew L.  ','BET-CPET-1B','TUPM-23-8899','N/A'))
table.insert(parent = '', index = 0, values = ('Ocampo, Joshua C.  ','BET-CPET-1B','TUPM-23-0097','N/A'))
table.insert(parent = '', index = 0, values = ('Reyes, Christian Jericho R. ','BET-CPET-1B','TUPM-23-0167','N/A'))
table.insert(parent = '', index = 0, values = ('Rivera, Lezlie R.  ','BET-CPET-1B','TUPM-23-0101','N/A'))
table.insert(parent = '', index = 0, values = ('Sebastian, John Edanwil S. ','BET-CPET-1B','TUPM-23-0123','N/A'))
table.insert(parent = '', index = 0, values = ('Sevilla, Aeron John A.','BET-CPET-1B','TUPM-23-0124','N/A'))
table.insert(parent = '', index = 0, values = ('abudlo, Charlotte D. ','BET-CPET-1B','TUPM-23-0125','N/A'))
table.insert(parent = '', index = 0, values = ('Tanuyan, Karl Raphael E. ','BET-CPET-1B','TUPM-23-0643','N/A'))
table.insert(parent = '', index = 0, values = ('Villapaña, Pocholo V.','BET-CPET-1B','TUPM-23-0342','N/A'))


window.mainloop()