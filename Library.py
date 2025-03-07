import json
My_Library = {
    1: {"bookname": "Love and War", "bookauthor": "unknown", "bookstatus": "bor"},
    2: {"bookname": "Death", "bookauthor": "killer", "bookstatus": "ava"},
    3: {"bookname": "How to play", "bookauthor": "warrior", "bookstatus": "ava"}
}

def load_library():
    try:
        with open("my_library.json", "r" ) as file:
            library = json.load(file)
    except FileNotFoundError:
        library = {}
    return library   

def save_library(library):
    with open("my_library.json", "w") as file:
        json.dump(library, file)
        
def add_book(library):
    while True:
        book_num = int(input("plz enter the book's number: "))
        book_name = input("plz enter the book's name: ")
        book_author = input("plz enter the book's author: ")
        book_status = input("plz enter the book's status: (ava/bor)")
        choice = input("Do you want to add another book? if you want to exist press (n), if you don't press any botton to continue. ")
        
        library[book_num] = {"bookname": book_name, "bookauthor": book_author, "bookstatus": book_status}
        
        if choice.lower() == "n":
            break    
    return library

def display_library(library):
    for key1, value1 in library.items():
        print(f"Book number: {key1}")
        for key2, value2 in value1.items():
            print(f"{key2.capitalize()}: {value2}")
        print()

def delete_book(library, n):
    del library[n]
    

def borrow_book(library, n):
    if n in library:    
        for key, value in library[n].items():
            pass
        if value == "ava":
            print(f"This book is avalilable.")
            delete_book(library, n)
            display_library(library)
            
        else:
            value == "bor"
            print("this book is borrowed.")
    else:
        print("This book doesn't exist at the library.")

# My_Library = load_library()
# delete_book(My_Library, int(input("Plz enter the number of book you want to delete: ")))
# add_book(My_Library)
# save_library(My_Library)
# borrow_book(My_Library, int(input("Plz enter the number of book you want to inquire about: ")))
display_library(My_Library)   