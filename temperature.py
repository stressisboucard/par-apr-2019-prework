import matplotlib.pyplot as plt
%matplotlib inline

temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

minimun = min(temperatures_C)
print("le minimun est de ",minimun)
maximum = max(temperatures_C)
print("le maximum est de",maximum)
somme = sum(temperatures_C)
mean = somme/len(temperatures_C)
print("la moyenne est de",mean)

temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]

temperature_hot = 0

for i in temperatures_C: 
	if i>70:
		temperature_hot = i+=1

print("il y a",i,"elements superieur à 70°")

for i in temperatures_C: 
	if i==0: 
		i == sum(i-1,i+1)/2
		temperatures_C.append(i)
print("la nouvelle liste:",temperatures_C)

# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')

fahrenheit = [((i*1.8)+32), for i in temperatures_C]