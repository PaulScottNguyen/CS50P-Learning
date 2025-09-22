def main():
    user_time = input("What time is it? ").strip()
    meal = convert(user_time)
    if meal:
        print(f"It's {meal} time")


def convert(time):
    time = time.replace(" ", "").lower()

    # Determine if it's 12-hour format
    is_am = "am" in time or "a.m" in time
    is_pm = "pm" in time or "p.m" in time

    # Remove suffix
    time = time.replace("am", "").replace("a.m", "")
    time = time.replace("pm", "").replace("p.m", "")

    # Split hours and minutes
    if ":" in time:
        hours_str, minutes_str = time.split(":")
    else:
        hours_str = time
        minutes_str = "00"

    try:
        hours = int(hours_str)
        minutes = int(minutes_str)
    except ValueError:
        return None  # Invalid input

    # Convert to 24-hour format
    if is_pm and hours != 12:
        hours += 12
    elif is_am and hours == 12:
        hours = 0

    time_float = hours + minutes / 60

    # Determine meal time
    if 7.0 <= time_float <= 8.0:
        return "breakfast"
    elif 12.0 <= time_float <= 13.0:
        return "lunch"
    elif 18.0 <= time_float <= 19.0:
        return "dinner"
    else:
        return None


if __name__ == "__main__":
    main()
