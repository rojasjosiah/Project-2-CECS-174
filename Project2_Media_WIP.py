### Slowly tweaking the code to make it what we want ### - PR




# Media is a superclass of Books class and Video class.
class Media:

    # Common attributes of Video and Books are:title,author,publisher.
    title = ""
    author = ""
    publisher = ""

    # Following 4 methods are common methods of Books and Video.
    # To initialize the attributes
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    # To return the value of attributes
    def getTitle(self):
        return Media.title

    def getAuthor(self):
        return Media.author

    def getPublisher(self):
        return Media.publisher


# Subclass Books.
class Book(Media):
    # Specific attributes of Books.
    pages = ""
    book_count = 0
    check_book = 0
    # The dictionary b is used to store all book details available in the library.
    book_dict = {}

    # To initialize Books instance with attribute of Books.
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)
        self.num_pages = num_pages
        # value is the information of other attributes which are stored into book_dict as value field.
        value = "Author = %s" % author + " Publisher = %s" % publisher + " No of pages = %s" % num_pages
        Book.book_dict[title] = value
        # To calculate number of books.
        Book.book_count += 1
        self.check_book = 0

    # To print the book details using print.
    def __repr__(self):
        return 'Book name = %s, Book author = %s, Book Publisher = %s, Total pages =%s' % \
               (self.getTitle(), self.getAuthor(), self.getPublisher(), self.num_pages)


# Subclass Video.
class Video(Media):
    # Specific attributes of Video.
    run_time = ""
    video_count = 0
    # The dictionary v is used to store all video details available in the library.
    video_dict = {}
    check_video = 0

    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)
        self.run_time = run_time
        Video.video_count += 1
        # value1 is the information of other attributes which are stored into v as value field.
        value1 = "Author = %s" % author + " Publisher = %s" % publisher + " Total time = %s" % run_time
        Video.video_dict[title] = value1
        check_video = 0

    # To print the video details using print.
    def __repr__(self):
        return 'Video name = %s, Video author = %s, Video Publisher = %s, Total time =%s' % \
               (self.getTitle(), self.getAuthor(), self.getPublisher(), self.run_time)


# Standalone Member class.
class Member:

    # Attributes of Member.
    name = ""
    check_count = 0
    # The dictionary m is used to store member name with check out details.
    check_out_dict = {}
    # The dictionary r is used to store member name with check in details.
    check_in_dict = {}

    #? member_count = 0

    # To initialize Member instance with attributes.
    def __init__(self, name):
        self.name = name
        #? Member.member_count += 1
        #? self.check_count = 0

    # Function to operate check out and insert the details of check out to m with member name.
    def CheckOutBook(self, *argv):  # *argv allows the user to pass as many number of attributes as she wants.
        count = len(argv)  # counts number of books passed as arguments through argv.
        if count > 2:  # As member can't check out more than 2 books at a time.
            print("\nSorry you cannot check out book more that 2...")
        else:
            for i in argv:  # i indicates book title.
                val = Book.book_dict.get(i, 'none')  # get() returns the values of key i if i is found in b else return the next parameter of get().
                if val == 'none':
                    print("\nThere is no such book in the library...")
                else:
                    key2 = self.name  # key2 stores name of the member.
                    value2 = val
                    Member.check_out_dict[key2] = Member.check_out_dict.get(key2, ' ') + value2  # Add new checkout details along with previous details.
                    del Book.book_dict[i]  # as the book of title is checked out delete it from the available books in b.

    # Function to operate check in.
    def CheckInBook(self, e):  # e is the title of the book.
        if e == Book.title:
            # value4 is the details of the book checked in.
            value4 = "Author = %s" % Book.author + " Publisher = %s" % Book.publisher + " Total pages = %s" % Book.pages
            # Add the book to the dictionary b to indicate that it is available again.
            Book.book_dict[e] = value4
            Member.check_in_dict[self.name] = Member.check_in_dict.get(self.name, ' ') + value4  # Add new checkin details along with previous #details.
        else:  # if book title e does not match.
            print("\nInvalid book...")

    # Function to operate check out video.
    # It does same operation as book check out function.
    def CheckOutVideo(self, *argv):
        count1 = len(argv)
        if count1 > 2:
            print("\nSorry you cannot check out video more that 2...")
        else:
            for j in argv:
                val1 = Video.video_dict.get(j, 'none')
                if val1 == 'none':
                    print("\nThere is no such video in the library...")
                else:
                    key3 = self.name
                    value3 = val1
                    Member.check_out_dict[key3] = Member.check_out_dict.get(key3, ' ') + value3
                    del Video.video_dict[j]

    # Function to operate check in video.
    def CheckInVideo(self, f):  # f is the title of the video.
        if f == Video.title:
            value5 = "Author = %s" % Video.author + " Publisher = %s" % Video.publisher + " Total time = %s" % Video.run_time  # value5 stores details of the video.
            Video.video_dict[f] = value5
            Member.check_in_dict[self.name] = Member.check_in_dict.get(self.name, ' ') + value5  ##Add new checkin details along with previous #details.
        else:
            print("\nInvalid video..")


