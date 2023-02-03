from flask import Flask, render_template
import pandas as pd

data = pd.read_csv("dictionary.csv")

website = Flask(__name__)


@website.route("/")
def home():
	return render_template("index.html")


@website.route("/dict/v1.4/<word>/")
def web_word(word):
	definition = data.loc[data["word"] == word]["definition"].squeeze()
	return {"definition": str(definition).strip("\n"),
	        "word": word}


website.run(debug=True, port=5478)
