import difflib

movies = {
    "Inception": ["The Matrix", "Interstellar", "Iron Man"],
    "The Matrix": ["Iron Man", "Inception", "Interstellar"],
    "Avengers": ["Spider-Man", "John Wick", "The Dark Knight"],
    "Interstellar": ["Inception", "The Martian", "Gravity"],
    "Iron Man": ["The Avengers", "Spider-Man", "Doctor Strange"],
    "John Wick": ["The Dark Knight", "Avengers", "Spider-Man"],
    "Spider-Man": ["Avengers", "Iron Man", "Doctor Strange"],
    "The Dark Knight": ["Inception", "John Wick", "Spider-Man"],
    "The Martian": ["Interstellar", "Gravity", "Inception"],
    "Gravity": ["The Martian", "Interstellar", "Inception"],

    "Vikram": ["Kaithi", "Master", "Rolex"],
    "Kaithi": ["Vikram", "Master", "Thunivu"],
    "Master": ["Vikram", "Kaithi", "Leo"],
    "Leo": ["Vikram", "Kaithi", "Master"],
    "Thunivu": ["Valimai", "Kaithi", "Vikram"],
    "Mankatha": ["Billa", "Vedalam", "Thunivu"],
    "Ghajini": ["7aum Arivu", "Thuppakki", "Mankatha"]
}

books = {
    "Harry Potter": ["Percy Jackson", "The Hobbit", "Narnia"],
    "The Hobbit": ["Lord of the Rings", "Harry Potter", "Narnia"],
    "Narnia": ["Harry Potter", "Percy Jackson", "The Hobbit"],
    "Percy Jackson": ["Harry Potter", "Narnia", "The Hobbit"],
    "Lord of the Rings": ["The Hobbit", "Narnia", "Percy Jackson"],

    "Ponniyin Selvan": ["Sivagamiyin Sabatham", "Parthiban Kanavu", "Kalki Novels"],
    "Sivagamiyin Sabatham": ["Ponniyin Selvan", "Parthiban Kanavu", "Kalki Novels"],
    "Parthiban Kanavu": ["Ponniyin Selvan", "Sivagamiyin Sabatham", "Kalki Novels"]
}

def recommend_item(user_input, dataset):
    user_input = user_input.strip().title()

    if user_input in dataset:
        return dataset[user_input]

    close_matches = difflib.get_close_matches(user_input, dataset.keys(), n=1, cutoff=0.6)
    if close_matches:
        best_match = close_matches[0]
        return dataset[best_match]

    return ["❌ Sorry, item not found in our dataset."]

# 🎯 Interactive Menu
print("✨ Welcome to the Interactive Recommendation System ✨")
print("You can get recommendations for:")
print("1️⃣ Movies 🎬")
print("2️⃣ Books 📚")
print("Type 'exit' anytime to quit.\n")

while True:
    choice = input("👉 Choose (1 for Movies / 2 for Books): ")

    if choice.lower() == "exit":
        print("👋 Thanks for using the system! Goodbye!")
        break

    if choice == "1":
        user_movie = input("🎬 Enter a movie title: ")
        if user_movie.lower() == "exit":
            break
        recommendations = recommend_item(user_movie, movies)
        print("\n✨ Recommended movies for you:")
        for rec in recommendations:
            print(f"   🎥 {rec}")
        print("\n" + "-"*40 + "\n")

    elif choice == "2":
        user_book = input("📚 Enter a book title: ")
        if user_book.lower() == "exit":
            break
        recommendations = recommend_item(user_book, books)
        print("\n✨ Recommended books for you:")
        for rec in recommendations:
            print(f"   📖 {rec}")
        print("\n" + "-"*40 + "\n")

    else:
        print("⚠️ Invalid choice! Please enter 1 or 2.\n")
