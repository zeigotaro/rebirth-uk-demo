from flask import Flask, render_template, jsonify, request
import json
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
renter_list = []
host_list = []

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/insurance')
def insurance():
    address = request.args.get('address', default='', type = str)
    name = request.args.get('name', default='', type = str)
    data = {'address': address, 'name': name }
    return render_template('insurance.html', data=data)

@app.route('/summary')
def summary():
    address = request.args.get('address', default='', type = str)
    name = request.args.get('name', default='', type = str)
    insured = request.args.get('insured', default='true', type = str)
    data = {'address': address, 'name': name, 'insurance': insured }
    return render_template('summary.html', data=data)
    
@app.route('/getRenters')
def getRenters():
    return jsonify(renter_list)

@app.route('/getHosts')
def getHosts():
    return jsonify(host_list)
    
@app.route('/clearHosts')
def clearHosts():
    host_list.clear()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/clearRenters')
def clearRenters():
    renter_list.clear()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/addRenter')
def addRenter():
    address = request.args.get('address', default='', type = str)
    name = request.args.get('name', default='', type = str)
    email = request.args.get('email', default='', type = str)
    renter_list.append({'name': name, 'address': address, 'email': email })
    policy_string = 'INSPOL' + str(random.randint(10000, 99999))
    return json.dumps({'success':True, 'policyNumber':policy_string}), 200, {'ContentType':'application/json'} 

@app.route('/addHost')
def addHost():
    address = request.args.get('address', default='', type = str)
    name = request.args.get('name', default='', type = str)
    email = request.args.get('email', default='', type = str)
    host_list.append({'name': name, 'address': address, 'email': email })
    policy_string = 'INSPOL' + str(random.randint(10000, 99999))
    return json.dumps({'success':True, 'policyNumber':policy_string}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)