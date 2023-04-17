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
dict = {}
direction_result = 0
for i in range(0, len(partners)):
    dict[i] = {}
    dict[i]['partner'] = partners[i]
    direction_result = gmaps.directions(origin=[partners[i].coordinates1[1], partners[i].coordinates1[0]],
mode="driving", destination=[booking1.coordinates[1], booking1.coordinates[0]], departure_time=now)

    dict[i]['direction'] = direction_result

print(dict[0]['direction'][0]['legs'][0]['duration']['value'])

res = [key for key in dict if all(dict[temp] >= dict[key] for temp in dict)]
print(str(res))


# print(direction_result)

#  partner's id of minimum value

# 3 partners - 5-6  bookings  (partner-id)
