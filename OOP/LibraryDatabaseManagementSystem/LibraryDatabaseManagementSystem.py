# Name : 柯玲萱 Cara
# ID: 10890021

import sqlite3

from BookClass import Book
from AuthorClass import Author
from PublisherClass import Publisher
from BorrowerClass import Borrower



class LibrarySystem:

    def __init__(self):
        self.conn = sqlite3.connect('Library.DB')
        self.cursor = self.conn.cursor()
        self.conn.commit()
    
    def Connect_To_DB(self):
        self.conn = sqlite3.connect("Library.DB")
        self.cursor = self.conn.cursor()
        return self.conn
    
    # Create Table
    def Create_Table(self):
        try:
            conn = self.Connect_To_DB()
            conn.execute("""
                CREATE TABLE Book(
                    ISBN  TXT PRIMARY KEY NOT NUll,
                    title TXT NOT NULL,
                    author TXT NOT NULL, 
                    publisher TXT NOT NULL,
                    publicationDate DATE 
                );
            """)

            conn.execute("""

                CREATE TABLE  Author (
                    name  TXT  NOT NUll,
                    birthDate DATE,
                    countryOfOrigin TXT NOT NULL,
                    PRIMARY KEY (name, birthDate, countryOfOrigin)

                );
            """)   
            conn.execute("""
                CREATE TABLE Publisher(
                    name TXT  NOT NUll,
                    address TXT NOT NULL,
                    country TXT NOT NULL,
                    PRIMARY KEY (name, address)

                );

            """)
            conn.execute("""
                CREATE TABLE  Borrower(
                    email  TXT  PRIMARY KEY NOT NUll,
                    name TXT NOT NULL,
                    contactNumber TXT NOT NULL
                );
                
            """)   


            conn.commit()
            print("Table is created successfully!")
        except:
            print("Table is not created yet, errors occurred!")
        finally:
            conn.close

    # Insert Book
    def Insert_Book(self,book):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO Book VALUES(:ISBN, :title, :author, :publisher, :publicationDate)
                """,{
                    "ISBN": book.ISBN,
                    "title": book.title,
                    "author":book.author,
                    "publisher": book.publisher,
                    "publicationDate": book.publicationDate
            }
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Update Book
    def Update_Book(self, New_ISBN, New_title, New_author, New_publisher, New_publicationDate, Old_ISBN):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Book SET ISBN=?, title=?, author=?, publisher=?, publicationDate=? WHERE ISBN=?",
                (New_ISBN, New_title, New_author, New_publisher, New_publicationDate, Old_ISBN)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Delete Book
    def Delete_Book(self,ISBN):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Book WHERE ISBN=?",
                (ISBN)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Get Books
    def Get_Books(self):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM Book"
            )
            All_Books = cur.fetchall()
            print("Get all books")
            for row in All_Books:
                print(row)
            conn.commit()

        except:
            conn.rollback()
        finally:
            conn.close()
    

    # Insert Author
    def Insert_Author(self,author):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                """
                  INSERT INTO Author VALUES(:name, :birthDate, :countryOfOrigin)
                """,{
                    "name": author.name,
                    "birthDate": author.birthDate,
                    "countryOfOrigin":author.countryOfOrigin
                }
            
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
    
     # Update Author
    def Update_Author(self, New_name, New_birthDate, New_countryOfOrigin,Old_name,Old_birthDate,Old_countryOfOrigin):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Author SET name=?, birthDate=?, countryOfOrigin=? WHERE name=? AND birthDate=? AND countryOfOrigin = ?",
                (New_name, New_birthDate, New_countryOfOrigin,Old_name,Old_birthDate,Old_countryOfOrigin)
            )
            conn.commit() 
        except:
            conn.rollback()
        finally:
            conn.close()

    # Delete Author
    def Delete_Author(self,name,birthDate,countryOfOrigin):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Author WHERE name=? AND birthDate=? AND countryOfOrigin = ?",
                (name, birthDate,countryOfOrigin)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Get Authors
    def Get_Authors(self):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM Author"
            )
            All_Authors = cur.fetchall()
            print("Get all authors")
            for row in All_Authors:
                print(row)
            conn.commit()

        except:
            conn.rollback()
        finally:
            conn.close()

    # Insert Publisher
    def Insert_Publisher(self,publisher):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
               """
               INSERT INTO Publisher VALUES(:name, :address, :country)
               """,{
                    "name": publisher.name,
                    "address": publisher.address,
                    "country":publisher.country
                }
            
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
    
     # Update Publisher
    def Update_Publisher(self, New_name, New_address, New_country,Old_name,Old_address):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Publisher SET name=?, address=?, country=? WHERE name=? AND address=?",
                (New_name, New_address, New_country,Old_name,Old_address)
            )
            conn.commit() 
        except:
            conn.rollback()
        finally:
            conn.close()

    # Delete Publisher
    def Delete_Publisher(self,name,address):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Publisher WHERE name=? AND address=?",
                (name, address)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Get Publishers
    def Get_Publishers(self):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM Publisher"
            )
            All_Publishers = cur.fetchall()
            print("Get all publishers")
            for row in All_Publishers:
                print(row)
            conn.commit()

        except:
            conn.rollback()
        finally:
            conn.close()
    
    # Insert Borrower
    def Insert_Borrower(self,borrower):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO Borrower VALUES(:email, :name, :contactNumber)
                """,{
                    "email": borrower.email,
                    "name": borrower.name,
                    "contactNumber":borrower.contactNumber
                }
            
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()
    
     # Update Borrower
    def Update_Borrower(self, New_email, New_name, New_contactNumber,Old_email):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Borrower SET email=?, name=?, contactNumber=? WHERE email=?",
                (New_email, New_name, New_contactNumber,Old_email)
            )
            conn.commit() 
        except:
            conn.rollback()
        finally:
            conn.close()

    # Delete Borrower
    def Delete_Borrower(self,email):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Borrower WHERE email=?",
                (email)
            )
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

    # Get Borrower
    def Get_Borrowers(self):
        try:
            conn = self.Connect_To_DB()
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM Borrower"
            )
            All_Borrowers = cur.fetchall()
            print("Get all borrowers")
            for row in All_Borrowers:
                print(row)
            conn.commit()

        except:
            conn.rollback()
        finally:
            conn.close()

    def choice(self):
        
        while True:
            print('--- Library Management System ---')
            print('0. Exit')
            print('1. Insert book')
            print('2. Update book')
            print('3. Delete book')
            print('4. Get books')
            print('5. Insert author')
            print('6. Update author')
            print('7. Delete author')
            print('8. Get authors')
            print('9. Insert publisher')
            print('10. Update publisher')
            print('11. Delete publisher')
            print('12. Get publishers')
            print('13. Insert borrowers')
            print('14. Update borrowers')
            print('15. Delete borrowesr')
            print('16. Get borrowers')

            choice = input('Enter your choice: ')
            if choice == "0":
                print("ByeBye")
                break
            elif choice == '1':
                ISBN = input('Enter the ISBN number: ')
                title = input('Enter the book title: ')
                author = input('Enter the author: ')
                publisher = input('Enter the publisher: ')
                publicationDate = input('Enter the publication date: ')
                book = Book(ISBN,title, author, publisher, publicationDate)
                Library.Insert_Book(book)
                pass
            elif choice == "2":
                Old_ISBN = input('Enter the ISBN number of the book you want to update : ')
                New_ISBN = input('Enter the New ISBN number: ')
                New_title = input('Enter the New title: ')
                New_author = input('Enter the New author: ')
                New_publisher = input('Enter the New publisher: ')
                New_publicationDate = input('Enter the New publication date: ')
                Library.Update_Book(New_ISBN,New_title,New_author,New_publisher,New_publicationDate,Old_ISBN)
                pass
            elif choice == "3":
                Delete_ISBN = input("Enter the ISBN number of the book you want to delete :")
                Library.Delete_Book(Delete_ISBN)
                pass
            elif choice == "4":
                Library.Get_Books()
                pass
            elif choice == "5":
                name = input("Enter the author name:")
                birthDate = input("Enter the author birthDate:")
                countryOfOrigin = input("Enter the author countryOfOrigin:")
                author = Author(name,birthDate,countryOfOrigin)
                Library.Insert_Author(author)
                pass
            elif choice == "6":
                Old_name = input('Enter the name of the author you want to update : ')
                Old_birthDate = input('Enter the birthDate of the author you want to update : ')
                Old_countryOfOrigin = input("Enter the ountryOfOrigin of the author you want to update")
                New_name = input('Enter the New name: ')
                New_birthDate = input('Enter the New birthDate: ')
                New_countryOfOrigin = input('Enter the New countryOfOrigin: ')
                Library.Update_Author(New_name,New_birthDate,New_countryOfOrigin,Old_name,Old_birthDate,Old_countryOfOrigin)
                pass
            elif choice == "7":
                Delete_name = input("Enter the name of the author you want to delete :")
                Delete_birthDate = input('Enter the birthDate of the author you want to delete : ')
                Delete_countryOfOrigin =  input('Enter the countryOfOrigin of the author you want to delete : ')
                Library.Delete_Author(Delete_name,Delete_birthDate,Delete_countryOfOrigin)
                pass
            elif choice == "8":
                Library.Get_Authors()
                pass
            elif choice == "9":
                name = input("Enter the publisher name:")
                address = input("Enter the publisher address:")
                country = input("Enter the publisher country:")
                publisher = Publisher(name,address,country)
                Library.Insert_Publisher(publisher)
                pass
            elif choice == "10":
                Old_name = input('Enter the name of the publisher you want to update : ')
                Old_address = input('Enter the address of the publisher you want to update : ')
                New_name = input('Enter the New name: ')
                New_birthDate = input('Enter the New address: ')
                New_countryOfOrigin = input('Enter the New country: ')
                Library.Update_Publisher(New_name,New_birthDate,New_countryOfOrigin,Old_name,Old_address)
                pass
            elif choice == "11":
                Delete_name = input("Enter the name of the publisher you want to delete :")
                Delete_address = input('Enter the address of the publisher you want to delete : ')
                Library.Delete_Publisher(Delete_name,Delete_address)
                pass
            elif choice == "12":
                Library.Get_Publishers()
                pass
            elif choice == "13":
                email = input("Enter the borrower email:")
                name = input("Enter the borrower name:")
                contactNumber = input("Enter the borrower contactNumber:")
                borrower = Borrower(email,name,contactNumber)
                Library.Insert_Borrower(borrower)
                pass
            elif choice == "14":
                Old_email = input('Enter the email of the borrower you want to update : ')
                New_email = input('Enter the New email: ')
                New_name = input('Enter the New name: ')
                New_contactNumber = input('Enter the New contactNumber: ')
                Library.Update_Borrower(New_email,New_name,New_contactNumber,Old_email)
                pass
            elif choice == "15":
                Delete_email = input("'Enter the email of the borrower you want to delete :")
                Library.Delete_Borrower(Delete_email)
                pass
            elif choice =="16":
                Library.Get_Borrowers()
                pass
            






if __name__ == "__main__":
    Library = LibrarySystem()
    Library.Create_Table()
    Library.choice()
    


    
