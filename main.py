def get_bmi(weight, height):
    """

    :param weight: inout weight in kg
    :param height: input height in m
    :return: bmi ratio
    """
    return weight / height ** 2


def bmi_status(bmi):
    """

    :param bmi: bmi ratio
    :return: status of your condition
    """
    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi and bmi >= 25:
        return "Norma"
    elif 25 > bmi and bmi <= 30:
        return "Nadwaga"
    elif bmi > 30:
        return "Otylosc"


if __name__ == "__main__":
    weight = input("Input weight in kilograms:")
    height = input("Input height in meters")
    height = height.replace(",", ".")
    bmi = get_bmi(float(weight), float(height))
    print(f"Your BMI is {bmi} and your weight status is {bmi_status(bmi)}")
