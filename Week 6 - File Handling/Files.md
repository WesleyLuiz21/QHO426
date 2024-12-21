# To open csv files in python

```python
import csv
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(row[0])
```

# To open JSON

```python
import json

with open("data.json") as json_file:
  data = json.load(json_file)

print(data)
```

### You can also write json to a file

```python
import json

json_data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_file = open("output.json", "w")
json.dump(json_data, json_file, indent = 4)

json_file.close()
```

# Remote files
* Use **requests**
```python
import requests

response = requests.get("https://somesite.com/data.json")
print(response.json())
```

## To send data to a server

```python
import json
import requests

data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_data = json.dumps(data)
requests.post("https://somesite.com/post", json=json_data)
```
