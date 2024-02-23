import re
import os
import requests
import colorama

colorama.init()

clear_command = "cls" if os.name == "nt" else "clear"

while True:
    os.system(clear_command)
    print(colorama.Fore.GREEN + "[IP Scan]: " + colorama.Fore.LIGHTYELLOW_EX + "Type the IP address to scan (type 'exit' to quit):")
    ip = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)

    if ip.lower() == 'exit':
        break

    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    p = re.compile(regex)

    if re.search(p, ip):
        url = 'https://ipapi.co/' + ip + '/json/'
        req = requests.get(url)
        result = req.json()

        if len(result) == 5:
            os.system(clear_command)
            print(colorama.Fore.GREEN + "\n[IP Scan]: " + colorama.Fore.RED + f"{str(result['reason'])}\n")
            print(colorama.Fore.YELLOW + f"IP: {colorama.Fore.LIGHTWHITE_EX+str(result['ip'])}\n"
                  + colorama.Fore.YELLOW + f"Type: {colorama.Fore.LIGHTWHITE_EX+str(result['version'])}")
        else:
            os.system(clear_command)
            print(colorama.Fore.YELLOW + f"IP: {colorama.Fore.LIGHTWHITE_EX+str(result['ip'])}\n"
                  + colorama.Fore.YELLOW + f"Network: {colorama.Fore.LIGHTWHITE_EX+str(result['network'])}\n"
                  + colorama.Fore.YELLOW + f"Type: {colorama.Fore.LIGHTWHITE_EX+str(result['version'])}\n"
                  + colorama.Fore.YELLOW + f"Country: {colorama.Fore.LIGHTWHITE_EX+str(result['country_name'])}\n"
                  + colorama.Fore.YELLOW + f"Country Code: {colorama.Fore.LIGHTWHITE_EX+str(result['country'])}\n"
                  + colorama.Fore.YELLOW + f"Country Phone: {colorama.Fore.LIGHTWHITE_EX+str(result['country_calling_code'])}\n"
                  + colorama.Fore.YELLOW + f"Country Tld: {colorama.Fore.LIGHTWHITE_EX+str(result['country_tld'])}\n"
                  + colorama.Fore.YELLOW + f"Region: {colorama.Fore.LIGHTWHITE_EX+str(result['region'])}\n"
                  + colorama.Fore.YELLOW + f"City: {colorama.Fore.LIGHTWHITE_EX+str(result['city'])}\n"
                  + colorama.Fore.YELLOW + f"Asn: {colorama.Fore.LIGHTWHITE_EX+str(result['asn'])}\n"
                  + colorama.Fore.YELLOW + f"Org: {colorama.Fore.LIGHTWHITE_EX+str(result['org'])}\n"
                  + colorama.Fore.YELLOW + f"Timezone: {colorama.Fore.LIGHTWHITE_EX+str(result['timezone'])} ({colorama.Fore.LIGHTWHITE_EX+str(result['utc_offset'])})\n"
                  + colorama.Fore.YELLOW + f"Currency:  {colorama.Fore.LIGHTWHITE_EX+str(result['currency_name'])}\n"
                  + colorama.Fore.YELLOW + f"Country Population: {colorama.Fore.LIGHTWHITE_EX+str(result['country_population'])}\n"
                  + colorama.Fore.YELLOW + f"Languages: {colorama.Fore.LIGHTWHITE_EX+str(result['languages'])}\n"
                  + colorama.Fore.YELLOW + f"Postal: {colorama.Fore.LIGHTWHITE_EX+str(result['postal'])}\n"
                  + colorama.Fore.YELLOW + f"Location: {colorama.Fore.LIGHTWHITE_EX+'https://google.com/maps/place/'+str(result['latitude'])},{str(result['longitude'])} ({str(result['latitude'])},{str(result['longitude'])})")

        input(colorama.Fore.GREEN + "[IP Scan]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")
