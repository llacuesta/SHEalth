import os 
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from server_methods import *

# creating simple Flask app to receive requests
app = Flask(__name__)

# configuring database
load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
pub_ip = os.getenv('PUBLIC_IP') # change this host according to google cloud sql proxy
db_name = os.getenv('DATABASE_NAME')
port = os.getenv('PORT')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@{pub_ip}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# defining user model
class User(db.Model):
    __tablename__ = "users"
    __table_args__ = (db.UniqueConstraint('r_hash'), )
    id = db.Column(db.Integer, primary_key=True)
    r_hash = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    first_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False) 
    middle_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    birthday = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    age = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    birthplace = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    income = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    sex = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    civil = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    citizenship = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    dependent = db.relationship('Dependent', backref="users", lazy=True, uselist=False) # dependent reference

    def __init__(self, r_hash, last_name, first_name, middle_name, birthday, age, birthplace, income, sex, civil, citizenship):
        self.r_hash = r_hash
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.age = age
        self.birthplace = birthplace
        self.income = income
        self.sex = sex
        self.civil = civil
        self.citizenship = citizenship

# defining dependent model
class Dependent(db.Model):
    __tablename__ = "dependents"
    id = db.Column(db.Integer, primary_key=True)
    r_hash = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    first_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False) 
    middle_name = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    birthday = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    relationship = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    citizenship = db.Column(db.LargeBinary(length=(2**24)-1), nullable=False)
    user_id = db.Column(db.String(64), db.ForeignKey('users.r_hash'), nullable=False) # foreign key to user

    def __init__(self, r_hash, last_name, first_name, middle_name, birthday, relationship, citizenship, user_id):
        self.r_hash = r_hash
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.relationship = relationship
        self.citizenship = citizenship
        self.user_id = user_id

# creating all required tables
with app.app_context():
    db.create_all()
# empty server instance
HE_server = HEServer()

# routes
@app.route('/send-context', methods=['POST'])
def receive_client_context():
    global HE_server
    print('Request Received')

    # initializing HE_server
    HE_server.generate_from_context(
        request.json.get('context').encode('cp437'),
        request.json.get('pubKey').encode('cp437')
    )

    # testing operation for client validation
    if HE_server:
        print(HE_server)
        return HE_server.validate_instance(
            request.json.get('cx').encode('cp437'),
            request.json.get('cy').encode('cp437')
        )
    else:
        return json.dumps({
            "success": False,
            "message": "Unable to generate HE server."
        })
@app.route('/save-data', methods=['POST'])
def store_user_info():
    print('Saving data...')

    data = request.json
    try: 
        user_hash = data.get('user_hash')
        last_name = data.get('last_name').encode('cp437')
        first_name = data.get('first_name').encode('cp437')
        middle_name = data.get('middle_name').encode('cp437')
        birthday = data.get('birthday').encode('cp437')
        age = data.get('age').encode('cp437')
        birthplace = data.get('birthplace').encode('cp437')
        income = data.get('income').encode('cp437')
        sex = data.get('sex').encode('cp437')
        civil = data.get('civil').encode('cp437')
        citizenship = data.get('citizenship').encode('cp437')

        dependent_data = data.get('dependent')
        if dependent_data:
            dep_hash = dependent_data.get('dep_hash')
            dep_last_name = dependent_data.get('last_name').encode('cp437')
            dep_first_name = dependent_data.get('first_name').encode('cp437')
            dep_middle_name = dependent_data.get('middle_name').encode('cp437')
            dep_birthday = dependent_data.get('bday').encode('cp437')
            dep_relationship = dependent_data.get('relationship').encode('cp437')
            dep_citizenship = dependent_data.get('citizenship').encode('cp437')

            # adding user
            new_user = User(user_hash, last_name, first_name, middle_name, birthday, age, birthplace, income, sex, civil, citizenship)
            db.session.add(new_user)
            db.session.commit() # commit add user

            # adding dependent
            new_dependent = Dependent(dep_hash, dep_last_name, dep_first_name, dep_middle_name, dep_birthday, dep_relationship, dep_citizenship, new_user.r_hash)
            db.session.add(new_dependent)
            db.session.commit()
        else:
            raise Exception("No dependent provided")
        
        print("Data saved")
        return json.dumps({ "success": True })
    except Exception as e:
        print("Something went wrong. Rolling back...")
        db.session.rollback()
        return json.dumps({ "success": False, "message": str(e) })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)