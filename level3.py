from helper import extract_comments
import re

comments = extract_comments('http://www.pythonchallenge.com/pc/def/equality.html')
comment = comments[0]

letters = re.findall("[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+", comment)
message = "".join(letters)

print("http://www.pythonchallenge.com/pc/def/"+message+".html")