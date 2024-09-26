# write a program to analyze weather after entering the temperature readings
# Calculate the average temperature and highest and lowest temperature

def analyze_weather(temperature_readings):
    avg_temp = sum(temperature_readings) / len(temperature_readings)

    highest_temp = max(temperature_readings)

    lowest_temp = min(temperature_readings)

    return avg_temp, highest_temp, lowest_temp


temperature_readings = list(map(int, input("Enter the temperature readings : ").split()))

avg_temp, highest_temp, lowest_temp = analyze_weather(temperature_readings)

print(f"Average Temperature: {avg_temp:.1f}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")