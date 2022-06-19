import os
import pathlib
import re

sortFromPath = r"D:\Downloads\2 - Torrents"
moviepath = r"D:\Videos\Movies"
seriespath = r"D:\Videos\Series"

#.is_file():


for sortFromPath in pathlib.Path(sortFromPath).iterdir():
    file_name, file_ext = os.path.splitext(sortFromPath)

    movie_name = re.split('s[0-9]|20', file_name, maxsplit=1)

    print(movie_name)