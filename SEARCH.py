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

#Search
def search(studentname, n):
    for value in table.get_children():
        values = table.item(value, 'values')
        if n in values:
            return True
    return False

#Search button function
def search_func():
    A = search_ID = E5.get() 
    if search_ID:
        if search(studentname, search_ID):
            print("Search Result:", f"'{search_ID}' Found." )
            print(studentname[]["name"])
        else:
            print("Search Result:", f"'{search_ID}' Not Found.")
    else:
        print("Input Error", "Please enter a value to search.")


# window
window = tk.Tk()
window.geometry("1320x620")
window.title('Student Violation Record')

#frame
frame = ttk.Frame(window, width= 300, height= 500, borderwidth= 10, relief= tk.GROOVE)
frame.pack_propagate(False)
frame.place(x=20,y=50)

#search menu


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
E5 = ttk.Entry(frame)
E5.place(x=150,y=275)

#Add button
button = ttk.Button(frame, text= 'Add', command = button_func)
button.place(x=100,y=200)

#delete button
button = ttk.Button(frame, text= 'Remove', command = remove_multiple) 
button.place(x=100,y=225)

#Search Input Text box
label =ttk.Label(frame, text= "Search Student ID:",font=('Arial',10,'bold'))
label.place(x=0,y=275)

# Search button
ttk.Button(frame, text='Search', command=search_func).place(x=150, y=300)

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

studentname=[{"name":"Africano, Luigi V","section":"BET-CPET-1B","ID":"TUPM-23-2355","vi":"N/A"},
{"name":"Armendi, Francis M","section":"BET-CPET-1B","ID":"TUPM-23-2355","vi":"N/A"},
{"name":"De Guzman, Jose Miguel T.","section":"BET-CPET-1B","ID":"TUPM-23-3453","vi":"N/A"},
{"name":"Dela Cruz, Kean Jarrelle P.","section":"BET-CPET-1B","ID":"TUPM-23-3344","vi":"N/A"},
{"name":"Dizon, Christian Edward R..","section":"BET-CPET-1B","ID":"TUPM-23-5676","vi":"N/A"},
{"name":"Esguerra, Earl Cedric C.","section":"BET-CPET-1B","ID":"TUPM-23-8970","vi":"N/A"},
{"name":"Espineda, Racel F.","section":"BET-CPET-1B","ID":"TUPM-23-4854","vi":"N/A"},
{"name":"Espino, Lance Andrie B.","section":"BET-CPET-1B","ID":"TUPM-23-3423","vi":"N/A"},
{"name":"Gadin, Rogene Lyle C","section":"BET-CPET-1B","ID":"TUPM-23-1211","vi":"N/A"},
{"name":"Gullon, Rodrigo L.","section":"BET-CPET-1B","ID":"TUPM-23-2211","vi":"N/A"},
{"name":"Iniquillo, Marc Oliver C.","section":"BET-CPET-1B","ID":"TUPM-23-1122","vi":"N/A"},
{"name":"Jaducana, Jelo Arviel C.","section":"BET-CPET-1B","ID":"TUPM-23-3321","vi":"N/A"},
{"name":"Lacdao, Justin Zeus V.","section":"BET-CPET-1B","ID":"TUPM-23-1132","vi":"N/A"},
{"name":"Lorenzo, Jamielyza P.","section":"BET-CPET-1B","ID":"TUPM-23-2313","vi":"N/A"},
{"name":"Mendiola, Jofryl Drew L.","section":"BET-CPET-1B","ID":"TUPM-23-8899","vi":"N/A"},
{"name":"Reyes, Christian Jericho R.","section":"BET-CPET-1B","ID":"TUPM-23-0167","vi":"N/A"},
{"name":"Rivera, Lezlie R. ","section":"BET-CPET-1B","ID":"TUPM-23-0101","vi":"N/A"},
{"name":"Sebastian, John Edanwil S.","section":"BET-CPET-1B","ID":"TUPM-23-0123","vi":"N/A"},
{"name":"Sevilla, Aeron John A.","section":"BET-CPET-1B","ID":"UPM-23-0124","vi":"N/A"},
{"name":"abudlo, Charlotte D.","section":"BET-CPET-1B","ID":"TUPM-23-0125","vi":"N/A"},
{"name":"Tanuyan, Karl Raphael E.","section":"BET-CPET-1B","ID":"TUPM-23-0643","vi":"N/A"},
{"name":"Villapaña, Pocholo V.","section":"BET-CPET-1B","ID":"TUPM-23-0342","vi":"N/A"},
]

