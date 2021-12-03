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
        processing_msg()
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
        processing_msg()
        temp = threading.Thread(target=__display_alsolikes,
                                args=[input_textbox3.get(), input_textbox2.get(), input_textbox1.get()])
        temp.start()
    elif (input_textbox1.get() and input_textbox2.get()):
        processing_msg()
        temp = threading.Thread(target=__display_alsolikes, args=["0", input_textbox2.get(), input_textbox1.get()])
        temp.start()


def click_also_likes_graph():
    display_textbox.delete(0.0, END)
    if not input_textbox1.get():
        display_textbox.insert(END, "No filename entered\n")
    if not input_textbox2.get():
        display_textbox.insert(END, "No doc ID entered\n")

    if (input_textbox1.get() and input_textbox2.get() and input_textbox3.get()):
        processing_msg()
        temp = threading.Thread(target=t5.generate_graph,
                                args=(input_textbox3.get(), input_textbox2.get(), input_textbox1.get()))
        temp.start()
    elif (input_textbox1.get() and input_textbox2.get()):
        processing_msg()
        temp = threading.Thread(target=t5.generate_graph, args=("0", input_textbox2.get(), input_textbox1.get()))
        temp.start()

def display(result):
    display_textbox.insert(END, result)

def processing_msg():
    display_textbox.insert(END, "Processing request...\n\n")

def complete_msg():
    display_textbox.insert(END, "Request complete\n\n")

def message():
    display_textbox.delete(0.0, END)
    msg = "To use the document track: \n1. Enter the the JSON file path, document ID and use ID (if applicable) " \
          "in the text boxes above. \n2. Then select an search option to process."
    display_textbox.insert(END, msg)

def window_close():
    window.destroy()
    exit()




def GUI(fileID, userID, docID):
    global file_ID
    global user_ID
    global doc_ID
    file_ID = fileID
    user_ID = userID
    doc_ID = docID

    global window
    window = tk.Tk()
    window.title("Document Tracker")
    window.configure(bg="black")
    window.geometry("1000x600")

    Label(window, text="Enter JSON file path:", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky=W)
    global input_textbox1
    input_textbox1 = Entry(window, width=50, bg="white")
    input_textbox1.grid(row=2, column=0, columnspan=3, sticky=W)
    input_textbox1.insert(0, fileID)

    Label(window, text="Enter Document ID:", bg="black", fg="white", font="none 12 bold").grid(row=3, column=0,
                                                                                               columnspan=2, sticky=W)
    global input_textbox2
    input_textbox2 = Entry(window, width=50, bg="white")
    input_textbox2.grid(row=4, columnspan=3, sticky=W)
    input_textbox2.insert(0, docID)

    Label(window, text="Enter User ID:", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0,
                                                                                           columnspan=2, sticky=W)

    global input_textbox3
    input_textbox3 = Entry(window, width=50, bg="white")
    input_textbox3.grid(row=6, columnspan=3, sticky=W)
    input_textbox3.insert(0, userID)

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

    Button(window, text="Also Likes", width=14, command=click_also_likes).grid(row=button_row_number, column=5,
                                                                               sticky=W)

    Button(window, text="Also Likes Graph", width=14, command=click_also_likes_graph).grid(row=button_row_number,
                                                                                           column=6,
                                                                                           sticky=W)

    Button(window, text="Help", width=14, command=message).grid(row=11, column=0, sticky=W)

    Button(window, text="Exit", width=14, command=window_close).grid(row=11, column=1, sticky=W)

    global display_textbox
    display_textbox = Text(window, width=125, height=20, wrap=WORD, bg="white")
    display_textbox.grid(row=10, column=0, columnspan=10, sticky=W)

    message()

    click_also_likes_graph()

    window.mainloop()


if __name__ == "__main__":
    GUI(r"C:\Users\myper\Desktop\Industrial Programming\Data-Analysis-of-a-Document-Tracker\sample_3m_lines.json", "0","140218134226-85827c1f2cec7cde188f60901c23558d"
                      )