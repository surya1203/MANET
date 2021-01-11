import math


def calculate_dist(loc1, loc2):
    r = 6371
    lat1 = math.radians(loc1[0])
    # print(lat1)
    lat2 = math.radians(loc2[0])
    long1 = math.radians(loc1[1])
    long2 = math.radians(loc2[1])

    delta_lambda = abs(lat1 - lat2)
    delta_phi = abs(long1 - long2)
    hav_delta_lambda = math.sin(delta_lambda / 2) ** 2
    hav_delta_phi = math.sin(delta_phi / 2) ** 2

    d = 2 * r * math.asin(math.sqrt(hav_delta_phi + (math.cos(lat1) * math.cos(lat2) * hav_delta_lambda)))
    return d


# lat1 = input('Enter Latitude for point 1: ')
# long1 = input('Enter Longitude for point 1: ')
# lat2 = input('Enter Latitude for point 2: ')
# long2 = input('Enter Longitude for point 2: ')

loc1 = [float(coord) for coord in input('Enter latitude and longitude of location 1 separated by comma:').split(',')]
loc2 = [float(coord) for coord in input('Enter latitude and longitude of location 2 separated by comma:').split(',')]

mum_ban = calculate_dist(loc1, loc2)
print(mum_ban)


