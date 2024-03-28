from flask import Flask, request

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    random_value = data['value']
    print("Received value:", random_value)
    # Do something with the received data here
    return "Data received successfully"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
