from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("notes.db")
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("notes.db")
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            conn.execute("INSERT INTO notes (content) VALUES (?)", (note,))
            conn.commit()
        return redirect("/")
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return render_template("index.html", notes=notes)

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("notes.db")
    conn.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
