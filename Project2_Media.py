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

Miguel Zavala:

'''

# Check README.md file for PSA and personal comments


# overarching media class, parent for classes Book and Video
class Media:

    checked_out = []

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher


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
        pass

    def checkIn(self):
        pass

    def printCheckedOutItems(self):
        print(self.has_books)


# this is the test case, type test conditions in this function
# and leave this function at the bottom of the file. change as
# desired for personal unit tests
if __name__ == "__main__":
    gary = Member("Gary")
    for member in Member.members:
        print(member.name)
