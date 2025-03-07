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
    
def status_modifier(library, n, borrow=0, resotre=0):
    # this will help in case if the book is borrowed and you want to return it, and will also help in case if the book is avaliable and you want to retrun it.
    if n in library:
        book_status = list(library[n].values())[-1]
        if borrow == 1:
            book_status = "bor"
        if resotre == 1:
            book_status = "ava"
    else:
        print("The book doesn't exist.")

def borrow_book(library, n):
    if n in library:    
        book_status = list(library[n].values())[-1]
        if book_status == "ava":
            print(f"This book is avalilable.")
            
            # make function for the status updating will be better!!!    
        else:
            book_status == "bor"
            print("this book is borrowed.")
            
    else:
        print("This book doesn't exist at the library.")
        
def resotre_book(library, n):
    pass

# My_Library = load_library()
# delete_book(My_Library, int(input("Plz enter the number of book you want to delete: ")))
# add_book(My_Library)
# save_library(My_Library)
# borrow_book(My_Library, int(input("Plz enter the number of book you want to inquire about: ")))
# status_modifier(My_Library, int(input("Plz enter the book you wnat to know it's status: ")))
# display_library(My_Library)   