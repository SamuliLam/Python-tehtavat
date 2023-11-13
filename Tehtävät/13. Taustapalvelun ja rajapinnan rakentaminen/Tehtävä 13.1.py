from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/alkuluku")
def alkuluku():
    args = request.args
    luku = int(args.get("luku"))
    if luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                isPrime = False
                break
        else:
            isPrime = True
    else:
        isPrime = False

    response = {"Number": luku,
                "isPrime": isPrime}

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
