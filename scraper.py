
import requests
from bs4 import BeautifulSoup
import re
import os

def createFolders(mode, mangas):
    for manga in mangas:
        os.mkdir(f"{mode}/{manga}")

def parseSiteScript(jsCode):
    CurChapter = re.search(r'"Chapter":"(\d+)",.*?"Page":"(\d+)",.*?"Directory":"(.*?)"', jsCode)

    if CurChapter:
        chapter = CurChapter.group(1)
        page = int(CurChapter.group(2))
        directory = CurChapter.group(3) 
        #print(f"Chapter: {chapter}, Page: {page}, Directory: '{directory}'")
    else:
        print("Could not find chapter dictionary")
        exit()

    CurPathName = re.search(r'vm\.CurPathName\s*=\s*"([^"]+)"', jsCode)

    if CurPathName:
        CurPathName = CurPathName.group(1)
        #print(f"CurPathName: {CurPathName}")
    else:
        print("Could not find path name")
        exit()

    chapterString = chapter[1:-1]
    chapter = chapterString if chapter[-1] == "0" else (chapterString + "." + chapter[-1])

    return chapter, page, directory, CurPathName

def downloadImage(url, mode, mangaName, chapterNumber, index):
    try:
        r = requests.get(url).content
        
        with open(f"{mode}/{mangaName}/chapter{chapterNumber}-page{index}.jpg", "wb+") as f:
            f.write(r)
    except:
        print(f"Error: Could not download chapter {chapterNumber}, page {index}")

# One Piece color to 1035
# Hunter x Hunter color to 390
# if we want JoJo's, have to use CycleGAN
mangas = ["Naruto", "Bleach", "One-Piece", "Hunter-X-Hunter"]
coloredMangas = ["Naruto-Digital-Colored-Comics", "Bleach-Color", "One-Piece-Digital-Colored-Comics", "Hunter-x-Hunter-Color"]

modes = ["grayscale", "color"]
"""
for manga in mangas:
    os.mkdir(f"grayscale/{manga}")
for manga in coloredMangas:
    os.mkdir(f"color/{manga}")
"""


for mangaIndex in range(len(mangas)):
    modes = ["grayscale", "color"]
    pageCounts = {"grayscale" : [], "color" : []}
    matchingPageCounts = []

    for mode in modes:
        manga = mangas[mangaIndex] if mode == "grayscale" else coloredMangas[mangaIndex]
        for chapterNumber in range(3, 11): # CHAPTER
            
            if not (chapterNumber >= 9 and manga == "Hunter-x-Hunter-Color"):
                continue

            url = f"https://manga4life.com/read-online/{manga}-chapter-{chapterNumber}.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            jsCode = soup.find_all("script")[-1].string

            chapter, page, directory, pathName = parseSiteScript(jsCode)

            pageCounts[mode].append(page)

            print(f"Downloading {manga}: Chapter {chapterNumber}...")

            for index in range(1, page+1):
                pageString = "000" + str(index)
                pageString = pageString[-3:]

                url = f"https://{pathName}/manga/{manga}/{'' if directory == '' else directory+'/'}{chapter}-{pageString}.png"

                downloadImage(url, mode, manga, chapterNumber, index)

    for chapterIndex in range(len(pageCounts["color"])):
        matchingPageCounts.append("Yes" if pageCounts["color"][chapterIndex] == pageCounts["grayscale"][chapterIndex] else "No")
    
    with open("MatchingPages.txt", "a") as f:
        f.write(f"{mangas[mangaIndex]}: {matchingPageCounts}\n")