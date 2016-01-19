#create a map of user, password
#encrypt password
#prompt for user input
#encrypt the password
#check if encrypted password matches for user
# if yes - Welcome!
# else - I dont know you

import bcrypt

dumbSalt = "dude"

users = {"mac" : bcrypt.hashpw("password", bcrypt.gensalt())}

user = raw_input("name?" );
pwd = raw_input("pwd? ");

if bcrypt.hashpw(pwd, users[user]) == users[user]:
    print "welcome!"
else:
    print "nope!"
