from datetime import datetime
date_obj=datetime.now()
print(date_obj)

formatted_date_string=date_obj.strftime("%d %b %Y %I:%M:%S %p")
print(formatted_date_string)
formatted_date_string_2=date_obj.strftime("%d/%m/%Y, %H:%M:%S")
print(formatted_date_string_2)
date_string_1="28 November, 2018"
date_object_conversion=datetime.strptime(date_string_1,"%d %B, %Y")
print(date_object_conversion)

# adding days to the date
