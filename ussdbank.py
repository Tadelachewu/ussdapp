from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    session_id = request.form.get("sessionId")
    phone_number = request.form.get("phoneNumber")
    text = request.form.get("text", "")

    if text == "":
        response = "CON Welcome to XBank\n1. Check Balance\n2. Exit"
    elif text == "1":
        response = "END Your balance is 500 ETB"
    elif text == "2":
        response = "END Thank you for using XBank!"
    else:
        response = "END Invalid option"

    res = make_response(response, 200)
    res.headers["Content-Type"] = "text/plain"
    return res

if __name__ == "__main__":
    app.run(port=3000)
