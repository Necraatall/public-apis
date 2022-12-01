import requests
import time
from bs4 import BeautifulSoup



# anime_querry_response = requests.get(
#     f'https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=~Kokaku&title=~Ghost%20in%20the%20Shell&gid=2330273185')

# print(f'anime_querry_response : {anime_querry_response}')

# fish_querry_response = requests.get('https://www.fishwatch.gov/api/species/red-snapper')
# print(f'anime_querry_response : {fish_querry_response.json()}')


# response = requests.get(
#     'https://fakestoreapi.com/products')
# print(f'response.status_code : {response.status_code}')

# fakestore_response = requests.get('https://fakestoreapi.com/products')
# print(f'response.status_code : {response.status_code}')
# # print(f'response.status_code : {response.json()}')

# fakestore_response_result = response.json()[0]['price']
# print(f'fakestore rating {fakestore_response_result}')

# print(f'fakestoreapi : {response.json()}')

######################################################################
# POST requests
######################################################################
API_ENDPOINT = 'https://fakestoreapi.com/users'

data = {
    "email": 'totonono@gmail.com',
    "username": 'Toto',
    "password": 'm38rmF$nono',
    "name": {
        "firstname": 'Toto',
        "lastname": 'oooo'
    },
    "address": {
        "city": 'Praha',
        "street": 'Zbraslavska',
        "number": 1,
        "zipcode": '15000',
        "geolocation": {
            "lat": '-37.321',
            "long": '81.1496'
        }
    },
    "phone": '725354123'
}

response = requests.post(url = API_ENDPOINT, data = data)
print(f'response.status_code : {response.status_code}')
pastebin_url = response.text
print("The pastebin URL is:%s"%pastebin_url)

number = response.json()['id']

print("Printed immediately.")
time.sleep(5.0)
print("Printed after 5.0 seconds.")

response = requests.get(
    f'https://fakestoreapi.com/users/{number}')

print(f'response.request.method : {response.request.method}')
print(f'response.request.path_url : {response.request.path_url}')
print(f'response.request.headers : {response.request.headers}')
print(f'response.request.body : {response.request.body}')
print(f'response.request.url : {response.request.url}')
print(f'response.status_code : {response.status_code}')
print(f'response.reason : {response.reason}')

print(f'response.ok : {response.ok}')
print(f'response.raise_for_status() : {response.raise_for_status()}')
print(f'response.links : {response.links}')

print(f'time till response response.elapsed : {response.elapsed}')
print(f'headers response response.headers : {response.headers}')
print(f'encoding response response.encoding : {response.encoding}')
print(f'cookies response response.cookies : {response.cookies}')
print(f'history response response.history : {response.history}')
print(f'is_permanent_redirect response response.is_permanent_redirect : {response.is_permanent_redirect}')
print(f'is_redirect response response.is_redirect : {response.is_redirect}')
print(f'URL response response.URL : {response.url}')

fakestore_response_result = response.json()
print(f'fakestore rating {fakestore_response_result}')


#### INPUT
# fetch('https://fakestoreapi.com/users',{
#             method:"POST",
#             body:JSON.stringify(
#                 {
#                     email:'John@gmail.com',
#                     username:'johnd',
#                     password:'m38rmF$',
#                     name:{
#                         firstname:'John',
#                         lastname:'Doe'
#                     },
#                     address:{
#                         city:'kilcoole',
#                         street:'7835 new road',
#                         number:3,
#                         zipcode:'12926-3874',
#                         geolocation:{
#                             lat:'-37.3159',
#                             long:'81.1496'
#                         }
#                     },
#                     phone:'1-570-236-7033'
#                 }
#             )
#         })
#             .then(res=>res.json())
#             .then(json=>console.log(json))

            # //output
            #     {id:21}


######################################################################
# urllib3
######################################################################

# it's unended loop
# import json
# import urllib3

# while True:
#     ip = input("Enter Ip Address : ")
#     url = "http://ip-api.com/json/"
#     http = urllib3.PoolManager()
#     response = http.request('GET', url + ip)
#     data = response.data
#     values = json.loads(data)
#     print(values)

import urllib3
import json
http = urllib3.PoolManager()
fakestore_response_url = http.request(
    'Get',
    'https://fakestoreapi.com/products')

fakestore_response_result = fakestore_response_url.data
fakestore_response_url_price = json.loads(fakestore_response_result)[0]['title']
print(f'fakestore rating {fakestore_response_url_price}')





# ????
#     @backoff.on_exception(
#         backoff.expo,
#         (requests.exceptions.RequestException, requests.exceptions.HTTPError),
#         on_backoff=sleep,
#         max_time=30,
#     )
#     def create_mergado_query(self, access_token: str, project_id: int, name: str, mql: str) -> List[str]:
#         """
#             Downloads and returns all mergado products for given query
#         """
#         mergado_query_response: Response = requests.post(
#             f'https://api.mergado.com/projects/{project_id}/queries/',
#             data=json.dumps({
#                 "name": name,
#                 "query": mql,
#                 "read_only": False,
#                 "search_output": True
#             }),
#             headers={
#                 "Accept": "application/json",
#                 "Authorization": f"Bearer {access_token}",
#                 'Content-Type': 'application/json'
#             },
#         )

#         if mergado_query_response.status_code > 499:
#             mergado_query_response.raise_for_status()

#         return mergado_query_response
