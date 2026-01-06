import requests
from datetime import datetime
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint= "your project url

user_params={
  "query": input("Tell which exercise you did : "),
  "weight_kg": 58,                  
  "height_cm": 175,                 
  "age": 20,                       
  "gender": "male"         
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": App_ID,
    "x-app-key": API_Key
}

responses = requests.post(url, headers=headers, json=user_params)
result = responses.json()

today=datetime.now()
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }




bearer_headers = {
"Authorization":f"Bearer {Bearer_TOKEN} "
}

response=requests.post(url= sheet_endpoint,json=sheet_inputs,headers=bearer_headers)
print(response.text)
