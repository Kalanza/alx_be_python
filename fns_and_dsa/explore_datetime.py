from datetime import datetime, date, timedelta
#This two enable us to workk with dates,time and yeard
def display_current_datetime():
    current_date = datetime.now()
    print(current_date)

display_current_datetime()

def calculate_future_date():
    days = int(input('Enter the number of days to add to the current date: '))
    today = date.today()
    future_date = today + timedelta(days=days)
  
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

calculate_future_date()