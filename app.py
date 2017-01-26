from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
	return "World's Best Blorg"

if __name__ == "__main__":
	app.run()