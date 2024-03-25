your_name = input("What is your name? ")
day_of_week = input("What day of the week is it? ")

if (
    day_of_week.lower() == "monday"
    or day_of_week == "tuesday"
    or day_of_week == "wednesday"
    or day_of_week == "thursday"
    or day_of_week == "friday"
):
    weather = input("What is the weather like? Sunny or Rainny? ")
    if weather.lower() == "Sunny":
        print(f"Hello {your_name}, go outside and enjoy the sunshine!")
    else:
        print(f"Hello {your_name}, stay at home and watch the rain!")
else:
    print("Its the weekend! Do whatever you want!")
