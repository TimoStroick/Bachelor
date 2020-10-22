import http.client, urllib.request, urllib.parse, urllib.error, base64, json


# Hier wird ein Zitat von dem Microsoft Academic Graph gesucht
# mittels des titels der schon auf kleinschreibung und Sonderzeichen angepasst wurde
# Die Rückgabe ist entweder die json Antwort oder none
def sucheZitate(titel):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'd887095bc04a4a04b446fdb9445bff8e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'latest',
        'count': '10',
        'offset': '0',
        'attributes': 'CitCon',
    })

    titel = urllib.parse.quote(titel)
    expr = "Ti='" + titel + "'"
    query = "/academic/v1.0/evaluate?expr={expr}&%s"% params
    query = query.format(expr=expr)

    try:
        conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
        conn.request("GET", query, None, headers)
        response = conn.getresponse()
        data = response.read()
        js = json.loads(data)
        conn.close()
        return js
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return None;



# Hier wird ein Titel von dem Microsoft Academic Graph gesucht
# mittels der paperid,also der id aus dem MAG
# Die Rückgabe ist entweder die json Antwort oder none
def sucheTitel(paperid):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'd887095bc04a4a04b446fdb9445bff8e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'latest',
        'count': '10',
        'offset': '0',
        'attributes': 'DN',
    })

    titel = urllib.parse.quote(paperid)
    expr = "Id=" + paperid + ""
    query = "/academic/v1.0/evaluate?expr={expr}&%s" % params
    query = query.format(expr=expr)

    try:
        conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
        conn.request("GET", query, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        js = json.loads(data)
        return js
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return None
