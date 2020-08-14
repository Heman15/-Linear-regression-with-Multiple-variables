import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x1 = np.array([1,2,3,4,5,6]).reshape(-1,1)
x2 =np.array([3,5,4,6,7,8]).reshape(-1,1)
y = np.array([5,6,7,8,9,2]).reshape(-1,1)

m1_new  = m2_new = c = 0
learning_rate = 0.01
for i in range(1000):
    y_pred = m1_new* x1 + m2_new* x2 + c
    m1d = (-2/len(x1))*sum((y - y_pred)*x1)
    m2d = (-2/len(x1))*sum((y-y_pred)*x2)
    cd = (-2/len(x1))*sum(y-y_pred)
    m1_new = m1_new - learning_rate*m1d
    m2_new = m2_new - learning_rate*m2d
    c = c- learning_rate*cd
    print (m1_new,m2_new,c)

y_points = []
for i  in  range(20):
    b = m1_new*i +m2_new*i + c
    y_points.append(b)
