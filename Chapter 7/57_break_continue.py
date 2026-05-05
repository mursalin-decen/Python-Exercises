print("Break condition")
for i in range(0,100):
    if(i==20):
        break #skip the loop right now

    print(i)

print("\n Continue Condition")
for i in range (0,20):
    if(i==10):
        continue #skip this iteration
    print(i)