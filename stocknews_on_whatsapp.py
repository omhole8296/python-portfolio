import requests
from twilio.rest import Client
response=requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=compact&apikey=stocksapikey")
response.raise_for_status()
data=response.json()


def send_news_alert(message_header):
    news=requests.get(url="https://newsapi.org/v2/everything?q=tesla&from=2025-12-04&sortBy=publishedAt&apiKey=newsapikey")
    news.raise_for_status()
    newsdata=news.json()
    
    
    articles = newsdata["articles"][:3]
    message_body = message_header + "\n\n"
    for i, article in enumerate(articles, start=1):
        title = article["title"]
        desc = article["description"] or "No description available"
        message_body += f"Headline {i}: {title}\nBrief: {desc}\n\n"
    account_sid = "id"   
    auth_token = "token"              
    client = Client(account_sid, auth_token)
    client.messages.create(
    from_="whatsapp:sender no.", 
    to="whatsapp:recever no.",       
    body=message_body)


dates = sorted(data["Time Series (Daily)"].keys(),reverse=True)
latestdate=dates[0]
previousdate=dates[1]
print(latestdate)
print(previousdate)

latestclose=data["Time Series (Daily)"][latestdate]["4. close"]
print(latestclose)

previousclose=data["Time Series (Daily)"][previousdate]["4. close"]
print(previousclose)


diff=float(latestclose)-float(previousclose)
per=round((diff*100)/float(previousclose))
print(per)
if per>5 :
    print("stock increase")
    send_news_alert(f"TSLA: 🔺{per}%")
elif per<-5:
    print("stock decrease")
    send_news_alert(f"TSLA: 🔻{per}%")
else:
    print("No significant change")
