import webbrowser 

class Video():
    """A recording of moving visual images. The video has the following attributes:
        title: Title of the video
        storyline: A description of the video
        poster_image: A background image for the video
        trailer_youtube: Trailer of the video
    """
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
class Movie():
    """A movie class that inherits the attributes of video class. A movie has the following attributes:
        (Video) title: Title of the video
        (Video) storyline: A description of the video
        (Video) poster_image: A background image for the video
        (Video) trailer_youtube: Trailer of the video
        (Movie) movie_duration: The duration of the movie
    """
    def __init__(self, title, storyline, poster_image, trailer_youtube, movie_duration):
        Video.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.title = title
        self.storyline = storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_duration = movie_duration

class TvShow():
    """A tv-show class that inherits the attributes of video class. A tv-show has the following attributes:
        (Video) title: Title of the video
        (Video) storyline: A description of the video
        (Video) poster_image: A background image for the video
        (Video) trailer_youtube: Trailer of the video
        (Movie) show_seasons: How many seasons does the tv-show have
    """
    def __init__(self, title, storyline, poster_image, trailer_youtube, show_seasons):
        Video.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.show_seasons = show_seasons

        
        
