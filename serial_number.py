__author__ = 'cobedien'

import requests
import json
import apic_login
import constant
from prettytable import PrettyTable


def serial_number():

    token = apic_login.aaaLogin()

    try:
        response = requests.get(
            url=constant.APIC_URL + "/api/node/class/topSystem.json",
            headers={
                    "Cookie": "APIC-cookie=" + token, "Content-Type": "application/json; charset=utf-8",
            },
        )

        structured_data = json.loads(response.text)
        fields = ['name', 'role', 'serial']
        data = []

        for endpoints in structured_data['imdata']:
            for endpoint_data in endpoints['topSystem'].items():
                line_dict={}
                for field in fields:
                    line_dict[field] = endpoint_data[1][field]
            data.append(line_dict)

        table = PrettyTable()
        table.field_names = ['Name','role','serial']

        for row in data:
            table.add_row([row['name'],row['role'],row['serial']])

        print table

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


serial_number()
