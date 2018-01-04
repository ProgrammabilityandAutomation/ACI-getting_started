__author__ = 'cobedien'


import requests
import json
import constant

def aaaLogin():
    # Request
    # POST https://dp2-apic1.cisco.com/api/aaaLogin.json

    try:
        response = requests.post(
            url=constant.APIC_URL +"/api/aaaLogin.json",
            headers={
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "aaaUser": {
                    "attributes": {
                        "name": constant.USERNAME,
                        "pwd": constant.PASSWORD
                    }
                }
            })
            , verify=False)

        auth = json.loads(response.text)
        login_attributes = auth['imdata'][0]['aaaLogin']['attributes']

        token = login_attributes["token"]

        return token

        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException as ex:
        print('HTTP Request failed:' + ex)
