from lib.viewer import Viewer
from lib.movie import Movie

class Review:
    
    def __init__(self, viewer, movie, rating):
        if (isinstance(viewer, Viewer)):
            self.viewer = viewer
        else:
            raise Exception("Not an instance of a Viewer")
        if (isinstance(movie, Movie)):
            self.movie = movie
        else:
            raise Exception("Not an instance of a Movie")
        if (rating > 0 and rating < 6 and type(rating) == int):
            self.rating = rating
        else:
            raise Exception("Rating must be between 1 and 5")

    def rating(self, rating):
        return rating
        

    def viewer(self):
        return self.viewer

    def movie(self):
        return self.movie