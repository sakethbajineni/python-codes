from datetime import datetime
date_string=input()
date_string_to_obj_conv=datetime.strptime(date_string,"%b %d %Y %I:%M%p")
formating=date_string_to_obj_conv.strftime("%d/%m/%Y %H:%M:%S")
print(formating)