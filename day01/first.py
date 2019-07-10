import webbrowser

url = "https://search.daum.net/search?q="
keywords = ["아이유", "수지", "설현"]

for name in keywords:
    webbrowser.open(url + name)


# print("happy" + " " + "hacking")