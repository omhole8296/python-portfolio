from datetime import datetime
import requests
pixela="https://pixe.la/v1/users"
user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
headers={
    "X-USER-TOKEN":token
}
# response=requests.post(url="https://pixe.la/v1/users",json=user_params)
# print(response.text)


graph_endpoint=f"{pixela}/{username}/graphs"
graph_config={
    "id":graph_id,
    "name":"Coding Graph",
    "unit":"Hr",
    "type":"float",
    "color":"ajisai"
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

quantity=input("How many hr did you code")
today=datetime.now()
pixel_creation_endpoint=f"{pixela}/{username}/graphs/{graph_id}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":quantity
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)


update_endpoint=f"{pixela}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"
new_pixel_data={
    "quantity":quantity
}
# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)


delete_endpoint=f"{pixela}/{username}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"
# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)

# you can update ,delete, put or get by just uncommenting  the lines and adding username ,graph_id & token
