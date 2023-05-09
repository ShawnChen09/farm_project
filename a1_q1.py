import math


def a1_q1(temperature, degree):
    if(degree == "C"):
        answer = (temperature - 32) * 5 / 9  # F to C
    if(degree == "F"):
        answer =  temperature * 9 / 5 + 32  # C to F
    return answer

