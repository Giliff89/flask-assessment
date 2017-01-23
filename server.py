from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)

jobs = ["QA Engineer", "Software Engineer", "Product Manager"]

# Required to use Flask sessions and the debug toolbar
app.secret_key = "98vy78wtbvn934x98f4vner9nui989f5v5r2jhed"


@app.route('/')
def homepage():
    """Homepage for application form"""

    return render_template("index.html")


@app.route('/application-form', methods=["GET"])
def application():
    """Brings user to the job application form"""

    return render_template("application-form.html", job_list=jobs)


@app.route('/application-success', methods=["POST"])
def submission():
    """Submits user application and displays successful form submission"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    job = request.form.get("job")
    salary = request.form.get("salaryreq")

    return render_template("application-response.html", first_name=first_name,
                           last_name=last_name, job=job, salary_requirement=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=8000)
