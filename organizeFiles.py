import os
import re

# files are ordered same as Windows File Explorer
def natural_key(string):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', string)]


modes = ["grayscale", "color"]

mangas = ["Naruto", "Bleach", "One-Piece", "Hunter-X-Hunter"]
coloredMangas = ["Naruto-Digital-Colored-Comics", "Bleach-Color", "One-Piece-Digital-Colored-Comics", "Hunter-x-Hunter-Color"]

"""
for mode in modes:
    for manga in allMangas1:
        path = f"{mode}/{manga}"

        files = sorted(
            [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))],
            key=natural_key
        )

        chapterIndex = 1
        pageIndex = 1
        for file in files:
            fullFilePath = os.path.join(path, file)
            oldName, ext = os.path.splitext(file) # splitext divides into filename and extension

            chapterNumber = int(re.search(r'\d+', oldName).group())
            if chapterNumber != chapterIndex:
                chapterIndex += 1
                pageIndex = 1
                
            newFileName = f"chapter{chapterNumber}-page{pageIndex}{ext}"
            print(newFileName)
            os.rename(os.path.join(path, file), os.path.join(path, newFileName))

            pageIndex += 1

"""

for mangaIndex in range(len(mangas)):
    for mode in modes:
        manga = mangas[mangaIndex] if mode == "grayscale" else coloredMangas[mangaIndex]

        path = f"{mode}/{manga}"

        files = sorted(
            [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))],
            key=natural_key
        )

        chapterIndex = 1
        pageIndex = 1
        for file in files:
            fullFilePath = os.path.join(path, file)
            oldName, ext = os.path.splitext(file) # splitext divides into filename and extension

            chapterNumber = int(re.search(r'\d+', oldName).group())
            if chapterNumber != chapterIndex:
                chapterIndex += 1
                pageIndex = 1
                
            newFileName = f"chapter{chapterNumber}-page{pageIndex}{ext}"
            print(newFileName)
            os.rename(os.path.join(path, file), os.path.join(path, newFileName))

            pageIndex += 1