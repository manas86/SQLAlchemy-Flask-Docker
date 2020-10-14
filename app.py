from flask import Flask, render_template, request, send_file
from . import create_app, database
from .models import Registers
import csv


app = create_app()


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route('/form', methods=["POST"])
def form():
    title = "Thank You"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    project_name = request.form.get("project_name")
    database.add_instance(Registers, first_name=first_name, last_name=last_name, email=email, project_name=project_name)
    return render_template("thankyou.html", title=title, first_name=first_name, last_name=last_name)


@app.route('/showall', methods=["GET"])
def showall():
    title = "Display"
    data = database.get_limit(Registers)
    all_records = database.get_all(Registers)
    with open('/tmp/download.csv', 'w') as f:
        out = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = Registers.__table__.columns.keys()
        out.writerow(header)

        for rec in all_records:
            out.writerow([getattr(rec, c) for c in header])

    return render_template("display.html", title=title, data=data)


@app.route('/download')
def download_file():
    try:
        return send_file("/tmp/download.csv",
                         mimetype='text/csv',
                         attachment_filename='all_register.csv',
                         as_attachment=True)
    except Exception as e:
        return str(e)
