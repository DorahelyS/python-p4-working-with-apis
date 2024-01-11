import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content

  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

#programs = GetPrograms().get_programs()
#print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)



'''
The requests library allows your program or application to send HTTP requests.

We define a get_programs() method that assigns our API endpoint to a variable name URL. The method submits a request with that URL using the get() method defined in the requests library, and returns the content of the response.

Now, in your terminal in the directory of this lab, run python lib/nyc_api.py. It should output the JSON response from the NYC Open Data API!
'''
