# Simple Movie Recommendation System (No pandas needed)

# Sample movie dataset as a list of dictionaries
movies = [
    {'title': 'Inception', 'genre': 'Sci-Fi'},
    {'title': 'Titanic', 'genre': 'Romance'},
    {'title': 'Avengers', 'genre': 'Action'},
    {'title': 'Joker', 'genre': 'Drama'},
    {'title': 'Frozen', 'genre': 'Animation'},
    {'title': 'Interstellar', 'genre': 'Sci-Fi'},
    {'title': 'The Notebook', 'genre': 'Romance'}
]

# Function to recommend movies based on genre
def recommend_movies(movie_name, movies):
    # Find the genre of the chosen movie
    genre = None
    for movie in movies:
        if movie['title'].lower() == movie_name.lower():
            genre = movie['genre']
            break
    if not genre:
        print("Movie not found!")
        return
    
    print(f"\nYou liked '{movie_name}' (Genre: {genre}). Here are some recommendations:")
    
    # Recommend other movies of the same genre
    recommendations = [m['title'] for m in movies if m['genre'] == genre and m['title'].lower() != movie_name.lower()]
    
    if recommendations:
        for rec in recommendations:
            print("- " + rec)
    else:
        print("No recommendations found!")

# Main program loop
def main():
    print("Welcome to the Movie Recommendation System!")
    print("Here are the movies you can choose from:")
    for movie in movies:
        print("- " + movie['title'])
    
    while True:
        choice = input("\nEnter a movie you like (or type 'exit' to quit): ")
        if choice.lower() == 'exit':
            print("Goodbye! Hope you enjoy the recommendations!")
            break
        recommend_movies(choice, movies)

# Run the program
if __name__ == "__main__":
    main()