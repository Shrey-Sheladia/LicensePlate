import requests
import pprint
import pyperclip
import json
import time


pp = pprint.PrettyPrinter(indent=4)


def getInfo(plate):
    plate = plate.upper().replace(" ", "")
    print(plate)

    headers =   {'authority': 'web.cuvora.com',
                'method': 'GET',
                'path': f'/car/web/details/list?vehicle_num={plate}',
                'scheme': "https",
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'appversion': '251',
                'city': 'Delhi',
                'deviceid': 'fa6072a-4713-b11-c37-fc80a34fcb',
                'dnt': '1',
                'origin': 'https://www.carinfo.app',
                'referer': 'https://www.carinfo.app/',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'src': 'car-info_web',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'userid': '63bddca28a78ec2da756a08a'}

    URL = f"https://web.cuvora.com/car/web/details/list?vehicle_num={plate}"

    r = requests.get(URL, headers=headers)

    if r.status_code != 200:
        return "Error", "Error"

    if 'errors' in r.json():
        return None, None
    
    

    

    data = r.json()['data']['data']


    f0 = data['rcDetails'][0]['data']['groups'][0]['fields']
    f1 = data['rcDetails'][0]['data']['groups'][1]['fields']
    f2 = data['rcDetails'][0]['data']['groups'][2]['fields']
    f3 = data['rcDetails'][0]['data']['groups'][3]['fields']



    vehicleInfo = {}

    for dict in f0:
        vehicleInfo[dict['name']] = dict['value']

    for dict in f1:
        vehicleInfo[dict['name']] = dict['value']

    for dict in f2:
        vehicleInfo[dict['name']] = dict['value']

    for dict in f3:
        vehicleInfo[dict['name']] = dict['value']

    mainInfo = {
        "Owner Name": vehicleInfo["Owner Name"],
        "Color": vehicleInfo["Color"],
        "Maker Model": vehicleInfo["Maker Model"]
    }

    secondaryInfo = {}

    for key, value in vehicleInfo.items():
        if key not in mainInfo:
            secondaryInfo[key] = value

    return mainInfo, secondaryInfo


if __name__ == "__main__":
    plateNum = "gj01vj7866"

    times = []


    info, info2= getInfo(plateNum)
    pp.pprint(info)
    pp.pprint(info2)



