#!/usr/bin/env python3
import sys, re
from datetime import datetime
import pathlib
import urllib.request
from lxml import html

def fixEmbedLink(url):
    return url.replace('/embed/', '/video/')

def getTree(url):
    if len(url) == 0:
        sys.exit('Parameter required, need BitChute URL')
    print('Fetching page ' + url)
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
    req = urllib.request.Request(url, headers = headers)
    htmlPage = urllib.request.urlopen(req).read()
    print('Parsing HTML...')
    return html.document_fromstring(htmlPage)

def getTarget(tree):
    match = tree.xpath('//*[@id="player"]/source')
    if len(match) == 0:
        sys.exit('Could not find player-source XPath to download')
    return match[0].get('src')

def getTitle(tree):
    match = tree.xpath('//*[@id="video-title"]')
    if len(match) == 0:
        sys.exit('Could not find page title XPath')
    title = match[0].text_content()
    charsRemovedTitle = re.sub(r'[^\w ]', '', title)
    words = charsRemovedTitle.split()
    newWords = []
    for word in words:
        newWords.append(word.capitalize())
    return ' '.join(newWords)

def getDate(tree):
    match = tree.xpath('//*[@id="video-watch"]/div/div[1]/div[3]/div/div[1]')
    if len(match) == 0:
        sys.exit('Could not find pubish date XPath')
    datePlatform = match[0].text_content()
    datePlatformStripped = datePlatform[20:-10] + datePlatform[-8:-2]
    dateObject = datetime.strptime(datePlatformStripped, '%H:%M %Z on %B %d, %Y')
    return dateObject.strftime('%Y%m%d')
    
def getPublisher(tree):
    match = tree.xpath('//*[@id="video-watch"]/div/div[1]/div[3]/div/div[2]/div[3]/p[1]/a')
    if len(match) == 0:
        sys.exit('Could not find publisher name XPath')
    publisherSpaced = match[0].text_content()
    return re.sub(r'[^\w]', '_', publisherSpaced)

def getExtension(target):
    return pathlib.Path(target).suffix

def downloadVideo(target, publisher, date, title, extension):
    outputFile = f'{date} {title}{extension}'
    pathlib.Path(publisher).mkdir(parents=True, exist_ok=True)
    outputFull = publisher + '/' + outputFile
    if pathlib.Path(outputFull).is_file():
        sys.exit('File already exists: ' + outputFull)
    print(f'Downloading video as: ' + outputFull)
    urllib.request.urlretrieve(target, outputFull)
    print('Done.')

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    url = fixEmbedLink(' '.join(args))
    tree = getTree(url)
    target = getTarget(tree)
    publisher = getPublisher(tree)
    date = getDate(tree)
    title = getTitle(tree)
    extension = getExtension(target)
    downloadVideo(target, publisher, date, title, extension)

if __name__ == '__main__':
    sys.exit(main())

# EOF
