import uuid
import shelve

class Member:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.first_name = ''
        self.last_name = ''
        self.gender = ''
        self.membership = ''
        self.remarks = ''

members = shelve.open('member')

# creates member and return the member object
def create_member(first_name, last_name, gender, membership, remarks):
    u = Member()
    u.first_name = first_name
    u.last_name = last_name
    u.gender = gender
    u.membership = membership
    u.remarks = remarks
    members[u.id] = u
    members.sync()
    return u


# retrieve all users
def get_all_members():
    member_list = []
    klist = list(members.keys())
    for key in klist:
        member_list.append(members[key])
    return member_list
