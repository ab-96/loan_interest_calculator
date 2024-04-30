from flask import Flask, render_template, request
from loan_interest_calculator import calculate_total_interest  # Import the function
import datetime

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # No initial values set here (use user input)
        return render_template("index.html", total_interest=None)
    else:
        # Extract user input from form data
        land_advance = int(request.form["landAdvance"])
        monthly_rate = float(request.form["monthlyRate"])
        default_period_start_str = request.form["defaultPeriodStart"]
        default_period_end_str = request.form["defaultPeriodEnd"]

        # Parse date strings into datetime objects
        default_period_start = datetime.datetime.strptime(default_period_start_str, "%Y-%m-%d").date()
        default_period_end = datetime.datetime.strptime(default_period_end_str, "%Y-%m-%d").date()


        # Call function to calculate interest (unchanged)
        total_interest = calculate_total_interest(land_advance, monthly_rate,
                                                   default_period_start, default_period_end)

        return render_template("index.html", land_advance=land_advance,
                               monthly_rate=monthly_rate,
                               default_period_start_str=default_period_start_str,
                               default_period_end_str=default_period_end_str,
                               total_interest=total_interest)


if __name__ == "__main__":
    app.run(debug=True)  # Use debug mode for live reloading