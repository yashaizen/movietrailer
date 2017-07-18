# Basic Handling Class
class Base():
    # Defining A Constructor
    def __init__(self, title, image, trailer):
        self.title = title
        self.image = image
        self.trailer = trailer

#  A Function to open the trailer from the given URL in a new browser window.
    def show_trailer(self):
        webbrowser.openurl(self.trailer)


# Separate Class 'Movie' To Add a Movie Database.
# We keep it separate so that if we want to change anything just for Movies, we can do it hassle free.
class Movie(Base):
    def __init__(self, title, image, trailer):
        Base.__init__(self, title, image, trailer)

