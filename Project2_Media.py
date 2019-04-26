'''
Project 2 - Group 2
CECS 174 TuTh 12:30

Josiah Rojas: (Project Manager)
    - Created base class Media and sub classes Book and Video
April Picato:

Philip Ramirez:

Ali Mourad:

Miguel Zavala:

'''

# Check README.md file for PSA and personal comments


# overarching media class, parent for classes Book and Video
class Media:
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


# this is the test case, type test conditions in this function
# and leave this function at the bottom of the file
if __name__ == "__main__":
    pass
