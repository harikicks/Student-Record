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

#Set Table Data
def setTableData(table, studentData):
    i = 0
    for student in studentData:
        table.insert(parent = '', index = i, values = (student['name'], student['section'], student['ID'], student['vi']))
        i+=1

#remove 
def remove_multiple():
    y = table.selection()
    for item in y:
        table.delete(item)

#Search
def search(id):
    for item in table.get_children():
        print(item)
        row = table.item(item, 'values')
        print(row)
        # TUPM-23-3453
        if not id in row:
            table.delete(item)
            # return True
    return False

#Search button function
def search_func():
    search_ID = E5.get() 
    if search_ID:
        if search(search_ID):
            print("Search Result:", f"'{search_ID}' Found." )
            
            
        else:
            print("Search Result:", f"'{search_ID}' Not Found.")
    else:
        print("Input Error", "Please enter a value to search.")

#Reset button function
def reset_func():
    for item in table.get_children():
        table.delete(item)
        # TUPM-23-3453
        # if not id in row:
        #     table.move(item, table.parent(item))
            # return True
    setTableData(table, studentData)

# window
window = tk.Tk()
window.geometry("1320x620")
window.title('Office of Student Affair Violation Record')

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
ttk.Button(frame, text='Search', command=search_func).place(x=120, y=300)
ttk.Button(frame, text='Reset', command=reset_func).place(x=200, y=300)

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

studentData=[{"name":"Africano, Luigi V","section":"BET-CPET-1B","ID":"TUPM-23-2355","vi":"Improper Hair Color"},
{"name":"Armendi, Francis M","section":"BET-CPET-1B","ID":"TUPM-23-2345","vi":"Improper Uniform"},
{"name":"De Guzman, Jose Miguel T.","section":"BET-CPET-1B","ID":"TUPM-23-3453","vi":"Improper Hairsyle"},
{"name":"Dela Cruz, Kean Jarrelle P.","section":"BET-CPET-1B","ID":"TUPM-23-3344","vi":"Hazing"},
{"name":"Dizon, Christian Edward R..","section":"BET-CPET-1B","ID":"TUPM-23-5676","vi":"Gambling"},
{"name":"Esguerra, Earl Cedric C.","section":"BET-CPET-1B","ID":"TUPM-23-8970","vi":"Smoking"},
{"name":"Espineda, Racel F.","section":"BET-CPET-1B","ID":"TUPM-23-4854","vi":"Smoking"},
{"name":"Espino, Lance Andrie B.","section":"BET-CPET-1B","ID":"TUPM-23-3423","vi":"Bullying"},
{"name":"Gadin, Rogene Lyle C","section":"BET-CPET-1B","ID":"TUPM-23-1211","vi":"Cyber Bullying"},
{"name":"Gullon, Rodrigo L.","section":"BET-CPET-1B","ID":"TUPM-23-2211","vi":"Liquor and Prohibited Drugs"},
{"name":"Iniquillo, Marc Oliver C.","section":"BET-CPET-1B","ID":"TUPM-23-1122","vi":"Illegal Assembly"},
{"name":"Jaducana, Jelo Arviel C.","section":"BET-CPET-1B","ID":"TUPM-23-3321","vi":"Failure to Account Funds"},
{"name":"Lacdao, Justin Zeus V.","section":"BET-CPET-1B","ID":"TUPM-23-1132","vi":"Physical Assault"},
{"name":"Lorenzo, Jamielyza P.","section":"BET-CPET-1B","ID":"TUPM-23-2313","vi":"Robbery"},
{"name":"Mendiola, Jofryl Drew L.","section":"BET-CPET-1B","ID":"TUPM-23-8899","vi":"Vandalism"},
{"name":"Reyes, Christian Jericho R.","section":"BET-CPET-1B","ID":"TUPM-23-0167","vi":"Trespassing"},
{"name":"Rivera, Lezlie R. ","section":"BET-CPET-1B","ID":"TUPM-23-0101","vi":"Slander"},
{"name":"Sebastian, John Edanwil S.","section":"BET-CPET-1B","ID":"TUPM-23-0123","vi":"Falsification of Documents"},
{"name":"Sevilla, Aeron John A.","section":"BET-CPET-1B","ID":"TUPM-23-0124","vi":"Academic Dishonesty"},
{"name":"abudlo, Charlotte D.","section":"BET-CPET-1B","ID":"TUPM-23-0125","vi":"Bribery"},
{"name":"Tanuyan, Karl Raphael E.","section":"BET-CPET-1B","ID":"TUPM-23-0643","vi":"Swindling"},
{"name":"Villapaña, Pocholo V.","section":"BET-CPET-1B","ID":"TUPM-23-0342","vi":"Smoking"},
]

setTableData(table, studentData)

window.mainloop()