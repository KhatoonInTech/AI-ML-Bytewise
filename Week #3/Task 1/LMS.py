from typing import Any


class Book():
    """A simple representation of a book"""
    def __init__(self,title,author,pages):
        """Initialize the attributes"""
        self.title=title
        self.author=author
        self.pages=pages

#get methodes
    def get_title(self ) : 
        """get method for title attribute"""   
        return self.title.title()
    
    
    def get_author(self ) :
        """get method for author attribute"""       
        return self.author.title()
    
    
    def get_pages(self ) : 
        """get method for title attribute"""     
        return self.pages
    
# set methods
    def set_title(self,new_title):
     # Optional validation (e.g., check for minimum length)
        if len(new_title) < 2:
           print("Error: Title must be at least 2 characters long.")
           return  # Exit the method without updating

        self.title = new_title.title()

    def set_author(self,new_author) :
     # Optional validation (e.g., check for minimum length)
            if len(new_author) < 3:
              print("Error: Author's name must be at least 3 characters long.")
              return  # Exit the method without updating
            
     # Optional validation (e.g., check for minimum length and digits)
            
            if not all(char.isalpha() or char.isspace() for char in new_author):
                print("Error: Author's name can only has alphabets.")
                return # Exit the method without updating
            
            self.author=new_author.title()

    def set_pages(self,new_pages):
     # Optional validation (e.g., check for minimum pages)
        if new_pages<=1:
            print("Error: A book must have at least more than 1 pages .")
            return # Exit the method without updating
        
     # Optional validation (e.g., check for digits only)
        if not all(digit.isdigit() for digit in str(new_pages)):
            print("Error: Number of pages can only be a numeric value.")
            return # Exit the method without updating

        self.pages=new_pages

    # Reading duration Evaluation
    def readtime(self,speed):
        """Evaluating time required to read the book based on avg reading speed of user"""
        """This formula demands speed in page/minute units""" 
        time= self.pages/speed 
        return f"{time//60} hours {int(time)%60} minutes"

# Creating an instance from class Book        
mybook=Book("blood and oil","Bradley hopes",450)

#demonstrating get methods
print(f"\nMy book has following info:\nTitle:{mybook.get_title()}\nAuthor:{mybook.get_author()}\nNumber of Pages:{mybook.get_pages()}")

#demonstrating set methods
mybook.set_title("48 laws of power")
mybook.set_author("Robert greene")
mybook.set_pages(400)
print(f"\n\nMy book has following UPDATED info:\nTitle:{mybook.get_title()}\nAuthor:{mybook.get_author()}\nNumber of Pages:{mybook.get_pages()}")

#demonstrating reading time methods
print(f"\n\nI require {mybook.readtime(1/5)} to read {mybook.get_title()}.\n\n")    #user can read 1 page in 5 minutes

# Creating CHILD class from INHERITENCE 
class Ebook(Book):
    """A simple representation of a Ebook"""
    def __init__(self,title,author,pages,format):
       """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
       """
       super().__init__(title,author,pages)
       self.format=format

    # Overriding __str__ method
    def __str__(self):
    # Return a formatted string representation
       return f"Title: {self.get_title()}\nAuthor: {self.get_author()}\nNumber of Pages:{self.get_pages()}\nFormat:{self.format}"
    
#Creating instance of CHILD class
myEbook=Ebook("The prince","nichole michaewali",345,"pdf")

#demonstrating overriding of __str__ method
print(myEbook)
   