import requests

# This could be a file somewhere you log a ton of IPs scanning/hitting your exterior network, or IPs that do weird stuff on the inside of your network :-) 
ips = ["113.120.9.25", "139.200.49.234", "61.153.83.236"]

headers = {"Accept": "application/json"}

for ip in ips:
    url = "https://api.greynoise.io/v3/community/" + ip
    response = requests.request("GET", url, headers=headers)
    print(response.text)
