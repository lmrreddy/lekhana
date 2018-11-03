import matplotlib.pyplot as plt
#x-coordinates of left sides of bar
left=[1,2,3,4,5]
#heights of bars
height=[10,20,15,25,30]
#labels for bars
tick_label=['one','two','three','four','five']
#ploting a bar chart
plt.bar(left,height,tick_label=tick_label,width=0.5,color=["red","blue"])
#naming of x and y axixs
plt.xlabel("X axis")
plt.ylabel("Y axixs")
#plot title
plt.title("my bar chart")
#function to show the plot
plt.show()