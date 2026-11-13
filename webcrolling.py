# import requests
# from bs4 import BeautifulSoup

# url = "https://indianexpress.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text, "html.parser")
# print(soup.title.text)


from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time
app = FastAPI()

#chache stored
chache_data = []
last_fetch = 0


@app.get("/news")
def get_news():
    global chache_data, last_fetch

    start = time.time()

    if time.time() - last_fetch >60:
        print("Fetching Fresh Data")

        url = "https://www.ycombinator.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")

        chache_data = [
            item.text for item in soup.find_all("body", class_="ycdc2 base home") 
        ]

        last_fetch = time.time()

    else:
        print("Using catche Data")

    end = time.time()

    time_taken = round(end-start,4)
    print("Time taken ", time_taken)

    return {
        "time_taken":time_taken,
        "data":chache_data[:5]
    }


        