'''
Project 2 - Group 2
CECS 174 TuTh 12:30

Josiah Rojas: (Project Manager)
    - Created base class Media and sub classes Book and Video (4/25)
    - Contributed to comments of Media, Book, and Video classes (4/25)
    - added framework class Member and its basic methods w/o capabilities (4/28)
April Picato:

Philip Ramirez:

Ali Mourad:
    - Created method of adding/subtracting media to and from class Member
    - Contributed to comments of Members
Miguel Zavala:
    -Contributed to Program debugging (5/1)
    -Contributed to methods of the Member class (5/1)
    -Created method to display stats and contributed to it's print formatting (5/2)

'''

# Check README.md file for PSA and personal comments


# overarching media class, parent for classes Book and Video
class Media:

    checked_out = []

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

        # Method is used to add books/videos to be checked out
        # PS objects should be pass through here

    def addMedia(self):
        pass

        # Method is used to remove books/videos from library

    def removeMedia(self):
        pass


# class Book child of class Media, creates Book type for library
class Book(Media):
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.num_pages = num_pages


# class Video child of class Media, creates Video type for library
class Video(Media):
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.run_time = run_time


# Member class for library members, feel free to code in those check in/out methods
class Member:

    members = []

    def __init__(self, name):
        self.name = name
        # this is a temporary method I'm using to store which books have been checked out,
        # we may need to use a more global counter, so if you find a better slution feel
        # free to do that and delete this
        self.has_books = []
        self.members.append(self)

    # func to check out books
    def checkOut(self):
        # make sure to add the Media item to the Media.checked_out list for inventory purposes
        #I'm not sure if this line is correct but I think this is how to add the media to the checked_out list
        Media.checked_out.append(self)
        pass

    def checkIn(self):
        pass


    def printCheckedOutItems(self):
        print(self.has_books)
        
    
    
def displayStats(self):
    print("******************************************\n")
    print("Record of library:\n")
    print("Total number of books = \n") #add on the number of books
    print("Number of books checked out = \n")
    print("Total number of videos = \n")
    print("Total number of members = ", len(members))
    print("\n")
    print("\n************************************************************************************\n")
    print("The following items are checked out of the library:")
        #insert checked out items + stats


# this is the test case, type test conditions in this function
# and leave this function at the bottom of the file. change as
# desired for personal unit tests
if __name__ == "__main__":
    gary = Member("Gary")
    for member in Member.members:
        print(member.name)
