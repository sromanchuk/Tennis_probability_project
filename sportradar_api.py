import http.client
import xmltodict
import json

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/tennis-t2/en/players/sr:competitor:18111/versus/sr:competitor:15126/matches.xml?api_key=8vfgwpuch3rpnauqm9cbzp7d")

res = conn.getresponse()
data = res.read()

xml_data = data.decode("utf-8")
json_data = xmltodict.parse(xml_data)
print(json.dumps(json_data, indent=2))