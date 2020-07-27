# BitChute-DL

## About

This Python script will download any video from the BitChute video platform to your PC for archival or offline use. The target video will be placed in a clearly named directory based on the publisher's name, a file name will be created based on the video title & publishing date and a check will be done for duplicate files. The project is inspired by [YouTube-DL](https://youtube-dl.org/).

## Launching

You'll need Python >= 3.7 and the [LXML](https://pypi.org/project/lxml/) **pip** package:

    pip3 install lxml

Download and unpack [this repository](https://github.com/Matteljay/bitchute-dl/releases), then run the script with the target URL as a parameter. Example:

    python3 ./bitchute-dl.py https://www.bitchute.com/video/oX3AgHj0jlUX/

To keep videos organized, a new folder will be created in the current directory and the video saved inside:

    ./Matteljay/20200529 Tightcms Set Up Your Own Website Cms Built In Vuejs With Mongodb Docker Container.mp4

## Coding details

Feel free to modify the script's behavior, it is a nice example of an app that will do diverse web scraping actions based on XPath XML selectors.

## Contact info & donations

More info here: [Contact](CONTACT.md)
