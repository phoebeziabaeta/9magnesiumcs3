import sys

yr = int(input("Enter year of birth (not earlier than 1900): "))

if yr < 1900:
    print("Invalid Year, input should not be earlier than 1900.")
    sys.exit(0)
else:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    zodiac_index = (yr - 1900) % 12
    element_index = ((yr - 1900) // 2) % 5

    print(f"Your Chinese Zodiac sign is: {zodiac[zodiac_index]}")
