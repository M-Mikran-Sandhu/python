#json and request exercise

import requests
import json
import pprint

endGame=""
url="https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple"

while endGame != "quit":
    x = requests.get(url)
    if(x.status_code != 200):
        endGame=input("Sorry! 404 _____ Press enter to try again or type 'quit' to Quit Game")
    else:
        data=json.loads(x.text)
        pprint.pprint(data)
        input("Press enter to get a new question")
    
     

               
