from models import SessionLocal, User, Loan
from ml.scoring import ai_score_loan

def handle_loan_application(phone_number, amount_input):
    db = SessionLocal()
    try:
        if not amount_input.isdigit():
            return "END Invalid amount entered."

        amount = int(amount_input)
        if amount <= 0 or amount > 10000:
            return "END Amount must be between 1 and 10,000 ETB."

        user = db.query(User).filter_by(phone_number=phone_number).first()
        if not user:
            user = User(phone_number=phone_number)
            db.add(user)
            db.commit()

        score = ai_score_loan(phone_number, amount)
        status = "APPROVED" if score > 70 else "REJECTED"

        loan = Loan(phone_number=phone_number, amount=amount, score=score, status=status)
        db.add(loan)
        db.commit()

        if status == "APPROVED":
            return f"END Loan of {amount} ETB approved!\nScore: {score:.1f}"
        else:
            return f"END Sorry, your score {score:.1f} is too low. Loan rejected."

    finally:
        db.close()
