class Movie:

    all = []
    reviews = []
    reviewers = []
    
    def __init__(self, title):
        if (len(title) > 0):
            self.title = title
        else:
            raise Exception("Title needs to be more than 0 characters!")
        Movie.all.append(self)
        

    def title(self, title):
        return title
        

    def average_rating(self):
        count = 0
        for review in self.reviews:
            count += review
        return count/len(self.reviews)

    @classmethod
    def highest_rated(cls):
        highest = 0
        highest_movie = None
        for movie in Movie.all:
            if (movie.average_rating() > highest):
                highest = movie.average_rating()
                highest_movie = movie
        return highest_movie