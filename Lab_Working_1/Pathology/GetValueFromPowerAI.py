import sys
import urllib3
import json
import requests
import os
from Pathology.views import *

urllib3.disable_warnings()

# import sys
# print(sys.argv[1:])
# file_name = sys.argv[1]
# print(file_name)

# a =   Lab_Api.objects.all()

# POWER_AI_VISION_API_URL = "https://10.150.20.65/powerai-vision/api/dlapis/73ba9966-b631-4ea9-86e7-16a063a864a9"


def detect_image_label(file_name, url):
    print("in Main Function")
    print('=============================', file_name)
    print(os.getcwd())
    rc11 = 0
    retry_count = 0
    label_value = ''
    confidence = 0
    result = ''
    while (rc11 != 200) and (retry_count < 5):
        # print("retry_count=%d" % retry_count)
        if retry_count != 0:
            print("retrying upload for  attempt %d" % retry_count)

        try:
            with open(file_name, 'rb') as f:
                # WARNING! verify=False is here to allow an untrusted cert!
                print('in try')
                s = requests.Session()
                r = s.post(url, files={'files': (file_name, f), 'containHeatMap': 'true'}, verify=False, timeout=10)
                print('r\t', r.text)
                # print(json.loads(r.text))
            data = json.loads(r.text)
            print('data\t', data)
            # print(data["result"])
            result = data["result"]
            heatmap = data['heatmap']
            print('heatmap', heatmap)
            # print(result)
            data_label = data["classified"]
            print("data_label", data_label)
            for label, val in data_label.items():
                confidence = float(val)
                confidence = confidence * 100
                print(label + "," + str(confidence))
                label_value = label

            rc11 = r.status_code
            # print("status code = %d " %rc1)

            return result, label_value, confidence, heatmap

        except Exception as exc:
            print('generated an exception: %s' % exc)
            rc1 = 0
            retry_count = retry_count + 1
            continue


# detect_image_label("F:\\Lab_Working_1\\media\\Patient_reports\\1_1_a_Xray.jpeg", POWER_AI_VISION_API_URL)
