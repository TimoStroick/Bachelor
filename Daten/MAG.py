import http.client, urllib.request, urllib.parse, urllib.error, base64, json



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
        #'orderby': '{string}',
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




def sucheTitel(titelid):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'd887095bc04a4a04b446fdb9445bff8e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model': 'latest',
        'count': '10',
        'offset': '0',
        #'orderby': '{string}',
        'attributes': 'DN',
    })

    titel = urllib.parse.quote(titelid)
    expr = "Id=" + titelid + ""
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
