# Week 1 Practice Code: Temperature Converter & Weather Advisory
city_name = input("Enter the name of the city: ")
temperature_celcius = float(input("Enter the temperature in Celsius: "))
humidity_percentage = float(input("Enter the humidity percentage: "))
wind_speed_kmh = float(input("Enter the wind speed in km/h: "))

temperature_fahrenheit = (temperature_celcius * 9/5) + 32
temperature_kelvin = temperature_celcius + 273.15
feel_like = temperature_celcius - (wind_speed_kmh / 10) * 2

print(f"\nWeather Advisory for {city_name}:")
print(f"Temperature in Celsius: {temperature_celcius:.2f}°C")
print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}°F")
print(f"Temperature in Kelvin: {temperature_kelvin:.2f}K")
print(f"Humidity: {humidity_percentage}%")
print(f"Wind speed in km/h: {wind_speed_kmh:.2f} km/h")
print(f"Feels like: {feel_like:.2f}°C")
