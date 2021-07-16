#!/usr/bin/env python3

import requests
import json

query = \
"""
query itemsByRange($min: DateTime!, $max: DateTime!, $more: String){
  items(after: $min, before: $max, more: $more){
   nodes {
     id
     added
     title
     units {
       id
       name
      items(after: $min, before: $max){ total }
     }
   }
    more
  }
}

"""

variables = {
  "min": "2020-04-02",
  "max": "2021-06-30"
}

url = 'https://escholarship.org/graphql'
more = True

while more:
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)

    nodes = json_data['data']['items']['nodes']
    
    for n in nodes:
        print("id:{}\nadded: {}\ntitle: {}\nunits:".format(n['id'], n['added'], n['title']))
        for u in n['units']:
            print("\tname: {}\n\ttotal items: {}".format(u['name'], u['items']['total']))

    more = json_data['data']['items']['more']
    variables['more'] = more
