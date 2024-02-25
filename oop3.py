# special methods
#__init__ metodu
# str-len

class Movie():
    def __init__(self,title,creator,duration):
        self.title=title
        self.creator=creator
        self.duration=duration
        print("Movie object created.")
    def __str__(self):
        return f"{self.title} by {self.creator}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("movie deleted")

m=Movie("movie name","movie creator",140)
print(len(m))

del m
