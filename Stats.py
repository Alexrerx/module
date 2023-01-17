def get_min(temps):
    return min(temps)

def get_max(temps):
    return max(temps)

def get_good_days(temps, good_temp_low = 17, good_temp_high = 25):
    k = 0
    for i in range(len(temps)):
        if good_temp_low < temps[i] < good_temp_high:
            k += 1
    return k
