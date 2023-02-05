movies = [
{
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
},
{
    "name": "Hitman",
    "imdb": 6.3,
    "category": "Action"
},
{
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
},
{
    "name": "The Help",
    "imdb": 8.0,
    "category": "Drama"
},
{
    "name": "The Choice",
    "imdb": 6.2,
    "category": "Romance"
},
{
    "name": "Colonia",
    "imdb": 7.4,
    "category": "Romance"
},
{
    "name": "Love",
    "imdb": 6.0,
    "category": "Romance"
},
{
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
},
{
    "name": "AlphaJet",
    "imdb": 3.2,
    "category": "War"
},
{
    "name": "Ringing Crime",
    "imdb": 4.0,
    "category": "Crime"
},
{
    "name": "Joking muck",
    "imdb": 7.2,
    "category": "Comedy"
},
{
    "name": "What is the name",
    "imdb": 9.2,
    "category": "Suspense"
},
{
    "name": "Detective",
    "imdb": 7.0,
    "category": "Suspense"
},
{
    "name": "Exam",
    "imdb": 4.2,
    "category": "Thriller"
},
{
    "name": "We Two",
    "imdb": 7.2,
    "category": "Romance"
}
]
# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
#
# Write a function that returns a sublist of movies with an IMDB score above 5.5.
#
# Write a function that takes a category name and returns just those movies under that category.
#
# Write a function that takes a list of movies and computes the average IMDB score.
#
# Write a function that takes a category and computes the average IMDB score.


def above5_5(movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            if movie['imdb'] > 5.5:
                return True
            return False

    return "Movie not found!"

def above5_5_movies():
  return [movie["name"] for movie in movies if movie['imdb'] > 5.5]


def category(category):
    return [movie["name"] for movie in movies if movie['category'].lower() == category.lower()]

def average_by_name(names):
    score = 0
    count = 0
    for movie in movies:
        if movie["name"] in names:
            score += movie["imdb"]
            count +=1

    return  score / count #len(names)

def average_by_category(category):
    score = 0
    count = 0
    for movie in movies:
        if movie["category"].lower() == category.lower():
            score += movie["imdb"]
            count+=1

    return  score / count


print(above5_5("Exam"))
print(above5_5_movies())
print(category("Romance"))
print(average_by_name(["Exam", "We Two"]))
print(average_by_category("Romance"))

