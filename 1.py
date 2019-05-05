# Media is a superclass of Books class and Video class.
class Media:

    # Common attributes of Video and Books are:title,author,publisher.
    title = ""
    author = ""
    publisher = ""

    # Following 4 methods are common methods of Books and Video.
    # To initialize the attributes
    def setAttr(self, a, b, c):
        Media.title = a
        Media.author = b
        Media.publisher = c

    # To return the value of attributes
    def getTitle(self):
        return Media.title

    def getAuthor(self):
        return Media.author

    def getPublisher(self):
        return Media.publisher


# Subclass Books.
class Books(Media):

    # Specific attributes of Books.
    pages = ""
    book_count = 0
    check_book = 0
    # The dictionary b is used to store all book details available in the library.
    b = {}

    # To initialize Books instance with attribute of Books.
    def __init__(self, x, y, z, w):
        self.setAttr(x, y, z)
        self.pages = w
        # key is the key of dictionary b for book of title x.
        key = x
        # value is the information of other attributes which are stored into b as value field.
        value = "Author = %s" % y + " Publisher = %s" % z + " No of pages = %s" % w
        Books.b[key] = value
        # To calculate number of books.
        Books.book_count += 1
        self.check_book = 0

    # To print the book details using print.
    def __repr__(self):
        return 'Book name = %s, Book author = %s, Book Publisher = %s, Total pages =%s' % \
               (self.getTitle(), self.getAuthor(), self.getPublisher(), self.pages)


# Subclass Video.
class Video(Media):

    # Specific attributes of Video.
    track_time = ""
    video_count = 0
    # The dictionary v is used to store all video details available in the library.
    v = {}
    check_video = 0

    # To initialize Video instance with attribute of Video.
    def __init__(self, m, n, o, p):
        self.setAttr(m, n, o)
        self.track_time = p
        Video.video_count += 1
        # key1 is the key of dictionary v for video of title m.
        key1 = m
        # value1 is the information of other attributes which are stored into v as value field.
        value1 = "Author = %s" % n + " Publisher = %s" % o + " Total time = %s" % p
        Video.v[key1] = value1
        check_video = 0

    # To print the video details using print.
    def __repr__(self):
        return 'Video name = %s, Video author = %s, Video Publisher = %s, Total time =%s' % \
               (self.getTitle(), self.getAuthor(), self.getPublisher(), self.track_time)


# Standalone Member class.
class Member:

    # Attributes of Member.
    name = ""
    check_count = 0
    # The dictionary m is used to store member name with check out details.
    m = {}
    # The dictionary r is used to store member name with check in details.
    r = {}

    # To initialize Member instance with attributes.
    def __init__(self, name):
        self.name = name

    # Function to operate check out and insert the details of check out to m with member name.
    def CheckOutBook(self, *argv):  # *argv allows the user to pass as many number of attributes as she wants.
        count = len(argv)  # counts number of books passed as arguments through argv.

        if count > 2:  # As mamber can't check out more than 2 books at a time.
            print("\nSorry you cannot check out book more that 2...")
        else:
            for i in argv:  # i indicates book title.
                val = Books.b.get(i,
                                  'none')  # get() returns the values of key i if i is found in b else return the next parameter of get().
                if val == 'none':
                    print("\nThere is no such book in the library...")
                else:
                    key2 = self.name  # key2 stores name of the member.
                    value2 = val
                    Member.m[key2] = Member.m.get(key2, ' ') + value2  # Add new checkout details along with previous details.
                    del Books.b[i]  # as the book of title is checked out delete it from the available books in b.

    # Function to operate check in.
    def CheckInBook(self, e):  # e is the title of the book.
        if e == Books.title:
            # value4 is the details of the book checked in.
            value4 = "Author = %s" % Books.author + " Publisher = %s" % Books.publisher + " Total pages = %s" % Books.pages
            # Add the book to the dictionary b to indicate that it is available again.
            Books.b[e] = value4
            Member.r[self.name] = Member.r.get(self.name, ' ') + value4  # Add new checkin details along with previous #details.
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
                val1 = Video.v.get(j, 'none')
                if val1 == 'none':
                    print("\nThere is no such video in the library...")
                else:
                    key3 = self.name
                    value3 = val1
                    Member.m[key3] = Member.m.get(key3, ' ') + value3
                    del Video.v[j]

    # Function to operate check in video.
    def CheckInVideo(self, f):  # f is the title of the video.
        if f == Video.title:
            value5 = "Author = %s" % Video.author + " Publisher = %s" % Video.publisher + " Total time = %s" % Video.track_time  # value5 stores details of the video.
            Video.v[f] = value5
            Member.r[self.name] = Member.r.get(self.name, ' ') + value5  ##Add new checkin details along with previous #details.
        else:
            print("\nInvalid video..")



#To create and print instance of Books.
print("\nDetails of every book....:")
book1 = Books("Programming", "Schild", "Pigeon", "500")
print(book1)
book2 = Books("Database", "Korth", "FamousPublisher", "1022")
print(book2)
book3 = Books("Networking", "Forouzan", "PPP", "1140")
print(book3)
print("\nTotal Books available %s " % Books.book_count)

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
print(Member.m)
print("\nAfter checkout book details available in the library:")
print(Books.b)
print("\nAfter check out video details available in the library:")
print(Video.v)
print("\nCheck out details of member %s:" % member1.name)
print(Member.m.get(member1.name, 'No check out today')) #get () Returns the check out details of the key #member1.name.If the key is not found print No check out today
print("\nCheck out details of member %s:" % member2.name)
print(Member.m.get(member2.name, 'No check out today')) #get() Returns the check out details of the key #member2.name.If the key is not found print No check out today

#check in.
member2.CheckInVideo("Songs")
#To print Check in details and statictics.
print("\nAfter check in available video in the library:")
print(Video.v)
print("\nAfter check in available books in the library:")
print(Books.b)
print("\nCheck In details of member %s:" % member1.name)
print(Member.r.get(member1.name, 'No check In today'))  #get() Returns the check in details of the key member1.name.If the key is not found print No check In today
print("\nCheck In details of member %s:" % member2.name)
print(Member.r.get(member2.name, 'No check In today'))  #get() Returns the check in details of the key member2.name.If the key is #not found print No check In today
