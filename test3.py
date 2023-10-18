planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
# print(planet_to_initial)
# print('Saturn' in planet_to_initial)
# print('UHIUHIU' in planet_to_initial)
# numbers={
#     'one':1, 'two':2, 'three':3
#     }
# numbers['eleven'] = 11
# numbers['one'] = 'Pluto'
# for k in numbers:
#     print("{}={}".format(k, numbers[k]))

# print(planet_to_initial.values())
# print(planet_to_initial)
# print(planet_to_initial.keys())
# print(planet_to_initial.items())
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))