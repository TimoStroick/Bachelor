import http.client, urllib.request, urllib.parse, urllib.error, base64, json

def sucheZitate(titel):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'd887095bc04a4a04b446fdb9445bff8e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'latest',
        'attributes': 'AA.AfN,CitCon',
        'count': '10',
        'offset': '0',
    })

    expr = "Composite(DN=='" +  titel + "')"
    query = "/academic/v1.0/calchistogram?expr={expr}&%s".format(expr=expr) % params
    query = urllib.parse.quote(query)

    try:
        conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
        conn.request("GET", query, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        js = json.loads(data)
        print(json.dumps(js["histograms"][""], indent=3))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def sucheTitel(titelid):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'd887095bc04a4a04b446fdb9445bff8e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'latest',
        'attributes': 'DN',
        'count': '10',
        'offset': '0',
    })

    expr = "Composite(Ti=='" + titelid + "')"
    query = "/academic/v1.0/calchistogram?expr={expr}&%s".format(expr=expr) % params
    query = urllib.parse.quote(query)

    try:
        conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
        conn.request("GET", query, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        js = json.loads(data)
        print(json.dumps(js["histograms"][""], indent=3))
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
