import time
while True:
    books = ["the brief history of time", "space: a wonder", "dr.apj abdul kalam biography", "mahabharata",
             "panchtantra", "rich dad poor dad", "the secretes of bermuda", "alpine: a place of terror"]
    lendbooks = {}
    print("Welcome to the world of books")
    User = input("please enter your name\t")
    while True:
        input("Press enter to proceed")
        work = input("What do you want to do\n1.VIEW BOOKS\n2.LEND A BOOK\n3.DONATE BOOK\n4.RETURN A BOOK"
                     "\n5.VIEW YOUR DETAILS\nNOTE: if you want to exit please write exit\n")


        class Library:
            def __init__(self,name):
                self.name = name
                try:
                    infofile = open(f"{name}info.txt", "x")
                    infofile.write(f"This is the personal space of {name}")

                except Exception as already:
                    pass
                fileread = open(f"{self.name}info.txt", "r")
                self.fileread = fileread.read()

            def view_books(self):
                print("\nthe books we have:-\n")
                for book in books:
                    print(book)
                    time.sleep(1)

            def lend_book(self, bookname):
                file = open(f"{self.name}info.txt", "a")
                if bookname in books:
                    if bookname in lendbooks:
                            print(f"{bookname} book is currently lended by {lendbooks[bookname]}")
                    else:
                        file.write(f"\n{bookname}----{time.asctime()}====>LENDED")
                        lendbooks.update({bookname: self.name})
                        print("your book is successfully issued")
                else:
                    print("this book is currently not available")


            def donate_book(self,bookname):
                file = open(f"{self.name}info.txt", "a")
                if bookname in books:
                    print("thankyou for donating")
                else:
                    file.write(f"\n{bookname}----{time.asctime()}====>DONATED")
                    books.append(bookname)
                    print("thankyou for donating")


            def return_book(self,bookname):
                file = open(f"{self.name}info.txt", "a")
                if bookname in lendbooks:
                    del lendbooks[bookname]
                    file.write(f"\n{bookname}----{time.asctime()}====>RETURNED")
                    print(f"you successfully returned {bookname} book")
                else:
                    print("this books is not in our record, please check the spelling and try again")


        user = Library(User)

        if work == "1":
            user.view_books()
        elif work=="2":
            lendbook = input("please write the book's name\t")
            user.lend_book(lendbook)
        elif work=="3":
            donatebook = input("please write the book's name\t")
            user.donate_book(donatebook)
        elif work == "4":
            returnbook = input("please write the book's name\t")
            user.return_book(returnbook)
        elif work=="5":
            print(user.fileread)
        elif work=="exit":
            print("thankyou for using our service")
            break
        else:
            print("please choose one option given above")




