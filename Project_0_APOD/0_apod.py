import requests
import json
import urllib.request as ur
import wget

def main():
    count = 2
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "DEMO_KEY"
    query_params = {"api_key":api_key, "hd":True, "count":count}

    response = requests.get(url, query_params)

    info = response.json()
    # print(info)
    for i in range(count):
        img_url = info[i]["url"]
        # filename = img_url.split("/")[-1]
        # ur.urlretrieve(img_url, filename)
        wget.download(img_url)

        explaination = info[i]["explanation"]
        with open(f"explaination_{i}.txt", "w") as f:
            f.write(img_url + "\n")
            f.write(explaination)
    
    # with open("example.json", "w") as f:
    #     json.dump(info[0], f)

if __name__ == "__main__":
    main()