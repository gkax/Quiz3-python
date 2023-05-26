import requests
import json
import sqlite3
from win10toast import ToastNotifier


# Function to make a request
def get_coronavirus_data():
    url = "https://api.coronavirusapi.com/summary"
    response = requests.get(url)
    return response.json()


# Function to save the JSON response to a file
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


# Function to process and print interesting information from the API response
def process_data(data):
    global_cases = data['Global']['TotalConfirmed']
    new_cases = data['Global']['NewConfirmed']
    total_deaths = data['Global']['TotalDeaths']

    print(f"Global COVID-19 cases: {global_cases}")
    print(f"New cases today: {new_cases}")
    print(f"Total deaths: {total_deaths}")


# Function to store interesting information in a SQLite database
def store_data_in_database(data):
    conn = sqlite3.connect('coronavirus.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS cases
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, global_cases INTEGER,
                 new_cases INTEGER, total_deaths INTEGER)''')

    global_cases = data['Global']['TotalConfirmed']
    new_cases = data['Global']['NewConfirmed']
    total_deaths = data['Global']['TotalDeaths']

    c.execute("INSERT INTO cases (global_cases, new_cases, total_deaths) VALUES (?, ?, ?)",
              (global_cases, new_cases, total_deaths))

    conn.commit()
    conn.close()


# Function to display a Windows notification using win10toast
def display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


# Main execution
if __name__ == '__main__':
    # Make a request to the API and retrieve data
    data = get_coronavirus_data()

    # Save the JSON response to a file
    save_json(data, 'coronavirus_data.json')

    # Process and print interesting information from the API response
    process_data(data)

    # Store interesting information in the database
    store_data_in_database(data)

    # Display a Windows notification with the latest information
    global_cases = data['Global']['TotalConfirmed']
    new_cases = data['Global']['NewConfirmed']
    total_deaths = data['Global']['TotalDeaths']
    notification_title = "COVID-19 Update"
    notification_message = f"Global cases: {global_cases}\nNew cases: {new_cases}\nTotal deaths: {total_deaths}"
    display_notification(notification_title, notification_message)