def displayStats(self):
    print("******************************************")
    print("\nRecord of library:")
    print("\nTotal number of books = ", Book.book_count)
    print("\nNumber of books checked out = ", )
    print("\nTotal number of videos = ", Video.video_count)
    # print("\nTotal number of members = ", Member.member_count)?
    print("\n************************************************************************************")
    print("\nThe following items are checked out of the library:")




#To create and print instance of Books.
print("\nDetails of every book....:")
book1 = Book("Programming", "Schild", "Pigeon", "500")
print(book1)
book2 = Book("Database", "Korth", "FamousPublisher", "1022")
print(book2)
book3 = Book("Networking", "Forouzan", "PPP", "1140")
print(book3)
print("\nTotal Books available %s " % Book.book_count)

#To create and print instance of Video.
print("\nDetails of every video...:")
video1 = Video("Movies", "Mr. A", "Sun", "60 Minutes")
print(video1)
video2 = Video("Game", "AB", "YoYo", "30 Minutes")
print(video2)
video3 = Video("Songs", "Akon", "AlwaysSinging", "120 minutes")
print(video3)
print("\nTotal videos available %s " % Video.video_count)

#To create instance of Member.
member1 = Member("Tandrima")
member2 = Member("Akash")

#Check out.
member1.CheckOutBook("abc")
member2.CheckOutVideo("Songs")

#To print check out details and statistics.
print("\nTotal Check out Details with member with name:")
print(Member.check_out_dict)
print("\nAfter checkout book details available in the library:")
print(Book.book_dict)
print("\nAfter check out video details available in the library:")
print(Video.video_dict)
print("\nCheck out details of member %s:" % member1.name)
print(Member.check_out_dict.get(member1.name, 'No check out today')) #get () Returns the check out details of the key #member1.name.If the key is not found print No check out today
print("\nCheck out details of member %s:" % member2.name)
print(Member.check_out_dict.get(member2.name, 'No check out today')) #get() Returns the check out details of the key #member2.name.If the key is not found print No check out today

#check in.
member2.CheckInVideo("Songs")
#To print Check in details and statictics.
print("\nAfter check in available video in the library:")
print(Video.video_dict)
print("\nAfter check in available books in the library:")
print(Book.book_dict)
print("\nCheck In details of member %s:" % member1.name)
print(Member.check_in_dict.get(member1.name, 'No check In today'))  #get() Returns the check in details of the key member1.name.If the key is not found print No check In today
print("\nCheck In details of member %s:" % member2.name)
print(Member.check_in_dict.get(member2.name, 'No check In today'))  #get() Returns the check in details of the key member2.name.If the key is #not found print No check In today
