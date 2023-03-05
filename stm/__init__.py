from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Старт")


@app.route("/table")
def get_table():
    return render_template(
        "table.html",
        title="Таблица данных",
        table=[
            ["ID", "Sensor", "Location", "Value", "Timestamp"],
            [1, "AN", 2, 3, "03.03.2023"],
            [2, "AN", 2, 10, "05.03.2023"],
        ],
    )


if __name__ == "__main__":
    app.run()
