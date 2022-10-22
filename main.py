# Import required modules
from lxml import html
import requests
from urllib.parse import urlparse
import json

url = "https://ipspeed.info/freevpn_sstp.php"
final = []

def screapper(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    for i in range(8,267,6):
        host_name = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i}]/text()')[0].split(":")
        location = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{int(i)-1}]/text()')
        ping = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{int(i)+2}]/text()')
        port = port_parser(tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i}]/text()')[0])
        uptime = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i+1}]/text()')
        final.append({"HOSTNAME": str(host_name[0]), "LOCATION": str(location[0]), "PING": str(ping[0]), "PORT": int(port), "UPTIME": str(uptime[0])})

    for i in range(289,530,6):
        host_name = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i}]/text()')[0].split(":")
        location = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{int(i)-1}]/text()')
        ping = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{int(i)+2}]/text()')
        port = port_parser(tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i}]/text()')[0])
        uptime = tree.xpath(f'/html/body/center/div[6]/div[3]/div[{i+1}]/text()')
        final.append({"HOSTNAME": str(host_name[0]), "LOCATION": str(location[0]), "PING": str(ping[0]), "PORT": int(port), "UPTIME": str(uptime[0])})

    return final

def port_parser(urll):
    o = urll.split(":")
    try:
        return int(o[-1])
    except:
        return int(443)

def write(data):
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

write(screapper(url))