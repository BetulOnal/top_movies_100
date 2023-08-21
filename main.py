import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

respond = requests.get(url=URL)
main_doc = respond.text

soup = BeautifulSoup(main_doc,"lxml")
movies = soup.select(selector=".title")

move_list = []
for x in movies:
    move_list.append(x.text)


new_list = []
for x in range(1,101):
    num= int(x*-1)
    new_list.append(move_list[num])

print(new_list)

file = open("moviest.txt","w")
for x in new_list:
    file.writelines(f"{x}\n")

