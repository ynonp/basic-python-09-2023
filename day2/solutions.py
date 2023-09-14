def pounds_to_kg(weight_in_lb: float) -> float:
    return weight_in_lb * 0.45359237


print(pounds_to_kg(14))

def wait(time_in_seconds: float):
    pass


def what_to_wear(temperature_in_celsius: float) -> str:
    if temperature_in_celsius < 12:
        return " layered clothing including thermal base layers, insulating layers, a windproof and waterproof outer layer, insulated pants, waterproof boots, headwear, gloves, and consider local weather conditions for adjustments."
    elif 12 < temperature_in_celsius < 20:
        return "long-sleeve shirt or light sweater, pants or jeans, and comfortable shoes"
    else:
        return " lightweight and breathable clothing such as shorts, short-sleeve shirts, sandals, and sun protection accessories"


print(what_to_wear(12))
print(what_to_wear)


# int, float, bool, str, function



