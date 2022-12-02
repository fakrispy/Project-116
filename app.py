# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Aryan Tiwari" # write your name
    age = "13" # write your agesude


    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name1 = "Aryan Ti" # write your name
    age1 = "13" # write your age

    return render_template('index.html' , name1 = name1 , age1 = age1)


# define the route to mother webpage
def mother():

    name2 = "Aryan Ti" # write your name
    age2 = "13" # write your age

    return render_template('index.html' , name2 = name2 , age2 = age2)

# define the route to friends webpage


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
