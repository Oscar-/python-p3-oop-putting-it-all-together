#!/usr/bin/env python3
import ipdb

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book1 = Book("And Then There Were None", 272)
book2 = Book("The World According to Garp", 69)




    

     
     

    
# ipdb.set_trace()   