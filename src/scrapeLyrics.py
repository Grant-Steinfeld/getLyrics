from bs4 import BeautifulSoup
import requests


def getPageData(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    title = getTitle(soup)
    lyrics = getLyrics(soup)
    return title, lyrics


def getTitle(soup):
    return soup.find('h1', class_='page-title').text.encode('utf-8').strip()


def getLyrics(soup):
    return soup.find('div', {'class':'content-text-inner'}).text.encode('utf-8').strip()


def writeToFile(artist, url, counter):
    title, lyrics = getPageData(url)
    pathToCorpus = './../corpi/{}/raw/'.format(artist)

    import os.path
    if not os.path.exists(pathToCorpus):
        os.makedirs(pathToCorpus)

    fileName = '{}_{}.txt'.format(artist,counter)
    corpusFile= "{}/{}".format(pathToCorpus,fileName)

    with open(corpusFile, 'a') as theFile:

        theFile.write( "title={}".format(title.replace('lyrics','').strip() ) )
        theFile.write( '\n' )
        theFile.write( '\n' )
        theFile.write( lyrics )
        theFile.write( '\n' )
        theFile.write( '\n' )
        theFile.write( '.' )
        theFile.write( '\n' )
        theFile.write( '\n' )


def parseArtist(artists):
    for artist in artists:

        lines=[]
        with open('../links/{}.urls'.format(artist)) as file:
            lines = [line.strip() for line in file]

        print artists, ' lines:', len(lines)

        counter=0
        for line in lines:
            counter = counter + 1
            writeToFile(artist , line, counter)
            print counter



if __name__ == '__main__':
    artists=['pink_floyd']
    artists=['michael_jackson']
    parseArtist(artists)







