from services.loan_service import handle_loan_application

def handle_ussd(text, phone_number):
    user_input = text.split("*")

    if text == "":
        return "CON Welcome to AI Loan Service\n1. Apply for Loan\n2. Exit"

    if user_input[0] == "1":
        if len(user_input) == 1:
            return "CON Enter loan amount:"
        elif len(user_input) == 2:
            return handle_loan_application(phone_number, user_input[1])

    elif user_input[0] == "2":
        return "END Thank you. Goodbye."

    return "END Invalid choice."
