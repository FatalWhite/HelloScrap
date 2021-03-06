#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'
source_code = requests.get(URL)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'lxml')

movie_list = []
for rank in soup.select("img['class = thumb_photo']"):
    movie_list.append(rank.get("alt").strip())

rate_list = []
for rank in soup.select("em['class=emph_grade']"):
    rate = rank.text.strip()
    if rate == "":
        rate = 10
    rate_list.append(rate)

info_list = []
rank = soup.select("dd")
for rank in soup.select("dd"):
    info_list.append(rank.text.strip())


# for rank in soup.select("dl['class=list_state']"):
#     info = rank.text.strip()
#     print(info)
#     info_list.append(rank.text.strip())

for i in range(0, len(movie_list)):
    rank = i + 1
    print( 'top' + str(rank) )
    print(movie_list[i])
    print('평점 : ' + str(rate_list[i]) + ' / 10')
    print(info_list[2 * i])
    print(info_list[2 * i + 1])
    print
