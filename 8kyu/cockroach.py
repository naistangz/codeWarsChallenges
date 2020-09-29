import math

def cockroach_speed(s):
    to_minutes =s/60
    to_secs = to_minutes/60
    return math.floor(to_secs*100000)




# print(cockroach_speed(1.08))
# print(cockroach_speed(1.09))
# print(cockroach_speed(0))