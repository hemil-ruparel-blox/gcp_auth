from flask import Flask, request
from base64 import b64decode

app = Flask(__name__)

@app.route("/")
@app.route("/<path:path>")
def hello_world(*args, **kwargs):
    print("headers: ")
    print(dict(request.headers))

    print(f'Authorization: {request.headers.get("Authorization")}')
    print(f'X-Apigateway-Api-Userinfo: {request.headers.get("X-Apigateway-Api-Userinfo")}')
    print(f'X-Apigateway-Api-Userinfo decoded: {b64decode(request.headers.get("X-Apigateway-Api-Userinfo", ""))}')

    print("body: ")
    print(request.data)

    return {
        'headers': dict(request.headers)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0')