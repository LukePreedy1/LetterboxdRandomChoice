from lxml import html
from bs4 import BeautifulSoup
import requests
import re
import random

#TODO still need to actually get the names of the movies from the page with the watchlist
username = input("What is your letterboxd username?")
url = "https://letterboxd.com/" + username + "/watchlist/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
line = soup.find_all('h1', class_='section-heading')
print(line[0].text)
list_of_num = re.findall(r'\d+', line[0].text)
nums_as_string = ""
for n in list_of_num:
    nums_as_string += n
num = int(nums_as_string)
print(num)
num_of_choice = random.random() * num

# the number of the movie in the list to choose
num_of_choice = int(num_of_choice)
print(num_of_choice)

url += "page/" + str(int(num_of_choice / 21)) + "/"
print(url)

# the number of the movie on the page to get
new_num = num % 21
print(new_num)

page2 = requests.get(url)
soup2 = BeautifulSoup(page.content, 'html.parser')
#//*[@id="content"]/div/div/section/ul/li[7]/div/div/a/span[1]
#print(movies[new_num].text)
print(movies)
#print(movies[new_num].text)
