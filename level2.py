from helper import extract_comments

comments = extract_comments('http://www.pythonchallenge.com/pc/def/ocr.html')
comment = comments[1]

chr_freq = dict()

for c in comment:
    if c in chr_freq:
        chr_freq[c] += 1
    else:
        chr_freq[c] = 1

message = ""
for i in sorted(chr_freq.items(), key=lambda x: (x[1])):
    if i[1] == 1:
        message += i[0]

print("http://www.pythonchallenge.com/pc/def/"+message+".html")



