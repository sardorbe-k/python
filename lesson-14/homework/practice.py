import json
import requests
import random
import os

def parse_students(json_filepath):
    if not os.path.exists(json_filepath):
        print(f"Fayl topilmadi: {json_filepath}")
        return
    with open(json_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    students = data.get("students", [])
    for i, stu in enumerate(students, start=1):
        print(f"{i}. Name: {stu.get('name')}, Age: {stu.get('age')}, Course: {stu.get('course')}")

def get_weather_for_city(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    resp = requests.get(url)
    data = resp.json()
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    wind = data.get("wind", {})
    print(f"\nWeather in {city_name}:")
    print(f"Temperature: {main.get('temp')}°C")
    print(f"Humidity: {main.get('humidity')}%")
    print(f"Pressure: {main.get('pressure')} hPa")
    print(f"Description: {weather_list[0].get('description') if weather_list else 'N/A'}")
    print(f"Wind speed: {wind.get('speed')} m/s")

def modify_books(json_filepath):
    if os.path.exists(json_filepath):
        with open(json_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"books": []}
    books = data["books"]

    def save():
        with open(json_filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    while True:
        print("\n1=List, 2=Add, 3=Update, 4=Delete, 0=Exit")
        ch = input("Tanlang: ")
        if ch == "1":
            for i, b in enumerate(books, 1):
                print(f"{i}. {b['title']} - {b['author']} ({b['year']})")
        elif ch == "2":
            title = input("Title: "); author = input("Author: "); year = input("Year: ")
            books.append({"title": title, "author": author, "year": year})
            save()
        elif ch == "3":
            for i, b in enumerate(books, 1):
                print(f"{i}. {b['title']}")
            sel = int(input("Tanlang: ")) - 1
            if 0 <= sel < len(books):
                books[sel]["title"] = input("New title: ") or books[sel]["title"]
                books[sel]["author"] = input("New author: ") or books[sel]["author"]
                books[sel]["year"] = input("New year: ") or books[sel]["year"]
                save()
        elif ch == "4":
            for i, b in enumerate(books, 1):
                print(f"{i}. {b['title']}")
            sel = int(input("Tanlang: ")) - 1
            if 0 <= sel < len(books):
                books.pop(sel)
                save()
        elif ch == "0":
            break

def recommend_movie_by_genre(api_key):
    genre = input("Movie genre (e.g. Action, Comedy): ")
    search_url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    r = requests.get(search_url).json()
    if r.get("Response") == "False":
        print("No movies found.")
        return
    results = r.get("Search", [])
    movie = random.choice(results)
    movie_data = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={movie['Title']}").json()
    print(f"\n🎬 Title: {movie_data.get('Title')}")
    print(f"Year: {movie_data.get('Year')}")
    print(f"Genre: {movie_data.get('Genre')}")
    print(f"Director: {movie_data.get('Director')}")
    print(f"Plot: {movie_data.get('Plot')}")

def main():
    weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    omdb_api_key = "YOUR_OMDB_API_KEY"

    parse_students("students.json")
    get_weather_for_city("Tashkent", weather_api_key)
    modify_books("books.json")
    recommend_movie_by_genre(omdb_api_key)

if __name__ == "__main__":
    main()

