import json
import random 
import os

def get_all_movies(movies):  # helper function
    all_movies = []
    # Collect all movies from every genre
    for genre in movies:
        for movie in movies[genre]:
            movie_copy = movie.copy()      # Create a copy
            movie_copy["genre"] = genre    # Add genre for display
            all_movies.append(movie_copy)
    return all_movies


def load_movies():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data.json")
    
    if not os.path.exists(file_path):
            return {}
    
    with open(file_path,'r') as file:
        movies = json.load(file)
        return movies
    
def view_genres(movies):
    print("===========MOVIES===========")
    for index,genre in enumerate(movies,start=1):
        print(index,genre)

def view_movies_acc_genre(movies):
    genre = input("Enter the genre:").strip().title()
    if genre in movies:
        for index,movie in enumerate(movies[genre],start=1):  #iterating over a list
            print(f"Movie {index}")
            print(f"Title  : {movie['title']}")
            print(f"Rating : {movie['rating']}")
            print(f"Year   : {movie['year']}")
            print(f"Mood   : {movie['mood']}")
            print()
            
    else:
        print("Genre not found")

def search_movie(movies):
    movie_name = input("Enter the movie name:").strip().title()
    for genre in movies:
        for movie in movies[genre]:
            if movie['title'] == movie_name:
                print("\nMovie Found!\n")
                print(f"Genre  : {genre}")
                print(f"Title   : {movie['title']}")
                print(f"Rating  : {movie['rating']}")
                print(f"Year    : {movie['year']}")
                print(f"Mood    : {movie['mood']}")
                return   #exit the function immediately
    print("Movie not found")


def add_movie(movies):
    u_genre = input("Enter genre of movie you want to add: ").strip().title()
    u_title = input("Enter title of the movie you want to add:").strip().title()
    u_rating = float(input("Enter rating of the movie: ").strip())
    u_year = int(input("Enter the year in which movie was released: ").strip())
    u_mood =input("Enter mood of the movie: ").strip().lower()

    new_movie = {
        "title":u_title,
        "rating":u_rating,
        "year": u_year,
        "mood":u_mood
    }

    if u_genre in movies:
        movies[u_genre].append(new_movie)
        
    else:
        movies[u_genre] = [new_movie]
    
    save_movies(movies)
    print("\nMovie added successfully!")

def save_movies(movies):
    with open ("data.json",'w') as file:
        json.dump(movies,file,indent=4)  #json.dump(object_to_save , file)

def update_movie(movies):
    movie_name = input("Enter the movie you want to update: ").strip().title()

    for genre in movies:
        for movie in movies[genre]:

            if movie["title"] == movie_name:
                print("\nWhat do you want to update?")
                print("1. Title")
                print("2. Rating")
                print("3. Year")
                print("4. Mood")

                option = int(input("Enter your choice: "))

                if option == 1:
                    movie["title"] = input("Enter new title: ").strip().title()

                elif option == 2:
                    movie["rating"] = float(input("Enter new rating: "))

                elif option == 3:
                    movie["year"] = int(input("Enter new year: "))

                elif option == 4:
                    movie["mood"] = input("Enter new mood: ").strip().lower()

                else:
                    print("Invalid option.")
                    return

                save_movies(movies)
                print("\nMovie updated successfully!")
                return

    print("Movie not found.")

def delete_movie(movies):
    movie_name = input("Enter name of the movie to be deleted: ").strip().title()
    for genre in movies:
        for movie in movies[genre]:

            if movie["title"] == movie_name:
                movies[genre].remove(movie)

                # Remove the genre if it has no movies left
                if len(movies[genre]) == 0:
                    del movies[genre]

                save_movies(movies)
                print("Movie deleted successfully.")
                return
    else:
        print("Movie not found.")

def top_rated_movies(movies):
    n= int(input("Enter the number of  top movies you want to see "))
    all_movies = get_all_movies(movies)
    # Sort by rating in descending order
    all_movies = sorted(
        all_movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )
    print("\n========== TOP RATED MOVIES ==========\n")
    for index, movie in enumerate(all_movies[:n], start=1):
        print(f"{index}. {movie['title']}")
        print(f"Genre  : {movie['genre']}")
        print(f"Rating : {movie['rating']}")
        print(f"Year   : {movie['year']}")
        print(f"Mood   : {movie['mood']}")
        print()
    
def random_movie_recommend(movies):
    all_movies = get_all_movies(movies)
    recommended =random.choice(all_movies)

    print("\n========== TODAY'S RECOMMENDATION ==========\n")
    print(f"Title  : {recommended['title']}")
    print(f"Genre  : {recommended['genre']}")
    print(f"Rating : {recommended['rating']}")
    print(f"Year   : {recommended['year']}")
    print(f"Mood   : {recommended['mood']}")

movies = load_movies()
while True:
    print("\n========== MOVIE RECOMMENDATION ENGINE ==========")
    print("1. View Genres")
    print("2. View Movies by Genre")
    print("3. Search Movie")
    print("4. Add Movie")
    print("5. Update Movie")
    print("6. Delete Movie")
    print("7. Top Rated Movies")
    print("8. Random Movie Recommendation")
    print("9. Exit")

    choice = input("\nEnter your choice:")
    if choice == "1":
        view_genres(movies)

    elif choice == "2":
        view_movies_acc_genre(movies)

    elif choice == "3":
        search_movie(movies)

    elif choice == "4":
        add_movie(movies)

    elif choice == "5":
        update_movie(movies)

    elif choice == "6":
        delete_movie(movies)

    elif choice == "7":
        top_rated_movies(movies)

    elif choice == "8":
        random_movie_recommend(movies)

    elif choice == "9":
        print("Thank you for using Movie Recommendation Engine!")
        break

    else:
        print("Invalid choice! Please try again.")

    # Reload movies after every operation
    movies = load_movies()
