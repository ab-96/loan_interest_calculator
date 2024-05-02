from distutils import debug
from flask import Flask, render_template, request
from loan_interest_calculator import calculate_total_interest  # Import the function
import datetime

app = Flask(__name__, static_url_path='/static')
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    total_interest = None  # Initialize to None by default

    if request.method == "GET":
        # No initial values set here (use user input)
        return render_template("index.html", total_interest=total_interest)
    else:
        # Extract user input from form data
        land_advance = int(request.form["landAdvance"])
        monthly_rate = float(request.form["monthlyRate"]) # Convert to decimal
        default_period_start_str = request.form["defaultPeriodStart"]
        default_period_end_str = request.form["defaultPeriodEnd"]
        

        # Parse date strings into datetime objects
        default_period_start = datetime.datetime.strptime(default_period_start_str, "%Y-%m-%d").date()
        default_period_end = datetime.datetime.strptime(default_period_end_str, "%Y-%m-%d").date()

        # Call function to calculate interest
        total_interest = calculate_total_interest(land_advance, monthly_rate,
                                                   default_period_start, default_period_end)
        
     

        return render_template("index.html", land_advance=land_advance,
                               monthly_rate=monthly_rate,
                               default_period_start_str=default_period_start_str,
                               default_period_end_str=default_period_end_str,
                               total_interest=total_interest)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    

