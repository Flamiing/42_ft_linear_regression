class URL():
    def __init__(self, url):
        self.url = url
        self.page = 1
    
    def __str__(self):
        return self.url + '?page=' + str(self.page)

    def next_page(self):
        self.page += 1

    def get_url(self):
        return str(self)