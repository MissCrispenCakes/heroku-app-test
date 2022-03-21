from flask import Flask, render_template
# request, flash
# from wtforms import Form, TextField, TextAreaField, validators, StringField

app = Flask(__name__)

@app.route("/") 
def index():
   
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
  
    # Render HTML with count variable
    return render_template("index.html", count=count)

# ButtonPressed = 0
# @app.route("/message", methods=["GET", "POST"])
# def messsage():
#     if request.method == "POST":
#         return render_template("message.html", ButtonPressed=ButtonPressed)
#         ButtonPressed = 1
#     return render_template("message.html", ButtonPressed=ButtonPressed)
        

if __name__ == "__main__":
    app.run()
