import requests

API_KEY="YOUR_API_KEY_HERE"

while True:
    print("\n===== WEATHER APP =====")
    print("1. Single City Weather")
    print("2. Multiple City Weather")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Step 1: Single City
    if choice == "1":
        city = input("Enter city name: ")

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\nCity:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
        else:
            print("City not found!")

    # Step 2: Multiple Cities
    elif choice == "2":
        cities = input("Enter city names separated by comma: ")

        cities = cities.split(",")

        for city in cities:
            city = city.strip()

            url = "https://api.openweathermap.org/data/2.5/weather"

            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                print("\nCity:", data["name"])
                print("Temperature:", data["main"]["temp"], "°C")
                print("Humidity:", data["main"]["humidity"], "%")
                print("Weather:", data["weather"][0]["description"])
            else:
                print(city, "- City not found!")

    # Step 3: Exit
    elif choice == "3":
        print("Thank you for using Weather App!")
        break

    else:
        print("Invalid choice!")