import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all(name='h3')
movie_titles = [movie.getText() for movie in all_movies]
file_content = '\n'.join(movie_titles[::-1])

with open("movies.txt", "w") as file:
    file.write(file_content)
    file.close()


# Second decision:

# response = requests.get(
#     "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
#     )
# text = response.text

# soup = BeautifulSoup(text, "html.parser")
# movie_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

# file = open("movies.txt", "a")
# for el in reversed(movie_titles):
#     file.write(el + "\n")

# file.close()
