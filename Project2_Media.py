# Project2_Media

# Project Members: Josiah Rojas, April Picato, Philip Ramirez, Ali Mourad, Miguel Zavala

# Project 2 - Group 2
# CECS 174 TuTh 12:30
#
# Josiah Rojas: (Project Manager)
#     - Created base class Media and sub classes Book and Video
#     - Contributed to comments of Media, Book, and Video classes
#     - Added framework class Member and its basic methods
#     - Edited displayStats function
#     - Contributing to editing program for redundancy
#     - Contributed to bug fixing
# April Picato:
#     - Contributed to adding/removing media components
#     - Contributed to methods of the Book/ Video classes
#     - Contributed to methods of the Member class
#     - Contributed to displayStats with basic print statements for desired output
# Philip Ramirez:
#     - Contributed to __repr__method and Member class formatting
#     - Contributed to __init__ and created count for classes
#     - Contributed to checkIn/checkOut functions to match expected output
#     - Contributed to displayStates and overall output formatting
#     - Fixed member items handling
# Ali Mourad:
#     - Contributed to adding/removing media components
#     - Contributed to comments of all classes
#     - Contributed to methods of Media class
#     - Contributed to methods of book/video classes
#     - Created __repr__ method of all classes
# Miguel Zavala:
#     - Contributed to Program debugging
#     - Contributed to methods of the Member class
#     - Created method to display stats and contributed to its print formatting
#     - Edited displayStats function


# overarching media class, parent for classes Book and Video
class Media:
    library = []
    # checked_out made dict to track who has the media
    checked_out = {}

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        Media.addMedia(self)

        # Method is used to add books/videos to be checked out
        # PS objects should be pass through here

    def addMedia(self):
        Media.library.append(self)

    # Method is used to remove books/videos from library
    # if no media exists then prints that
    def removeMedia(self):
        if self in Media.library:
            Media.library.remove(self)
            self.count -= 1
        else:
            print('Media does not exist')


# class Book child of class Media, creates Book type for library
class Book(Media):
    # keeps track of how many total books exist
    count = 0

    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.num_pages = num_pages
        Book.count += 1
        # changed to descr so wouldn't have to know type of media to use
        self.descr = "Author: %s, Publisher: %s, Number of Pages: %d" % (author, publisher, num_pages)

    # Used to represent class object as their attributes instead of memory location
    def __repr__(self):
        return "Book--> {} written by {}".format(self.title, self.author)


# class Video child of class Media, creates Video type for library
class Video(Media):
    count = 0

    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.run_time = "{} mins video".format(run_time)
        Video.count += 1
        self.descr = "Author: %s, Publisher: %s, Run time: %d minutes" % (author, publisher, run_time)

    # Used to represent class object as their attributes instead of memory location
    def __repr__(self):
        return "Video--> {} {} created by {}".format(self.run_time, self.title, self.author)


# Member class for library members, feel free to code in those check in/out methods
class Member:
    members = []
    
    def __init__(self, name):
        self.name = name
        self.members.append(self)
        self.items_out = []

    # Allows for representation of the object by a string
    def __repr__(self):
        return "{}".format(self.name)

    # func to check out media
    # Passes objects from Media through Members
    def checkOut(self, a_media):
        max_out = 2
        if a_media in Media.checked_out:
            print("Sorry {}, {} is not available, checked out by {}".format(self, a_media, Media.checked_out[a_media]))
        elif a_media in Media.library:
            if len(self.items_out) < max_out:
                Media.checked_out[a_media] = self
                self.items_out.append(a_media)
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
            # removes from checked_out dict and items_out list
            del Media.checked_out[a_media]
            self.items_out.remove(a_media)
            print(self, "checked in:", a_media)

    def printCheckedOutItems(self):
        print("Items checked out by {}:".format(self))
        # prints out each item checked out
        if len(self.items_out) > 0:
            for i in range(len(self.items_out)):
                print('\t', self.items_out[i])
        else:
            print("\t No items checked out.")


def displayStats():
    print("******************************************")
    print("Record of library:")
    print("Total number of books:", Book.count)
    print("Number of books checked out:", len(Media.checked_out))
    print("Total number of videos:", Video.count)
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
    Jim.printCheckedOutItems()

    Joe.checkOut(video1)
    Joe.checkIn(book1)
    
    Jim.checkOut(book2)
    Joe.checkIn(book2)
    
    Jim.checkOut(video1)
    Jim.checkOut(book1)
    
    displayStats()

