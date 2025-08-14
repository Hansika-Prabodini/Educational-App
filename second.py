score = input("Enter Score: ")
try:
    score = float(score)
except ValueError:
    print("Enter score in number format")
    quit()

if score < 0 or score > 10:
    print('The score should be between 0 & 10')
else:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
