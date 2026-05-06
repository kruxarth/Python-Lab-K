# reads a CSV file containing Indian weather data, performs various analyses,
# saves filtered results to a new CSV file.
# pratical 12 - working with CSV files using pandas
import pandas as pd
# Load the CSV file
df = pd.read_csv("indian_weather_data.csv")

# Display basic information
print("\n===== DATA INFO =====")
print(df.info())

# 1. Average temperature of all cities
avg_temp = df["temperature"].mean()
print("\nAverage Temperature:", round(avg_temp, 2), "°C")

# 2. City with highest temperature
max_temp_city = df.loc[df["temperature"].idxmax(), "city"]
max_temp = df["temperature"].max()
print("\nHottest City:", max_temp_city, "-", max_temp, "°C")

# 3. City with lowest temperature
min_temp_city = df.loc[df["temperature"].idxmin(), "city"]
min_temp = df["temperature"].min()
print("Coldest City:", min_temp_city, "-", min_temp, "°C")

# 4. Average Air Pollution (PM2.5)
avg_pm25 = df["pm2_5"].mean()
print("\nAverage PM2.5 Level:", round(avg_pm25, 2))

# 5. Most polluted city (based on PM2.5)
polluted_city = df.loc[df["pm2_5"].idxmax(), "city"]
print("Most Polluted City:", polluted_city)

# 6. Cities with high humidity (> 70%)
high_humidity = df[df["humidity"] > 70]
print("\nCities with High Humidity:")
print(high_humidity[["city", "humidity"]])

# 7. Wind speed analysis
max_wind_city = df.loc[df["wind_speed"].idxmax(), "city"]
print("\nHighest Wind Speed in:", max_wind_city)

