import helper
import re
from progress.bar import Bar

links = helper.extract_links("http://www.pythonchallenge.com/pc/def/linkedlist.php")
url = "http://www.pythonchallenge.com/pc/def/"+links[0]
number = 0
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

bar = Bar('Following the linked list', max=251)
for i in range(251):
    body = helper.get_body(url)
    bar.next()

    if body == "Yes. Divide by two and keep going.":
        url = base_url + str(number / 2)
    else:
        try:
            number = int(re.search(r"and the next nothing is (\d+)", body)[1])
            url = base_url + str(number)
        except:
            print("\n")
            print("Url found", "http://www.pythonchallenge.com/pc/def/"+body)
            bar.finish()
            exit(1)

bar.finish()
