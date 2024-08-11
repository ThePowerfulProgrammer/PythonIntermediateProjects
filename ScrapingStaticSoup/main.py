from bs4 import BeautifulSoup
import requests 

response =  requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")


soup = BeautifulSoup(response.text, 'html.parser')
articleTag = soup.find(name="a", class_="storylink")
articleText = soup.find(name="a", class_="storylink").text
articleLink = soup.find(name="a", class_="storylink").get("href")
articleUpvote = soup.find(name="span", class_="score").text



print("Article Title: ", articleText)
print("Link: ", articleLink)
print("Upvotes: ",articleUpvote)

articles = soup.find_all(name="a", class_="storylink")
articleUpvotes = soup.find_all(name="span", class_="score")

# print("\n"*20)
# for article in articles:
#     print(f"Title: {article.getText()} - {article.get('href')}  {articleUpvotes.getText()}")



largestScore = 0
index = 0
            
            
for i in range(len(articleUpvotes)):
    if (int(articleUpvotes[i].getText().split()[0]) > largestScore):
        largestScore = int(articleUpvotes[i].getText().split()[0])
        index = i

print(largestScore)
print(index)
print(articleUpvotes[index])
print(articles[index])
        