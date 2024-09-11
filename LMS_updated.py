import datetime
from tabulate import tabulate
""" This class keep records of books in library.
    It has total four modules: "Display available books", "Add new books", "Borrow books", "Return books" """

class LMS:
    
    library_data= {
        "list_of_books":['Gamperaliya',
                        "Harry Potter and the Sorcerer's Stone",
                        'Beddegama',
                        'Eda Heladiwa',
                        'The Jungle book',
                        'The Science of Intersteller',
                        'A Game of Thrones',
                        'The Lord of The Rings',
                        'The Hobit',
                        'Abha Yaluwo',
                        'Magul kema'
                         ],
        "ISBN_no": [
                    '978-9558415436',
                    '***-0590353403',
                    '978-9552100336',
                    '978-9552102233',
                    '978-1684120321',
                    '978-1783293698',
                    '978-0553593716',
                    '978-0544003415',
                    '978-0547928227',
                    '978-9155573058',
                    '955-21-0106-9'
                     ],
        "Authors": [
                    'Martin Wickramasinghe',  
                    'J.K. Rowling',           
                    'Leonard Wolf',          
                    'David Karunaratne',      
                    'Rudyard Kipling',        
                    'Greg Keyes',             
                    'R. R. Martin',           
                    'J.R.R. Tolkien',    
                    'J.R.R. Tolkien',
                    'T B Ilangarathne',
                    'Kumarathunga Munidasa',
                    ], 
    }
    
    def __init__ (self, library_name):
        self.library_name = library_name
        self.books_dict = {}
        id = 10

        for books, authors, isbns in zip(self.library_data["list_of_books"], self.library_data["Authors"], self.library_data["ISBN_no"]):
            self.books_dict.update({str(id):{
                "books_title":books,
                "authors" : authors,
                "ISBNs" : isbns,
                "lender_name": "",
                "issue_date":"",
                "status":"Available"
                }})
            id += 1
                


# this part shows the books table.
    def display_books(self):
        book_table= [['Book_id', 'ISBN_NO', 'Title', 'Author', 'status']]
        for key, value in self.books_dict.items():
            book_table.append([key, value['ISBNs'], value['books_title'], value['authors'],  value['status']])
        print("-----------------------------------List of Books-------------------------------------------------")
        print(tabulate(book_table, headers="firstrow", tablefmt="fancy_grid"))
                

#borrow books and update status
    def Borrow_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"] == "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['issue_date']} ")
                return self.Borrow_books()
            #{if book is available ,get the user information and realese book}
            elif self.books_dict[books_id]['status'] == "Available":  
                Your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = Your_name
                self.books_dict[books_id]['issue_date'] = current_date
                # {update status}
                self.books_dict[books_id]['status'] = "Borrowed !" 
                print("Books issued sucessfully !:)\n")
        else:
            print("Book ID not found !")
            return self.Borrow_books()

#Add new books ,get the book's informations from user    
    def add_new_books(self):
        new_books = input("Enter books title: ")
        new_author = input("Enter the author name: ")
        new_ISBN = input("Enter the ISBN No: ")
        if new_books == "":
            return self.add_new_books()
        elif len(new_books) > 30:
            print("Books title is too long!! Title length should be 25 charactors")
            return self.add_new_books
        # put the information in to tha tables
        else: 
            self.books_dict.update({str(int(max(self.books_dict))+1)
                                        : {'books_title':new_books,
                                           'authors' : new_author,
                                           'ISBNs' : new_ISBN,
                                           'lender_name':"", 
                                           'issu_date':"",
                                           'status':"Available"}})
            print(f"This book '{new_books}' has been added successfully !!")
                 
#Return books
    def return_books(self):
        books_id = input("Enter books ID:")
        #check the status of book
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == "Available":
                print("This book is alredy available in library.Please check yur book ID.")
                return self.return_books()
            #recive the book and update ststus
            elif not self.books_dict[books_id]['status'] == "Available":
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['issue_date'] = ""
                self.books_dict[books_id]['status'] = "Available"
                print("Successfully Returned ! \nThank you come again ! \n")

        else:
            print("Book ID is not found")

#interact with users and get inputs
try:
    myLMS = LMS("python's")
    press_key_list = {"D": "Display Books", "B": "Borrow_books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n----------------Welcome to {myLMS.library_name} Library Management System----------------------\n")
        for key, value in press_key_list.items():
            print("press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "b":
            print("\nCurrent Selection : Borrow books\n")
            myLMS.Borrow_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Books\n")
            myLMS.add_new_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print(f"Something went wrong.Please check your input ! \nError:{e}")
    
