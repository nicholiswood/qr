# Import the necessary modules
from flask import Flask, render_template, request
from qrcode import make
import re

# Create a flask app
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

# Define a route for the generate page
@app.route("/generate", methods=["POST"])
def generate():
    # Get the input from the form
    input = request.form.get("input")

    # Make a QR code from the input
    qr = make(input)

    # Replace any non-alphanumeric characters in the input with underscores
    file_name = re.sub(r"\W+", "_", input)

    # Save the QR code as an image file with the input as the file name
    qr.save(f"static/{file_name}.png")

    # Render the generate.html template with the input and the QR code image
    return render_template("generate.html", input=input, qr=f"static/{file_name}.png")

# Run the app in debug mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
