import helper
import pickle

body = helper.get_body("http://www.pythonchallenge.com/pc/def/banner.p")

body_encoded = body.encode()
data = pickle.loads(body_encoded)

s = ""
for row in data:
    for item in row:
        s += item[0]*item[1]
    s += "\n"
print(s)


