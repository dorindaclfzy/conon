from datetime import datetime, timedelta

# Function to convert UTC string to datetime object
def convert_utc_to_datetime(utc_string):
    return datetime.strptime(utc_string, '%Y-%m-%d %H:%M:%S')

# Function to add days to a datetime object
def add_days_to_datetime(dt_obj, days):
    return dt_obj + timedelta(days=days)

# Main execution
if __name__ == "__main__":
    utc_input = "2024-04-15 14:12:59"
    dt_object = convert_utc_to_datetime(utc_input)
    new_dt_object = add_days_to_datetime(dt_object, 10)  # Adding 10 days as an example
    print(f"New Date and Time: {new_dt_object.strftime('%Y-%m-%d %H:%M:%S')}")
