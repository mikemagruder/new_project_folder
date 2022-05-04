# importing the Flask class
from flask import Flask, render_template, redirect, request

# import the class from friend.py
from user import User

app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", all_users = users)


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
        }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/") #this is the same as saying localhost:5000/
# def index():
#     this_name = "Bob Ross"
#     name_list = [this_name, "Fred Rogers", "Mr T", "Bob Barker"]
#     return render_template("index.html", name=this_name, all_names=name_list)

# @app.route("/yo/<string:name>/<int:num>")
# def yo(name, num):
#     return f"Yo!!! {name * num}"

# @app.route("/users/<string:username>/<string:password>")
# def user(username, password):
#     print(username)
#     print(password)
#     return f"Hello, " + username + " Your password is: " + password

# @app.route("/mike") #this is the same as saying localhost:5000/
# def mike():
#     return 'Wow, this worked too!!! How cool!!!! Welcome to Mike`s Page!!!'

# @app.route("/hello/<string:name>")
# def say_hello(name):
#     return f"hi! welcome to {name}'s page!"

# @app.route("/<int:num_a>and<int:num_b>")
# def add_num(num_a, num_b):
#     return str(num_a+num_b)


# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     student_info = [
#         {'name' : 'Michael', 'age' : 35},
#         {'name' : 'John', 'age' : 30 },
#         {'name' : 'Mark', 'age' : 25},
#         {'name' : 'KB', 'age' : 27}
#         ]
#     return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

# if __name__=="__main__":
#      # are we directly running this file?
#      app.run(debug=True)


