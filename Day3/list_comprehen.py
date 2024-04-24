
#capitalized_cities = [city.title() for city in cities]


scores = {
             "Ram Thapa": 70,
             "Mira Rai": 35,
             "Sunil Limbu": 82,
             "Simran Singh": 23,
             "Biren Jha": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed) #prints ['Ram Thapa', 'Sunil Limbu', 'Biren Jha']