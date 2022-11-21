import re 
import os
from os.path import join
from os import path

def replaceChars(filepath):
	lyrics = ""
	with open(filepath, 'r') as f:
		lyrics = f.read()

		lyrics = lyrics.replace("е", "e")
		lyrics = lyrics.replace("”", "\"")
		lyrics = lyrics.replace("“", "\"")
		lyrics = lyrics.replace("’", "\'")
		lyrics = lyrics.replace("\u2005", " ")
		lyrics = lyrics.replace("\u205f", " ")
		lyrics = lyrics.replace("\u200b", " ")
		lyrics = lyrics.replace("—", "-") # this is a long dash
		lyrics = lyrics.replace("–", "-") # this is a different long dash
		lyrics = lyrics.replace("…", "...")
	
	# Now we remove the background vocals, which appear between parentheses
	# the [\s\S] character set matches any character, including newline.
	# we also remove and spaces around the parentheses

	# if the match occurs at the start/end of the line, then remove it entirely
	lyrics = re.sub("\n[ ]*\([^()]*?\)[ ]*", "\n", lyrics)
	lyrics = re.sub("[ ]*\([^()]*?\)[ ]*\n", "\n", lyrics)
	lyrics = re.sub("[ ]*\([^()]*?\)[ ]*,", ",", lyrics)

	# if the match does not occur at the start/end of the line, then replace it with a space.
	lyrics = re.sub("[ ]*\([^()]*?\)[ ]*", " ", lyrics)


	with open(filepath, 'w') as f:
		f.write(lyrics)



working_dir = path.dirname(__file__)
raw_lyric_dir = "lyrics"

os.chdir(raw_lyric_dir)
album_titles = [name for name in os.listdir(".") if os.path.isdir(name)]


for album in album_titles:
	os.chdir(join(working_dir, raw_lyric_dir, album))
	for path in os.listdir("."):
		# print(album, path)
		if not os.path.isfile(path):
			continue
		replaceChars(path)
