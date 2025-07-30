from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/ussd", methods=["POST"])
def ussd():
    session_id = request.form.get("sessionId")
    phone_number = request.form.get("phoneNumber")
    text = request.form.get("text", "")
    print(f"Session ID: {session_id}, Phone Number: {phone_number}, Text: {text}")

    # Split the text by '*' to track user inputs through steps
    user_response = text.split('*')

    if text == "":
        # First interaction - show main menu
        response = "CON Welcome to XBank Lending\n"
        response += "1. Apply for Loan\n"
        response += "2. Exit"
    
    elif user_response[0] == "1":
        # Lending flow
        if len(user_response) == 1:
            # Ask for loan amount
            response = "CON Enter loan amount you want to apply for:"
        
        elif len(user_response) == 2:
            loan_amount = user_response[1]
            # Check if loan_amount is a number and within limits
            if not loan_amount.isdigit():
                response = "END Invalid amount. Please enter a number next time."
            else:
                loan_amount = int(loan_amount)
                if loan_amount <= 0:
                    response = "END Loan amount must be greater than 0."
                elif loan_amount > 10000:
                    response = "END Sorry, max loan amount is 10,000 ETB."
                else:
                    # Simulate loan approval
                    response = f"END Your loan of {loan_amount} ETB has been approved! Thank you for choosing XBank."
        else:
            # More than expected inputs
            response = "END Invalid input. Please try again."

    elif user_response[0] == "2":
        # Exit option
        response = "END Thank you for using XBank Lending. Goodbye!"
    
    else:
        response = "END Invalid option. Please try again."

    res = make_response(response, 200)
    res.headers["Content-Type"] = "text/plain"
    return res

if __name__ == "__main__":
    app.run(port=5000)
