import media #python module that has the parent class 'Video' & children 'Movie' & 'Tv_Show'
import fresh_tomatoes #python module provided by Udacity, however, edited to implement new concepts introducted in this course

#Favourite Movies
shutter_island = media.Movie("Shutter Island",
                             "In 1954, a U.S. Marshal investigates the disappearance of a murderer, who escaped from a hospital for the criminally insane.",
                             "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM",
                             "2hr 18min")

inside_out = media.Movie("Inside Out",
                         "In 1954, a U.S. Marshal investigates the disappearance of a murderer, who escaped from a hospital for the criminally insane.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4",
                         "1hr 35min")

matchstick_men = media.Movie("Matchstick Men",
                            "A phobic con artist and his protégé are on the verge of pulling off a lucrative swindle when the former's teenage daughter arrives unexpectedly.",
                            "https://upload.wikimedia.org/wikipedia/en/8/8e/Matchstick_Men.jpg",
                            "https://www.youtube.com/watch?v=WgsmEhnIy7I",
                            "1hr 56min")

#Favourite TV Shows
walking_dead = media.TvShow("Walking Dead",
                            "Sheriff Deputy Rick Grimes wakes up from a coma, to learn the world is in ruins, and must lead a group of survivors to stay alive.",
                            "http://www.gstatic.com/tv/thumb/tvbanners/13176393/p13176393_b_v8_ab.jpg",
                            "https://www.youtube.com/watch?v=R1v0uFms68U",
                            7)

game_of_thrones = media.TvShow("Game of Thrones",
                                "Nine noble families fight for control over the mythical lands of Westeros, while a forgotten race returns after being dormant for thousands of years.",
                                "http://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg",
                                "https://www.youtube.com/watch?v=BpJYNVhGf1s",
                                7)

house_of_cards = media.TvShow("House of Cards",
                              "A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.",
                              "http://www.gstatic.com/tv/thumb/tvbanners/13835596/p13835596_b_v8_aa.jpg",
                              "https://www.youtube.com/watch?v=ULwUzF1q5w4",
                              5)

#List of movies to use in HTML creation
movies = [shutter_island, matchstick_men, inside_out]

#List of movies to use in HTML creation
tv_shows = [walking_dead, game_of_thrones, house_of_cards]

#Calling function open_videos_page from fresh_tomatoes module (this is a function created by modifying function open_movies_page)
fresh_tomatoes.open_videos_page(movies, tv_shows)
