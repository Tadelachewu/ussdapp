from flask import Blueprint, request, make_response
from services.menu_service import handle_ussd

ussd_blueprint = Blueprint('ussd', __name__)

@ussd_blueprint.route("/ussd", methods=["POST"])
def ussd():
    text = request.form.get("text", "")
    phone = request.form.get("phoneNumber")

    response = handle_ussd(text, phone)

    res = make_response(response, 200)
    res.headers['Content-Type'] = 'text/plain'
    return res
