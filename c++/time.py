import time

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        # Private data fields to store hour, minute, and second
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_hour(self):
        # Get method for hour
        return self.__hour

    def get_minute(self):
        # Get method for minute
        return self.__minute

    def get_second(self):
        # Get method for second
        return self.__second

    def set_time(self, elapsed_time):
        # Calculate the hour, minute, and second based on the elapsed_time in seconds
        total_seconds = int(elapsed_time)
        self.__hour = (total_seconds // 3600) % 24
        self.__minute = (total_seconds // 60) % 60
        self.__second = total_seconds % 60

# Create a Time object representing the current time
current_time = time.localtime()
time_obj = Time(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)

# Display the current time
print(f"Current time is {time_obj.get_hour()}:{time_obj.get_minute()}:{time_obj.get_second()}")

# Prompt the user to enter an elapsed time
elapsed_time_input = int(input("Enter the elapsed time in seconds: "))

# Set the elapsed time in the Time object
time_obj.set_time(elapsed_time_input)

# Display the hour, minute, and second for the elapsed time
print(f"The hour:minute:second for the elapsed time is {time_obj.get_hour()}:{time_obj.get_minute()}:{time_obj.get_second()}")
