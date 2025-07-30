from flask import Flask
from models import Base, engine
from routes.ussd import ussd_blueprint

app = Flask(__name__)
app.register_blueprint(ussd_blueprint)

# Initialize DB tables
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(port=3000)
