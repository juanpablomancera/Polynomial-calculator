from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
from polynomialCalculator import calculatePolynomial

app = Flask(__name__)

@app.route('/')
def formulary():
    return render_template("index.html")

@app.route('/ajax', methods=['POST'])
@cross_origin()
def respuesta_ajax():
    req_data = request.get_json()
    a = int(req_data['a'])
    b = int(req_data['b'])
    c = int(req_data['c'])
    x = int(req_data['x'])
    try:
        response = jsonify({"status":"ok","a": a, "b": b, "c":c, "x": x, 'result': calculatePolynomial(a,b,c,x)})
    except:
        response = jsonify({"status": "ko"})
        response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)