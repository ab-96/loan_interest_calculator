import datetime


def calculate_total_interest(landAdvance, monthly_rate, defaultPeriodStart, defaultPeriodEnd):

    # start of the loan
    dateOfloan = datetime.date(2023, 1, 15)
    
    # fee that will be added to the landAdvancement
    arrangementFee = 5000

    openingPB = landAdvance + arrangementFee

    interestBalance = 20000
    isDefault = False
    dailyInterest = 0
    accrured_daily_interest = 0
    total_interest = 0
    dailyRate = monthly_rate / 30
    defaultRate = 2.000 / 30
    largest_interest = 0

    drawdowns = [
        (datetime.date(2023, 2, 14), 25000),
        (datetime.date(2023, 3, 25), 25000),
        (datetime.date(2023, 5, 3), 25000),
        (datetime.date(2023, 6, 11), 25000),
        (datetime.date(2023, 7, 20), 25000),
        (datetime.date(2023, 8, 28), 25000),
        (datetime.date(2023, 10, 6), 25000),
        (datetime.date(2023, 11, 14), 25000),
        (datetime.date(2023, 12, 23), 25000),
        (datetime.date(2024, 1, 31), 25000)
    ]

    repayments = [(datetime.date(2024, 2, 23), 100000)]

    accured_interest = []

    current_date = dateOfloan

    while current_date <= datetime.date(2024,4,23):

        # Check if current date is within the default period (assuming fixed start date)
        isDefault = current_date <= defaultPeriodEnd and current_date >= defaultPeriodStart

        drawdown = next(
            (drawdown[1] for drawdown in drawdowns if drawdown[0] == current_date), 0)

        # Calculate daily interest based on whether it's a default day or not
        if isDefault:
            dailyInterest = (openingPB + drawdown +
                             interestBalance) * (defaultRate / 100)
        else:
            dailyInterest = (openingPB + drawdown +
                             interestBalance) * (dailyRate / 100)

        openingPB += drawdown

        accrured_daily_interest = (accrured_daily_interest + dailyInterest)
        accured_interest.append(accrured_daily_interest)

        if accrured_daily_interest > interestBalance:
            interestBalance = accrured_daily_interest

        for interest in accured_interest:
            largest_interest = max(largest_interest, interest)

        total_interest = largest_interest

        for repayment_date, amount in repayments:
            if current_date == repayment_date:
                openingPB -= amount

         # Move to the next day
        current_date += datetime.timedelta(days=1)
        
        # print(accrured_daily_interest)

    return round(total_interest)






# default_period_start_str = "24-Mar-2024"
# default_period_end_str = "23-Apr-2024"

# default_period_start = datetime.datetime.strptime(
#     default_period_start_str, "%d-%b-%Y").date()
# default_period_end = datetime.datetime.strptime(
#     default_period_end_str, "%d-%b-%Y").date()


# print(calculate_total_interest(100000, 0.8,
#       defaultPeriodStart=default_period_start, defaultPeriodEnd=default_period_end))
