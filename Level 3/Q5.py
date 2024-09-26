class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        total_hours = self.hours + other_time.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"Time: {self.hours} hour(s) and {self.minutes} minute(s)")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes} minutes")

def input_time():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    return Time(hours, minutes)


print("Enter first time:")
time1 = input_time()

print("Enter second time:")
time2 = input_time()

# Add time objects
added_time = time1.addTime(time2)

# Display results
added_time.displayTime()
added_time.displayMinute()