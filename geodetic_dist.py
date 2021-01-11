#
#   Author: Surya V. Giri
#   Last Modified : Jan 11, 2021.
#
#   Purpose: Implments the haversine exppression for geodetic distance between two coordinates.
#   Input Format: give the lat-lon pairs twice as comma separated floating point numbers
# 


import math


def calculate_dist(loc1, loc2):
    r = 6371
    lat1 = math.radians(loc1[0])
    # print(lat1)
    lat2 = math.radians(loc2[0])
    long1 = math.radians(loc1[1])
    long2 = math.radians(loc2[1])

    # ANAND's Comments
    #-------------------
    # Evaluation of math.sin() is calculation intensive and so time intensive.
    # Therefore to do Square[math.sin()], it is better to do it as
    #         hav_delta_lambda = (math.sin())**2;
    #   This way math.sin() will be evaluated first and then that number is squared.
    #
    # hav_delta_lambda = math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2)
    # hav_delta_phi = math.sin(delta_phi / 2) * math.sin(delta_phi / 2)
    
    delta_lambda = abs(lat1 - lat2)
    delta_phi = abs(long1 - long2)
    hav_delta_lambda = math.sin(delta_lambda / 2) ** 2
    hav_delta_phi = math.sin(delta_phi / 2) ** 2

    d = 2 * r * math.asin(math.sqrt(hav_delta_phi + (math.cos(lat1) * math.cos(lat2) * hav_delta_lambda)))
    return d

# Personal Comments
# ------------------
# Too much printing. Increases time factor and looks clunky. Replaced with list comprehension.
# lat1 = input('Enter Latitude for point 1: ')
# long1 = input('Enter Longitude for point 1: ')
# lat2 = input('Enter Latitude for point 2: ')
# long2 = input('Enter Longitude for point 2: ')

loc1 = [float(coord) for coord in input('Enter latitude and longitude of location 1 separated by comma: ').split(',')]
loc2 = [float(coord) for coord in input('Enter latitude and longitude of location 2 separated by comma: ').split(',')]

mum_ban = calculate_dist(loc1, loc2)
print(mum_ban)


