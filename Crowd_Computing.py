from statistics import mean, median
from scipy import stats
estimates = [153, 333, 169, 158, 216, 592, 245, 550, 538, 556, 644, 666, 591, 504, 336, 295, 646, 571, 393, 126, 200, 140, 530, 692, 114, 237, 304, 227, 313, 352, 329, 398, 575, 129, 492, 584, 474, 198, 585, 134, 598, 306, 356, 132, 434, 110, 661, 419, 380, 362, 581, 426, 506, 410, 507, 495, 569, 544, 439, 670, 446, 225, 689, 539, 514, 449, 151, 178, 282, 240, 315, 453, 642, 231, 274, 1000, 1550]
estimates.sort()
'''tm = int(0.1*len(estimates))
estimates = estimates[tm:]
estimates = estimates[:len(estimates)-tm]

#s = 0
#for i in range(len(estimates)):
#    s+=estimates[i]
#avg = s//len(estimates)
print(mean(estimates))
'''

# we can directly calculate the trimmed mean and for that we only need to use sort() from above program and import stats from scipy
m = stats.trim_mean(estimates, 0.1)
print(m)

# plot different numbers in python
import matplotlib.pyplot as plt
#plt.plot([1,2,3,4],[1,8,27,64], 'g^') # this is y-axis values and it will generate x-values if we don't pass any
# 'ro' used for red dots, 'r--' used for red dashes, 'bs' used for blue squares, g^ for green triangles
#plt.xlabel('Numbers')
#plt.ylabel('Their cube')
# plt.plot(estimates) # i want constant y-values
y = []
estimates.sort()
tm = int(0.1*len(estimates))
estimates = estimates[tm:]
estimates = estimates[:len(estimates)-tm]

for i in range(len(estimates)):
    y.append(5)
#plt.plot(estimates,y,'ro')
plt.plot(estimates,y,'go')
plt.plot([mean(estimates)],[5],'bo')
plt.plot([median(estimates)], [5], 'co')
plt.plot([375],[5],'ro')
plt.show()
