import media
import fresh_tomatoes

# A Movie Database which includes the title, Trailer URL and its Poster Image.
# This Is created with the help of instances which use the construction "Movie"

assassin = media.Movie("Assassins Creed",
 "http://pre07.deviantart.net/18fb/th/pre/f/2016/133/b/9/assassin_s_creed_movie_flipped_poster_by_maximumsohan-da2byc0.jpg",
 "https://www.youtube.com/watch?v=naQr0uTrH_s")
pirate = media.Movie("Pirates Of The Carribean",
 "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-nie8b7_49ceb417.jpeg?region=0,0,300,450",
 "https://www.youtube.com/watch?v=naQr0uTrH_s")
megamind = media.Movie("MegaMind",
 "https://s-media-cache-ak0.pinimg.com/originals/6b/a2/c4/6ba2c49b228e90497e9bfaa89aa6022e.jpg",
 "https://www.youtube.com/watch?v=Xu42-p6_5RE")
godfather = media.Movie("Godfather",
 "http://imgsrc.allposters.com/img/print/posters/the-godfather_a-G-1635808-0.jpg",
 "https://www.youtube.com/watch?v=sY1S34973zA")
inception = media.Movie("Inception",
 "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/inception_keyart.jpg?itok=7jXiglyb",
 "https://www.youtube.com/watch?v=YoHD9XEInc0")
death = media.Movie("Death Note",
 "https://s-media-cache-ak0.pinimg.com/originals/25/d2/66/25d2668ed913bba840b1bddbbd351e58.jpg",
 "https://www.youtube.com/watch?v=7mhBapcDf4k")

# Adding all the instances inside a list
movies = [assassin, pirate, megamind, godfather, inception, death]

# A Function which will generate our html page and open it in a web browser.
fresh_tomatoes.open_movies_page(movies)

