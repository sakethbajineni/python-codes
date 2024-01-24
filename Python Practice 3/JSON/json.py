# json is used to store the data and exchange the data

import json

n='{"name":"saketh","age":21,"gender":"male"}'

# to covert the given   normal object to json data we use json.loads(variable name)

y=json.dumps(n)
print(y)


