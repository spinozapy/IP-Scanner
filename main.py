import shutil
from urllib import request
import colorama
import os
import json 
import re

colorama.init()
os.system("cls")

while True: 
    print(colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN + "[IP Scan]: " + colorama.Fore.LIGHTYELLOW_EX + "Type the IP address to scan.")
    ip = input(colorama.Style.RESET_ALL+"root@you:~$ " + colorama.Fore.LIGHTBLUE_EX + "")

    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    p = re.compile(regex)

    if (re.search(p, ip)):
        url = 'https://ipapi.co/' + ip + '/json/'
        req = request.Request(url)
        response = request.urlopen(req)
        result = json.loads(response.read().decode("utf-8"))

        if len(result) == 5:
            os.system("cls")
            print(colorama.Fore.RED+f"\n\033[1;3m[IP Scan - ERROR]: {str(result['reason'])}\033[0m\n\n"+
                colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· IP: {colorama.Fore.LIGHTWHITE_EX+str(result['ip'])}\n"+
                colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Type: {colorama.Fore.LIGHTWHITE_EX+str(result['version'])}")

        else:
            os.system("cls")
            print(colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· IP: {colorama.Fore.LIGHTWHITE_EX+str(result['ip'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Network: {colorama.Fore.LIGHTWHITE_EX+str(result['network'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Type: {colorama.Fore.LIGHTWHITE_EX+str(result['version'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Country: {colorama.Fore.LIGHTWHITE_EX+str(result['country_name'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Country Code: {colorama.Fore.LIGHTWHITE_EX+str(result['country'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Country Phone: {colorama.Fore.LIGHTWHITE_EX+str(result['country_calling_code'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Country Tld: {colorama.Fore.LIGHTWHITE_EX+str(result['country_tld'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Region: {colorama.Fore.LIGHTWHITE_EX+str(result['region'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· City: {colorama.Fore.LIGHTWHITE_EX+str(result['city'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Asn: {colorama.Fore.LIGHTWHITE_EX+str(result['asn'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Org: {colorama.Fore.LIGHTWHITE_EX+str(result['org'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Timezone: {colorama.Fore.LIGHTWHITE_EX+str(result['timezone'])} ({colorama.Fore.LIGHTWHITE_EX+str(result['utc_offset'])})\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Currency:  {colorama.Fore.LIGHTWHITE_EX+str(result['currency_name'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Country Population: {colorama.Fore.LIGHTWHITE_EX+str(result['country_population'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Languages: {colorama.Fore.LIGHTWHITE_EX+str(result['languages'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Postal: {colorama.Fore.LIGHTWHITE_EX+str(result['postal'])}\n"+
                  colorama.Fore.LIGHTBLUE_EX+f"\033[1;3m· Location: {colorama.Fore.LIGHTWHITE_EX+'https://google.com/maps/place/'+str(result['latitude'])},{str(result['longitude'])} ({str(result['latitude'])},{str(result['longitude'])})")

    else:
        print(colorama.Fore.WHITE + "[IP Scan]: " + colorama.Fore.RED + "IP address is incorrect.")
