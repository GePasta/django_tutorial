def get_bmi(weight, height):
    """

    :param weight: inout weight in kg
    :param height: input height in m
    :return: bmi ratio
    """
    return weight / height ** 2


if __name__ == "__main__":
    weight = input("Input weight in kilograms:")
    height = input("Input height in meters")
    height = height.replace(",", ".")
    bmi = get_bmi(float(weight), float(height))
    print(f"Your BMI is {bmi}")
