import http.client
import json


def get_json(source):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", source)
    res = conn.getresponse()
    json_data = res.read().decode("utf-8")
    json_data = json.loads(json_data)
    return json_data


json_data = get_json("/tennis-t2/en/players/sr:competitor:18111/versus/sr:competitor:15126/matches.json?api_key=8vfgwpuch3rpnauqm9cbzp7d")
json_data = json.dumps(json_data, indent=2)
print(json_data)
