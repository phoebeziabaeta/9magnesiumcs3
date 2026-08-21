# Requirements:
  - Ask the user to enter a year of birth. The baseline year 1900.
  - Validate user input that it should not be earlier than 1900.
  - If the user enters an invalid year then display an appropriate message then stop or abort the program.
# Code
```
import sys

yr = int(input("Enter year of birth (not earlier than 1900): "))```

if yr < 1900:
    print("Invalid Year, input should not be earlier than 1900.")
    sys.exit(0)
else:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    zodiac_index = (yr - 1900) % 12
    element_index = ((yr - 1900) // 2) % 5

    print(f"Your Chinese Zodiac sign is: {zodiac[zodiac_index]}")```
# Output
<img width="323" height="64" alt="image" src="https://github.com/user-attachments/assets/629f4968-b53b-4aee-9596-83eb392f3865" />
```
# Output

<img width="293" height="68" alt="image" src="https://github.com/user-attachments/assets/1faeb097-60d4-4774-a6a6-e644096ab370" />
