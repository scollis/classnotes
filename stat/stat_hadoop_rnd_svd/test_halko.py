# Pure Halko
import numpy as np
import numpy.random as rand
import numpy.linalg as lin
import matplotlib.pyplot as plt
import pandas as pd

'''
(70, 30)
Y (70, 5)
Q (70, 5)
BT (30, 5)
V (5, 5)
Uhat (5, 5)
U (70, 5)
'''

n = 30; k = 5
df = pd.read_csv("w1.csv",sep=';')
A = np.array(df)[:,1:]
print A.shape

# randomized SVD

Omega = rand.randn(n,k)

Y = np.dot(A, Omega) 
print "Y", Y.shape

Q, R = lin.qr(Y) 

BT = np.dot(A.T, Q)

print "Q", Q.shape
print "BT", BT.shape

Uhat, Sigma, V = lin.svd(BT)
print 'V', V.shape
Uhat = V.T 

print "Uhat", Uhat.shape

U = np.dot(Q, Uhat) 

print "U", U.shape

plt.plot(U[:,0],-U[:,1],'r+')

plt.hold(True)
        
# compare with real SVD

U, Sigma, V = lin.svd(A);
plt.plot(U[:,0],U[:,1],'bx')

plt.show()
