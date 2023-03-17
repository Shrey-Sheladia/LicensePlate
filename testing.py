import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)

headers = {     'method': 'GET',
                'scheme': "https",
                'cookie': 'Cookie: MYUCDAVIS_LANDING_IMAGE=bikesandtrees%2Ejpg; SAP_CASAUTH=3262A34FE73253C6E194CDFB556070D4E90B1A3291EE3A0286A9C8002F2EDFCC2E93A0905B5C205C208B9B692976672D3181023FC6B3D7AEE8F3862D1A2B05E820D83A8B4B6BAF01A33AFF62D940A475B7133FECA91A59CC169C184D1352F8D0',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'appversion': '251',
                'city': 'Delhi',
                'deviceid': 'fa6072a-4713-b11-c37-fc80a34fcb',
                'dnt': '1',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'src': 'car-info_web',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'userid': '63bddca28a78ec2da756a08a'}

# URL = f"https://web.cuvora.com/car/web/details/list?vehicle_num={plate}"
URL = "https://org.ucdavis.edu/directory-search/person?query=khushee"

r = requests.get(URL, headers=headers)

    
data = r.json()

for person in data:
    pp.pprint(data)
    print("\n\n\n")

