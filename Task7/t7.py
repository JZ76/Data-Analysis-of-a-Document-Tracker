
import tkinter as tk
from tkinter import *
from Task2 import t2
from Task3 import t3
from Task4 import t4
from Task5 import t5
import threading
button_row_number = 8


def click_country():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    if not input_textbox2.get():
        display_textbox.insert(END, "No doc ID entered\n")
    if (input_textbox1.get() and input_textbox2.get()):
        t2.view_by_country(input_textbox2.get(), input_textbox1.get())


def click_continent():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    if not input_textbox2.get():
        display_textbox.insert(END, "No doc ID entered\n")
    if (input_textbox1.get() and input_textbox2.get()):
        t2.view_by_continent(input_textbox2.get(), input_textbox1.get())



def click_all_browser():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    else:
        t3.view_by_browser_all(input_textbox1.get())


def click_main_browser():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    else:
        t3.view_by_browser(input_textbox1.get())

def __display_top_10(filename):
    display(t4.top_10_reader(filename))

def click_top10():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    else:
        temp = threading.Thread(target=__display_top_10, args=[input_textbox1.get()])
        temp.start()

def __display_alsolikes(userID, docID, filename):
    display(t5.alsolikes_sorted(userID, docID, filename))

def click_also_likes():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    if not input_textbox2.get():
        display_textbox.insert(END, "No doc ID entered\n")

    if (input_textbox1.get() and input_textbox2.get() and input_textbox3.get()):
        temp = threading.Thread(target=__display_alsolikes, args=[input_textbox3.get(), input_textbox2.get(), input_textbox1.get()])
        temp.start()
    elif (input_textbox1.get() and input_textbox2.get()):
        temp = threading.Thread(target=__display_alsolikes, args=["0", input_textbox2.get(), input_textbox1.get()])
        temp.start()


def click_also_likes_graph():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    if not input_textbox2.get():
        display_textbox.insert(END, "No doc ID entered\n")

    if (input_textbox1.get() and input_textbox2.get() and input_textbox3.get()):
        temp = threading.Thread(target=t5.generate_graph, args=(input_textbox3.get(), input_textbox2.get(), input_textbox1.get()))
        temp.start()
    elif (input_textbox1.get() and input_textbox2.get()):
        temp = threading.Thread(target=t5.generate_graph, args=("0", input_textbox2.get(), input_textbox1.get()))
        temp.start()

def read_input1():
    input_text = "-f " + input_textbox1.get()
    input_text += " -d " + input_textbox2.get()
    input_text += " -u " + input_textbox3.get()
    return input_text

def read_input2():
    input_text = "-f " + input_textbox1.get()
    input_text += " -d " + input_textbox2.get()
    return input_text
        
def display(result):
    display_textbox.insert(END, result)



def window_close():
    window.destroy()
    exit()

def GUI():
    global window
    window = tk.Tk()
    window.title("Document Tracker")
    window.configure(bg="black")
    window.geometry("900x600")


    Label(window, text="Enter JSON file name:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0,
                                                                                                  columnspan=2, sticky=W)
    global input_textbox1
    input_textbox1 = Entry(window, width=50, bg="white")
    input_textbox1.grid(row=2, column=0, columnspan=3, sticky=W)

    Label(window, text="Enter Document ID:", bg="black", fg="white", font="none 12 bold").grid(row=3, column=0,
                                                                                               columnspan=2, sticky=W)
    global input_textbox2
    input_textbox2 = Entry(window, width=50, bg="white")
    input_textbox2.grid(row=4, columnspan=3, sticky=W)

    Label(window, text="Enter User ID:", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0, columnspan=2, sticky=W)

    global input_textbox3
    input_textbox3 = Entry(window, width=50, bg="white")
    input_textbox3.grid(row=6, columnspan=3, sticky=W)

    Label(window, text="Select search option:", bg="black", fg="white", font="none 12 bold").grid(row=7, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky=W)

    Button(window, text="Views by country", width=15, command=click_country).grid(row=button_row_number, column=0,
                                                                                  sticky=W)

    Button(window, text="Views by continent", width=15, command=click_continent).grid(row=button_row_number, column=1,
                                                                                      sticky=W)

    Button(window, text="All Browsers", width=14, command=click_all_browser).grid(row=button_row_number, column=2,
                                                                                  sticky=W)

    Button(window, text="Main browser", width=14, command=click_main_browser).grid(row=button_row_number, column=3,
                                                                                   sticky=W)

    Button(window, text="Top 10 Readers", width=14, command=click_top10).grid(row=button_row_number, column=4, sticky=W)

    Button(window, text="Also Likes", width=14, command=click_also_likes).grid(row=button_row_number, column=5, sticky=W)

    Button(window, text="Also Likes Graph", width=14, command=click_also_likes_graph).grid(row=button_row_number, column=6,
                                                                                 sticky=W)

    Button(window, text="Help", width=14).grid(row=11, column=0, sticky=W)

    Button(window, text="Exit", width=14, command=window_close).grid(row=11, column=1, sticky=W)

    global display_textbox
    display_textbox = Text(window, width=100, height=20, wrap=WORD, bg="white")
    display_textbox.grid(row=10, column=0, columnspan=10, sticky=W)

    window.mainloop()

if __name__=="__main__":
    GUI()
