# favourite_videos

favourite_videos allows you to store a list your favourite **Movies** and **TV shows** and then generates a static web page to browse the videos and watch the trailers.

# Quickstart

### Install
    import media
    import fresh_tomatoes

### Examples
Below you will see _code_ that shows you how to create an instance of a Movie or TV-Show and how to pass it to the function that creates a static web page:

	#Defining Movie Instances
	movie1 = media.Movie("Name","Description","Image URL","Trailer URL","Duration")
	movie2 = media.Movie("Name","Description","Image URL","Trailer URL","Duration")
	
	#Defining TV-Show Instances
	tv_show1 = media.Movie("Name","Description","Image URL","Trailer URL",seasons)
	tv_show2 = media.Movie("Name","Description","Image URL","Trailer URL", seasons)

	#List of movies to use in HTML creation
	movies = [movie1, movie2]

	#List of movies to use in HTML creation
	tv_shows = [tv_show1, tv_show2]

	#Calling function open_videos_page from fresh_tomatoes module (this is a function created by modifying function open_movies_page)
	fresh_tomatoes.open_videos_page(movies, tv_shows)

# Issues / Limitations
Both a _Movie_ and  _TV-show_ object(s) need to be defined and passed to the function `open_videos_page(movie, tv_show)` in a list format to get an output of a static web page.

# License
You can do whatever you want with it.    
