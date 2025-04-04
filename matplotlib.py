import matplotlib.pyplot as plt
 
x=[1,2,3,4]
y=[5,6,7,8]
 
 
plt.plot(x,y)
 
plt.show()
 
legend=['january','february','march','april']
plt.xticks(x,legend)
plt.show()
plt.bar(x,y)
plt.show()
plt.title("Montly Sales")
 
plt.ylabel("this is a chart")
 
plt.show()
plt.bar(x,y)
 
plt.show()
