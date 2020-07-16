import requests
from flask import Flask, json, jsonify, request

Environment = {'DR': 'r', 'Dev' : 'd', 'SIT' : 'sit', 'Prod' : 'p', 'UAT' : 'u'}
Department = {'SAP Core BW': 'bw', 'SAP Finance BW': 'fbw', 'Sap Core BA': 'ba', 'Sap Finance BA' : 'fba', 'SAP HRGRC': 'grc', 'SAP HR Human Capital Mobility' : 'hem', 'SBG Mobile' : 'sbg', 'AAM': 'aam', 'MCAF Tools': 'mca', 'Innovation Channel': 'mic', 'Linux Internal': 'lin', 'Internet Banking': 'ibr', 'Falcon': 'fal', 'SAP FSE': 'fse', 'PAS': 'pas', 'Hiport': 'hip'}
Application = {'SAP Online Banking': 'sapo', 'jbos': 'jbo', 'SAP BW': 'sapb', 'SAP CI' : 'sape', 'DB2': 'db', 'Oracle': 'ora', 'Sybase': 'syb', 'others': 'app', 'Webserver': 'web', 'LAMP': 'lamp', 'MySQL': 'sql', 'SAS': 'sas', 'abinitio': 'abi', 'HANA': 'hana', 'SAP Router': 'sapr', 'Sybase SCC': 'see' }
Node = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7: '7', 8:'8', 9:'9', 10:'10'}


url = 'http://127.0.0.1:4000/'

res = requests.get(url)

data = res.json()


envData = data['message'][1]['Environment']
depData = data['message'][1]['Department']
appData = data['message'][1]['Application']
nodeData = data['message'][1]['Index']
checkData = data['message'][0]

def env(envId):
    try:
       return Environment[envId]
    except KeyError:
        return "Invalid Environment entry."         


def dep(depId):
    try:
        return Department[depId]
    except KeyError:
        return "Invalid Department entry"


def app(appId):
    try:
       return Application[appId]
    except KeyError:
        return "Invalid Application entry."  


def node(nodeId):
    try:
       return Node[nodeId]
    except KeyError:
        return "Invalid Node number entry." 




#print(env(envData) + dep(depData) + app(appData) + node(nodeData) + 'v')
hostname = (env(envData) + dep(depData) + app(appData) + node(nodeData) + 'v')
#print(len(env('Dev') + dep('SBG Mobile') + app('others') + node(1) + 'v'))
#print(hostname)
#print(checkData)

checkData["hostname"] = hostname

with open("sample.tfvars.json", "w") as outfile:  
    json.dump(checkData, outfile) 



#dict(checkData)
print(checkData)
#print(env('Nothing'))
#print(len(Environment))
#print(Environment('Prod'))

