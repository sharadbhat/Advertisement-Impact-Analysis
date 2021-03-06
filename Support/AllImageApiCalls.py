import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import ast
import os
import cv2
import time
import glob
import filemapper as fm

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '************************',
}

params = urllib.parse.urlencode({
})

allfiles = fm.load('Images')
# Replace the example URL below with the URL of the image you want to analyze.
for eachFile in allfiles:
    body = open("Images/" + eachFile, "rb").read()
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        b = data.decode("utf-8") #bytes to string conversion
        c = ast.literal_eval(b) #string to list conversion
        print(c[0]['scores']) #parsing
        conn.close()
    except Exception as e:
        print(e.args)
    time.sleep(3)
