from flask import Flask, render_template, request, jsonify
from quorumchallenge import get_oppose_count , get_support_count , get_bill_supporters , get_bill_opposers , query_by_bill , query_by_legislator

# flask server for the quorum challenge
app = Flask(__name__)

# route for the index page
@app.route('/')
def index():
  # return a json with data: "OK"
  return jsonify({'data': 'OK'})

# route for the support count
@app.route('/support/<legislator_name>')
def support(legislator_name):
  # return a json with data: support count
  return jsonify({'data': get_support_count(legislator_name)})

# route for the oppose count
@app.route('/oppose/<legislator_name>')
def oppose(legislator_name):
  # return a json with data: oppose count
  return jsonify({'data': get_oppose_count(legislator_name)})

# route for the bill supporters
@app.route('/bill/supporters/<bill_title>')
def bill_supporters(bill_title):
  # return a json with data: list of supporters
  return jsonify({'data': get_bill_supporters(bill_title)})

# route for the bill opposers
@app.route('/bill/opposers/<bill_title>')
def bill_opposers(bill_title):
  # return a json with data: list of opposers
  return jsonify({'data': get_bill_opposers(bill_title)})

# route for the query by bill
@app.route('/query/bill/<bill_title>')
def query_bill(bill_title):
  # return a json with data: query by bill
  return jsonify({'data': query_by_bill(bill_title).to_json(orient='records')})

# route for the query by legislator
@app.route('/query/legislator/<legislator_name>')
def query_legislator(legislator_name):
  # return a json with data: query by legislator
  return jsonify({'data': query_by_legislator(legislator_name).to_json(orient='records')})

# run the app
if __name__ == '__main__':
  app.run(debug=True)
#
# if __name__ == '__main__':
