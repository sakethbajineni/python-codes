from datetime import datetime
date_string=input()
date_obj_conv=datetime.strptime(date_string,"%d %b %Y")
print(date_obj_conv)