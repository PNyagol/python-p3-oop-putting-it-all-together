class Book:
    def __init__(self, title, page_count):
        self.title = title
        if type(page_count) is not int:
            print("page_count must be an integer")
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")