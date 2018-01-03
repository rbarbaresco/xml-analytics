from flask import Flask, jsonify
from flasgger import Flasgger, swag_from

app = Flask(__name__)
swagger = Flasgger(app)


@app.route('/')
@swag_from('schemas/definitions.yml')
def index():
    return 'Server is running!'


@app.route('/compare', methods=['POST'])
@swag_from('schemas/compare.yml')
def compare():
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
