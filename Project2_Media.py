'''
Project 2 - Group 2
CECS 174 TuTh 12:30

Josiah Rojas: (Project Manager)
    - Created base class Media and sub classes Book and Video (4/25)
    - Contributed to comments of Media, Book, and Video classes (4/25)
    - added framework class Member and its basic methods w/o capabilities (4/28)
    - Edited displayStats function (5/5)
    - Contributing to editing program for redundancy (5/5)
April Picato:
    - Contributed to adding/removing media components
    - Contributed to methods od the Book/ Video classes
    - Contributed to methods of the Member class 
    - Contributed to displayStats with basic print statements for desired output
Philip Ramirez:
    - Contributed to __repr__method for classes
    - Contributed to __init__ and created count for classes
    - Contributed to checkIn/checkOut functions to match expected output
    - Contributed to displayStates to match desired output

Ali Mourad:
    - Created method of adding/subtracting media to and from class Member
    - Contributed to comments of Members/ Media/ Book/ Video
    - Created __repr__ method for all cl
    - Contributed to debugging of entire code
Miguel Zavala:
    - Contributed to Program debugging (5/1)
    - Contributed to methods of the Member class (5/1)
    - Created method to display stats and contributed to its print formatting (5/2)
    - Edited displayStats function(5/6)

'''

# Check README.md file for PSA and personal comments


# overarching media class, parent for classes Book and Video
class Media:
    library = []
    checked_out = []

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        Media.addMedia(self)

        # Method is used to add books/videos to be checked out
        # PS objects should be pass through here

    # Multiple of the same media may be added to the library, such as multiple of the same book
    def addMedia(self):
        Media.library.append(self)

    # Method is used to remove books/videos from library
    # Removing a media removes 1 copy of that media
    # if no other copy exists then the media is completely removed from library

    def removeMedia(self):
        if self in Media.library:
            Media.library.remove(self)
        else:
            print('Media does not exist')


# class Book child of class Media, creates Book type for library
class Book(Media):
    book_count = 0

    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.num_pages = num_pages
        Book.book_count += 1
        # changed to descr so wouldn't have to know type of media to use
        self.descr = "Author: %s, Publisher: %s, Number of Pages: %d" % (author, publisher, num_pages)

    # Used to represent class object as their attributes instead of memory location
    def __repr__(self):
        return "Book--> {} written by {}".format(self.title, self.author)


# class Video child of class Media, creates Video type for library
class Video(Media):
    video_count = 0

    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.run_time = "{} mins video".format(run_time)
        Video.video_count += 1
        self.descr = "Author: %s, Publisher: %s, Run time: %d minutes" % (author, publisher, run_time)

    # Used to represent class object as their attributes instead of memory location
    def __repr__(self):
        return "Video--> {} {} created by {}".format(self.run_time, self.title, self.author)


# Member class for library members, feel free to code in those check in/out methods
class Member:
    members = []
    member_out = []

    def __init__(self, name):
        self.name = name
        # this is a temporary method I'm using to store which books have been checked out,
        # we may need to use a more global counter, so if you find a better solution feel
        # free to do that and delete this
        self.has_books = []
        self.members.append(self)

    # Allows for representation of the object by a string
    def __repr__(self):
        return "{}".format(self.name)

    # func to check out media
    # Passes objects from Media through Members
    def checkOut(self, a_media):
        max_out = 2
        if a_media in Media.checked_out:
            print("Sorry {}, {} is not available, checked out by {}".format(self, a_media, "?????"))
        elif a_media in Media.library:
            if len(Member.member_out) < max_out:
                Media.checked_out.append(a_media)
                Member.member_out.append(a_media)
                print(self, "has checked out:", a_media)
            else:
                print("{} has reached the maximum number ({}) of borrowed items, "
                      "so can't check out: {}".format(self, max_out, a_media))
        else:
            print('Media does not exist')

    def checkIn(self, a_media):
        if a_media not in Media.checked_out:
            print('Media not yet checked out')
        else:
            Media.checked_out.remove(a_media)
            Member.member_out.remove(a_media)
            print(self, "checked in:", a_media)

    def printCheckedOutItems(self):
        print("Items checked out by {}:".format(self))
        for i in range(len(Member.member_out)):
            print('\t', Member.member_out[i])


def displayStats():
    print("******************************************")
    print("Record of library:")
    print("Total number of books:", Book.book_count)
    print("Number of books checked out:", len(Media.checked_out))
    print("Total number of videos:", Video.video_count)
    print("Total number of members:", len(Member.members))
    print("******************************************")
    print("The following items are checked out of the library:", *Media.checked_out, sep='\n')
 


# this is the test case, type test conditions in this function
# and leave this function at the bottom of the file. change as
# desired for personal unit tests
if __name__ == "__main__":
    book1 = Book("Python for Beginners", "Unknown", "Pub?", 0)
    book2 = Book("Python for Kids", "Jason R. Briggs", "Pub?", 0)

    video1 = Video("Tom and Jerry", "W.Hannah, J.Barbara", "Pub?", 30)

    Joe = Member("Joe Smith")
    Jim = Member("Jim Stuart")

    Joe.checkOut(book1)
    Joe.checkOut(book2)

    Joe.printCheckedOutItems()
#     Jim.printCheckedOutItems()

    Joe.checkOut(video1)
    Joe.checkIn(book1)

    Jim.checkOut(book2)
    Joe.checkIn(book2)

    Jim.checkOut(video1)
    Jim.checkOut(book1)

    print(displayStats())
    
    
#     print(Media.checked_out)
#     print(Media.library)
#     print(Member.member_out)
#     print(Member.members)
