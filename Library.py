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
        library = {int(key): value for key,value in library.items()}
    except FileNotFoundError:
        library = {}
    return library   

def save_library(library):
    with open("my_library.json", "w") as file:
        json.dump(library, file)
        
def add_book(library):
    while True:
        book_num_input = input("plz enter the book's number: ")
        if not book_num_input.isdigit():
            print("Invalid input! The book number must be a positive integer.")
            continue
        book_num = int(book_num_input)
        if book_num in library:
            print(f"Book number {book_num} is already taken. Please choose a different number.")
            continue
        
        book_name = input("plz enter the book's name: ").strip()
        book_author = input("plz enter the book's author: ").strip()
        book_status = input("plz enter the book's status: (ava/bor)").strip().lower()
        if book_status not in ["ava", "bor"]:
            print("Invalid status! Enter 'ava' for available or 'bor' for borrowed.")
            continue
        
        library[book_num] = {"bookname": book_name, "bookauthor": book_author, "bookstatus": book_status}
        print(f"Book '{book_name}' successfully added to the library!")
        
        choice = input("Do you want to add another book? if you want to exist press (E), if you don't press any botton to continue. ")
        if choice.lower() == "e":
            break    
    save_library(library)

def display_library(library):
    for key1, value1 in library.items():
        print(f"Book number: {key1}")
        for key2, value2 in value1.items():
            print(f"{key2.capitalize()}: {value2}")
        print()

def delete_book(library, n):
    if n in library:
        n = str(n)
        del library[n]
    else:
        print("This book doesn't exist at the library.")
    save_library(library)

def borrow_book(library, n):
    n = str(n)
    if n in library:    
        if list(library[n].values())[-1] == "ava":
            library[n]["bookstatus"] = "bor"
            print("You borrowed this book successfully")
        else:
            print("You can't borrow this book it's already borrowed.")
    else:
        print("This book doesn't exist at the library.")
    save_library(library)
    
def restore_book(library, n):
    n = str(n)
    if n in library:    
        if list(library[n].values())[-1] == "bor":
            library[n]["bookstatus"] = "ava"
            print("You returned this book successfully.")
        else:
            print("this book is already here.")
    else:
        print("This book doesn't exist at the library.")
    save_library(library)
        
def main():
    My_Library = load_library()  
    while True:
        func = input("1: Display -- 2: Add -- 3:Borrow -- 4: Return -- 5: Delete\nPress (E) to Exit")
        if func == "1":
            display_library(My_Library)
        elif func == "2":
            add_book(My_Library)
        elif func == "3":
            borrow_book(My_Library, int(input("Plz enter the number of book you want to borrow: ")))
        elif func == "4":
            restore_book(My_Library, int(input("Plz enter the number of book you want to restore: ")))
        elif func == "5":
            delete_book(My_Library, int(input("Plz enter the number of book you want to delete: ")))
        elif func.lower() == "e":
            break
        else:
            print("Invalid choice!")
        
main()