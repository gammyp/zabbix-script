import urllib.request, json, ssl

jsonData = ""
data = ""
request = ""

def getData(jsonData):
    request = urllib.request.urlopen("https://api.wip.camp/api/v1/profiles")
    jsonData = request.read()
    return jsonData

def deCodejSon(jsonData):
    data = json.loads(jsonData)
    return data

getData(jsonData)
print(jsonData)