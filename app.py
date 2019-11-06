from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
from persistence import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    form = CreateUserForm(request.form)
    if request.method == 'POST' and form.validate():
        member = create_member(form.firstName.data, form.lastName.data, form.gender.data, form.membership.data, form.remarks.data)
        # for debugging purpose
        print('created', member.id, member.first_name)
        return redirect(url_for('home'))
    return render_template('createUser.html', form=form)

@app.route('/retrieveUsers')
def retrieve_user():
    user_list = get_all_members()
    return render_template('retrieve_users.html', usersList = user_list, count=len(user_list))

if __name__ == '__main__':
    app.run()