table.insert(parent = '', index = 0, values = (studentname[0]['name'],studentname[0]['section'],studentname[0]['ID'],studentname[0]['vi']))
table.insert(parent = '', index = 0, values = (studentname[1]['name'],studentname[1]['section'],studentname[1]['ID'],studentname[1]['vi']))
table.insert(parent = '', index = 0, values = (studentname[2]['name'],studentname[2]['section'],studentname[2]['ID'],studentname[2]['vi']))
table.insert(parent = '', index = 0, values = (studentname[3]['name'],studentname[3]['section'],studentname[3]['ID'],studentname[3]['vi']))
table.insert(parent = '', index = 0, values = (studentname[4]['name'],studentname[4]['section'],studentname[4]['ID'],studentname[4]['vi']))
table.insert(parent = '', index = 0, values = (studentname[5]['name'],studentname[5]['section'],studentname[5]['ID'],studentname[5]['vi']))
table.insert(parent = '', index = 0, values = (studentname[6]['name'],studentname[6]['section'],studentname[6]['ID'],studentname[6]['vi']))
table.insert(parent = '', index = 0, values = (studentname[7]['name'],studentname[7]['section'],studentname[7]['ID'],studentname[7]['vi']))
table.insert(parent = '', index = 0, values = (studentname[8]['name'],studentname[8]['section'],studentname[8]['ID'],studentname[8]['vi']))
table.insert(parent = '', index = 0, values = (studentname[9]['name'],studentname[9]['section'],studentname[9]['ID'],studentname[9]['vi']))
table.insert(parent = '', index = 0, values = (studentname[10]['name'],studentname[10]['section'],studentname[10]['ID'],studentname[10]['vi']))
table.insert(parent = '', index = 0, values = (studentname[11]['name'],studentname[11]['section'],studentname[11]['ID'],studentname[11]['vi']))
table.insert(parent = '', index = 0, values = (studentname[12]['name'],studentname[12]['section'],studentname[12]['ID'],studentname[12]['vi']))
table.insert(parent = '', index = 0, values = (studentname[13]['name'],studentname[13]['section'],studentname[13]['ID'],studentname[13]['vi']))
table.insert(parent = '', index = 0, values = (studentname[14]['name'],studentname[14]['section'],studentname[14]['ID'],studentname[14]['vi']))
table.insert(parent = '', index = 0, values = (studentname[15]['name'],studentname[15]['section'],studentname[15]['ID'],studentname[15]['vi']))
table.insert(parent = '', index = 0, values = (studentname[16]['name'],studentname[16]['section'],studentname[16]['ID'],studentname[16]['vi']))
table.insert(parent = '', index = 0, values = (studentname[17]['name'],studentname[17]['section'],studentname[17]['ID'],studentname[17]['vi']))
table.insert(parent = '', index = 0, values = (studentname[18]['name'],studentname[18]['section'],studentname[18]['ID'],studentname[18]['vi']))
table.insert(parent = '', index = 0, values = (studentname[19]['name'],studentname[19]['section'],studentname[19]['ID'],studentname[19]['vi']))
table.insert(parent = '', index = 0, values = (studentname[20]['name'],studentname[20]['section'],studentname[20]['ID'],studentname[20]['vi']))
table.insert(parent = '', index = 0, values = (studentname[21]['name'],studentname[21]['section'],studentname[21]['ID'],studentname[21]['vi']))


table.insert(parent = '', index = 0, values = (studentname[0]['name'],studentname[0]['section'],studentname[0]['ID'],studentname[0]['vi']))
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