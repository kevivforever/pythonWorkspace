import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "a story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_%282009_film%29#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lotr = media.Movie("Lord of the Rings", "A hobbit commence on a journey to destroy the strongest ring in the world where it was created",
                   "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_%28film_series%29#/media/File:Ringstrilogyposter.jpg",
                   "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

school_of_rock = media.Movie("School of rock", "Using rock music to learn",
                   "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                   "https://www.youtube.com/watch?v=3PsUJFEBC74")

movies = [toy_story, avatar, lotr, school_of_rock]
#fresh_tomatoes.open_movies_page(movies)
#print (toy_story.storyline)
#print (avatar.storyline)
#avatar.show_trailer()
#lotr.show_trailer()
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)

