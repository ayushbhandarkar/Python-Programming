import googlemaps
from datetime import datetime


class Partners:
    id1 = ""
    coordinates1 = []


class Bookings:
    id = ""
    coordinates = []


booking1 = Bookings()
booking1.id = "100"
booking1.coordinates = [79.0936895615746, 21.135576874431653]

booking2 = Bookings()
booking2.id = "200"
booking2.coordinates = [79.13351452963623, 21.090321760679913]

booking3 = Bookings()
booking3.id = "300"
booking3.coordinates = [79.12234409151928, 21.072246379532398]

partner1 = Partners()
partner1.id1 = "101"
partner1.coordinates1 = [79.15701147795686, 21.11297553431112]


partner2 = Partners()
partner2.id1 = "102"
partner2.coordinates1 = [79.10867031276771, 21.14117574859845]

partner3 = Partners()
partner3.id1 = "103"
partner3.coordinates1 = [79.14785641707441, 21.14244590633484]

gmaps = googlemaps.Client(key='AIzaSyAFTp5IDSzpxbBIVHc5_2XT_vzsNunUaI0')
now = datetime.now()

partners = [partner1, partner2, partner3]
bookings = [booking1, booking2, booking3]
dict = {}
direction_result = 0
for i in range(0, len(partners)):
    dict[i] = {}
    dict[i]['partner'] = partners[i]
    # for all partners

    for j in range(0, len(bookings)):
        direction_result = gmaps.directions(origin=[partners[i].coordinates1[1], partners[i].coordinates1[0]],
mode="driving", destination=[bookings[j].coordinates[1], bookings[j].coordinates[0]], departure_time=now)
        dict[i]['direction'] = {}
        dict[i]['direction'][j] = direction_result
        print(dict[i])


# print(dict[0]['direction'][0]['legs'][0]['duration']['value'])
