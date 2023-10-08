import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "How to build APIs", "likes": "20000", "views": "10000"}, {"name": "How to build a website", "likes": "30", "views": "3000"}, {"name": "How to build a house", "likes": "10", "views": "100"}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/" + str(0))
print(response)

input()

response = requests.get(BASE + "video/" + str(2))
print(response.json())
