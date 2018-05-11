from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)