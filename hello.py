from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/homepage")
def hello():
    return render_template('homepage.html')

@app.route("/", methods=['GET', 'POST'])
def options():
    # return render_template('homepage.html')
    if request.method == 'POST':
        if request.form.get('movie') == 'Movies':
            return render_template('movies.html')
        elif request.form.get('fitness') == 'Health and Fitness':
            return render_template('fitness.html')
        elif request.form.get('order') == 'Online Shopping':
            return render_template('orders.html')
        else:
            return render_template('homepage.html')
    elif request.method == 'GET':
        print("Hi") 
    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(debug=True)





# @app.route("/")
# def home():
#     return render_template("homepage.html")

# @app.route("/")