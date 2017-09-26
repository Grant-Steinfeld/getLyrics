from bs4 import BeautifulSoup
import requests


def getPageLinks(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    x = soup.find('div', class_='nodetype-artist-content-lyrics-all')
    bits = x.find_all('a')
    urls = []
    for bit in bits:
        urls.append("http://www.allthelyrics.com{}".format( bit['href']))

    return urls

def writeToFile(artist, urls):

    linkFile = './../links/{}.urls'.format(artist)


    with open(linkFile, 'w+') as theFile:
        theFile.write("\n".join(urls))

def getArtistMainPages(artists):
    for artist in artists:
        url_ = 'http://www.allthelyrics.com/lyrics/{}'.format(artist)
        urls =  getPageLinks(url_)
        writeToFile(artist, urls)



if __name__ == '__main__':
    artists=['led_zeppelin']
    getArtistMainPages(artists)






