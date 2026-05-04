a= {
  "Zam":"Shi",
  "Me" : "You",
  "l1" : [1,3,24,5]
 }

#using items() method:
print(a.items()) #giving output as a tuples
print("\n")
#keys() method
print(a.keys()) #left side of : are keys and right sides are Value
print("\n")
#update() method:
a.update({"Zam":"Zamzam"})
print(a)
print("\n")
#get() method
print(a.get("Zam"))
print(a["Zam"]) #output same as get() method

#but there are some differences between get() and a[""]
#if get() didn't find anything then output will None but a[" "] will give an error