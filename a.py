import random
import math
import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["num1", "num2", "label"])
    for i in range(0,400):
        num1 = random.randint(0,100)
        num2 = random.randint(0,100)
        if abs(num1 - num2) < 20 :
            writer.writerow([num1, num2,0])
        else:
            writer.writerow([num1, num2,1])