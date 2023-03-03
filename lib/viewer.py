from lib.movie import Movie

class Viewer:

    all = []

    def __init__(self, username):
        if (len(username) > 5 and len(username) < 17):
            self.username = username
            Viewer.all.append(username)
        else:
            raise Exception("Username must be 6 to 16 characters!")
        self.reviews = []
        self.reviewed_movies = []

    def username(self, username):
        return username
        
    def reviewed_movie(self, movie):
        test = False
        for reviewed_movie in self.reviewed_movies:
            if (reviewed_movie == movie):
                test = True
        return test

    def rate_movie(self, movie, rating):
        from lib.review import Review
        if (self.reviewed_movie(movie)):
            for review in self.reviews:
                if (review.viewer == self):
                    review.rating = rating
        else:
            new_review = Review(self, movie, rating)
            movie.reviews.append(rating)
            movie.reviewers.append(self)
            self.reviews.append(new_review)
            self.reviewed_movies.append(movie)