import requests
url = ('https://newsapi.org/v2/top-headlines?sources=espn-cric-info&apiKey=65837541ae524575b8fa0df4556d2d06')
response = requests.get(url)
a=response.json()
#print (response.json())
for i in range(0,5):
    print("Heading name "+str(i+1)+" is")
    print(a['articles'][i]['title']) 
    print(a['articles'][i]['url'])
    print(a['articles'][i]['urlToImage']) 
    print(a['articles'][i]['publishedAt'])