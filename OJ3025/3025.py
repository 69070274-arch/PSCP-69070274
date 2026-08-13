"""season"""
month = int(input())
day = int(input())

if month <= 3:
    season = "winter"
elif month <= 6:
    season = "spring"
elif month <= 9:
    season = "summer"
else:
    season = "fall"

if month == 3 and day >= 21:
    season = "spring"
elif month == 6 and day >= 21:
    season = "summer"
elif month == 9 and day >= 21:
    season = "fall"
elif month == 12 and day >= 21:
    season = "winter"

print(season)
