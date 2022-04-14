import requests
from datetime import datetime
USERNAME="your username"
TOKEN="your token"
ID="first"
params={
    "id":ID,
    "name":"Running Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"


}
headers={
    "X-USER-TOKEN":TOKEN
}

today=datetime(year=2022,month=4,day=11)
todays_straf=today.strftime("%Y%m%d")
print(today)
post_params={
    "date":todays_straf,
    "quantity":"23.78",

}
update_params={
    "quantity":"40.78",

}

end_point="https://pixe.la/v1/users"
graph_endpoint=f"{end_point}/{USERNAME}/graphs"
post_endpoint=f"{end_point}/{USERNAME}/graphs/{ID}"
update_pixel=f"{end_point}/{USERNAME}/graphs/{ID}/{todays_straf}"
# request=requests.post(end_point,json=params)
# print(request.text)

# request=requests.post(url=graph_endpoint,json=params,headers=headers )
# print(request.text)

# post_request=requests.post(url=post_endpoint,json=post_params,headers=headers)
# print(post_request.text)

# update_request=requests.put(url=update_pixel,json=update_params,headers=headers)
# print(update_request.text)

delete_request=requests.delete(url=update_pixel,headers=headers)
print(delete_request.text)
