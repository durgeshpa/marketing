import requests
import json

url = "https://indiaapi.stg.sekel.tech/store/tertiary-category/"

payload = json.dumps({
  "name": "gold plated",
  "image_url": "",
  "display_name": "gold plated jewel",
  "description": "test",
  "secondary_category_id": "5334916849729536",
  "created_by": "b15cbae3-af8a-48d5-8546-4bd990561911",
  "updated_by": "b15cbae3-af8a-48d5-8546-4bd990561911",
  "brand_id": "977ffe5e-3be8-49e1-bac0-adc79065cbc3"
})
headers = {
  'authority': 'indiaapi.stg.sekel.tech',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,te;q=0.7',
  'authorization': 'Bearer',
  'content-type': 'application/json',
  'cookie': '_hjSessionUser_3466791=eyJpZCI6IjhjZjY2YzM0LWU4N2QtNWRkOC04NmE5LTY0NGUwNTVmNjg2NCIsImNyZWF0ZWQiOjE2OTIyNDc0NzU2ODQsImV4aXN0aW5nIjp0cnVlfQ==; _ga_0V6Z57RHZ7=GS1.1.1702540339.3.0.1702540339.0.0.0; _ga_1YFE1ZK40C=GS1.1.1703224991.47.0.1703224994.0.0.0; _ga_H6YV1LDG7Y=GS1.1.1708021972.116.0.1708021972.0.0.0; _ga=GA1.2.294651291.1686813328; _ga_PFK6CHF8WL=GS1.1.1710910135.6.0.1710910135.0.0.0; _gid=GA1.2.994356456.1711949616',
  'origin': 'https://dashboard.stg.sekel.tech',
  'referer': 'https://dashboard.stg.sekel.tech/',
  'region-api-url': 'https://indiaapi.stg.sekel.tech',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
  'x-authenticated-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImIxNWNiYWUzLWFmOGEtNDhkNS04NTQ2LTRiZDk5MDU2MTkxMSIsInVzZXJuYW1lIjoic3VkaGFuc2h1LmdvdXJAc2VrZWwudGVjaCIsIm5hbWUiOiJTdWRoYW5zaHUiLCJhY2Nlc3NfdG9rZW4iOiIiLCJlbnRpdHlfaWRzIjpbIiJdLCJlbnRpdHlfdHlwZSI6ImludGVybmFsIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJicmFuZF9pZCI6Ik5vbmUiLCJleHAiOjE3MTIyMDUzMTl9.C_ePby4Jo-dSy3a_BDUVsffILHWpj_bBqNQ4Q5uVNFI'
}
j =0
for i in range(4800):
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code!=500:
        break;


