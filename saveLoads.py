from json import dump
from json import loads
from pathlib import Path

def save(listWords):
	
	with open("listWords.json", "w") as fout:
		dump(listWords, fout)

def load():
	
	
	words = []
	
	filesWords = Path("listWords.json")	
	if filesWords.is_file():
		words = loads(open("listWords.json").read())
		
	return words
	
