from flask import Flask, json, jsonify, request

dummyData = [
    {
        'id': 1,
        'Environment': 'Dev',
        'Department': 'Linux Internal',
        'Application': 'others',
        'Index': 1,
        'Type': 'virtual',
        'Data Centre' : 'RDC',
        'HDD' : '100',
        'CPU' : '1',
        'RAM' : '4'
    },

    {
        'id': 2,
        'Environment': 'DR',
        'Department': 'Internet Banking',
        'Application': 'Webserver',
        'Index': 2,
        'Type': 'virtual',
        'Data Centre' : 'RDC',
        'HDD' : '100',
        'CPU' : '1',
        'RAM' : '4'
    },

    {
        'id': 3,
        'Environment': 'Prod',
        'Department': 'AAM',
        'Application': 'HANA',
        'Index': 1,
        'Type': 'virtual',
        'Data Centre' : 'SDC',
        'HDD' : '100',
        'CPU' : '2',
        'RAM' : '8'
    }
]


serverapi = Flask(__name__)

@serverapi.route('/', methods=['GET'])
def get_data():
    return jsonify(message = dummyData)


if __name__ == '__main__':
    serverapi.run(port=4000)