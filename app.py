
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "10b1c96d2253fd41b79dd63bf4d5edbc"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city").strip()

        if city == "":
            weather = {"error": "Please enter city name"}
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            print(data)  # DEBUG

            if str(data.get("cod")) == "200":
                weather = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "desc": data["weather"][0]["description"]
                }
            else:
                weather = {"error": data.get("message", "City not found")}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
