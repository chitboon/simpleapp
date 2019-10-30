from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
import shelve, User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def createUser():
    createUserForm = CreateUserForm(request.form)
    if request.method == 'POST' and createUserForm.validate():
        usersDict = {}
        db = shelve.open('storage.db', 'c')

        try:
            usersDict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(createUserForm.firstName.data, createUserForm.lastName.data, createUserForm.membership.data, createUserForm.gender.data, createUserForm.remarks.data)
        usersDict[user.get_userID()] = user
        db['Users'] = usersDict

        # Test codes
        usersDict = db['Users']
        user = usersDict[user.get_userID()]
        print(user.get_firstName(), user.get_lastName(), "was stored in shelve successfully with userID =", user.get_userID())

        db.close()

        return redirect(url_for('home'))
    return render_template('createUser.html', form=createUserForm)

if __name__ == '__main__':
    app.run()
