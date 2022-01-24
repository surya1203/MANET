def calculate_dist():
    r = 6371
    # lat1 = math.radians(loc1[0])
    # # print(lat1)
    # lat2 = math.radians(loc2[0])
    # long1 = math.radians(loc1[1])
    # long2 = math.radians(loc2[1])
    lat1 = math.radians(float(textbox1.get()))
    lat2 = math.radians(float(textbox3.get()))
    long1 = math.radians(float(textbox2.get()))
    long2 = math.radians(float(textbox4.get()))

    delta_lambda = abs(lat1 - lat2)
    delta_phi = abs(long1 - long2)
    hav_delta_lambda = math.sin(delta_lambda / 2) ** 2
    hav_delta_phi = math.sin(delta_phi / 2) ** 2

    d = 2 * r * math.asin(math.sqrt(hav_delta_phi + (math.cos(lat1) * math.cos(lat2) * hav_delta_lambda)))
    print(d)
    textbox5.insert(tkinter.END, str(d))
