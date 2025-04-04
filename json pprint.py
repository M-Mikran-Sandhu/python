import requests
import json
import pprint
r=requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
r.status_code

#json to dictionary
question=json.loads(r.text)

pprint.pprint(question)

question["results"][0]["category"]

#dictionary to json
person={"name":"ali","age":"20"}
person_json=json.dumps(person)
person_json
