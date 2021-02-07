def add_time(start, duration, day_of_week=None):
    time, time_format = start.split()
    hrs, mins = map(int, time.split(':'))
    added_hrs, added_mins = map(int, duration.split(':'))
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_passed = 0

    new_hrs = hrs + added_hrs
    new_mins = mins + added_mins

    while new_mins > 60:
      new_hrs += 1
      new_mins -= 60

    while new_hrs >= 12:
      if new_hrs == 12:
        days_passed += 0.5
        break
      else:
        days_passed += 0.5
        new_hrs -= 12
    
    if time_format == 'PM' and str(days_passed).endswith('.5'):
      days_passed += 0.5
      time_format = 'AM'
    elif time_format == 'AM' and str(days_passed).endswith('.5'):
      time_format = 'PM'
    
    if day_of_week:
      day_of_week_index = days_of_week.index(day_of_week.title())

      if int(days_passed) > 6 and int(days_passed) % 7 != 0:
        new_day_index = day_of_week_index + int(days_passed % 7)
      elif int(days_passed) > 6 and int(days_passed) % 7 == 0:
        new_day_index = day_of_week_index
      else:
        new_day_index = day_of_week_index + int(days_passed)
      
      while new_day_index > 6:
        new_day_index -= 7

      new_day = days_of_week[new_day_index]

      if int(days_passed) == 1:
        new_time = f"{new_hrs}:{new_mins:02} {time_format}, {new_day} (next day)"
      elif int(days_passed) > 1 and day_of_week:
        new_time = f"{new_hrs}:{new_mins:02} {time_format}, {new_day} ({int(days_passed)} days later)"
      else:
        new_time = f"{new_hrs}:{new_mins:02} {time_format}, {new_day}"
        
    else:
      if int(days_passed) == 1:
        new_time = f"{new_hrs}:{new_mins:02} {time_format} (next day)"
      elif int(days_passed) > 1:
        new_time = f"{new_hrs}:{new_mins:02} {time_format} ({int(days_passed)} days later)"
      else:
        new_time = f"{new_hrs}:{new_mins:02} {time_format}"

    return new_time