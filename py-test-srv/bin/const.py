URL = 'http://py-srv:8000'

GET_ALL_URL = URL + '/dog'

STATIC = {  
    "results": [
    {
      "color": "brown",
      "id": 1,
      "name": "RC Cola"
    },
    {
      "color": "clear",
      "id": 2,
      "name": "Sprite"
    },
    {
      "color": "brown",
      "id": 3,
      "name": "Verners"
    },
    {
      "color": "green",
      "id": 4,
      "name": "Mt. Lightening"
    }
  ]
}

DELETE_URL = URL + '/dog/1'

INSERT_URL = URL + '/dog/pink/lemonade'

SMOKE_URL = URL + '/'

SMOKE = {"hello": "world"}

UPDATE_URL = URL + '/dog/2/clear/crystal'
