import json
My_Library = {
    # 1: {"bookname": "Love and War", "bookauthor": "unknown", "bookstatus": "bor"},
    # 2: {"bookname": "Death", "bookauthor": "killer", "bookstatus": "ava"},
    # 3: {"bookname": "How to play", "bookauthor": "warrior", "bookstatus": "ava"}
}

def load_library():
    try:
        with open("my_library", "r") as file:
            

def save_library(library):
    with open("my_libray.txt" , "w") as file:
        x = []
        for key1, value1 in library.items():
            x.append(key1)
            for key2, value2 in value1.items():
                x.append(key2)
                x.append(value2)
        # print(str(x).strip())
        file.write(str(x).strip())
        
def add_book(library):
    
    while True:
        book_num = int(input("plz enter the book's number: "))
        book_name = input("plz enter the book's name: ")
        book_author = input("plz enter the book's author: ")
        book_status = input("plz enter the book's status: (ava/bor)")
        choice = input("Do you want to add another book? if you want to exist press (n), if you don't press any botton to continue")
        
        library[book_num] = {"bookname": book_name, "bookauthor": book_author, "bookstatus": book_status}
        
        if choice.lower() == "n":
            break
        
    return library

def display_library(library):
    for i, j in library.items():
        print(f"Book number: {i}")
        for key, value in j.items():
            print(f"{key.capitalize()}: {value}")
        print()

def delete_book(library, n):
    del library[n]
    

# delete_book(My_Library, 2)
save_library(My_Library)
print(My_Library)