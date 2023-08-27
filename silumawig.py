'''Compute the dimension 0 shifted bottleneck distance between two persistence 
    diagrams X and Y.
'''

import numpy as np




def silumawig(X,Y):
    X=-np.sort(-X)
    Y=-np.sort(-Y)
    d=0
    shift=0
    
    N = min(len(X),len(Y))
    if N==1:
        d=abs(X[0]-Y[0])/2
        shift=d
        return d,shift
    X=X[0:N]
    Y=Y[0:N]
    Z = abs(X-Y)
    l = np.argmax(Z)



    if Y[l]>=X[l]:
        X_copy=X
        X=Y
        Y=X_copy
    if len(np.where(X>=Y)[0])==N:
        d=(X[l]-Y[l])/2
        shift=d
        return d,shift
            
    else: 
        m=np.argmin(X-Y)
        if Y[m] - X[m] > Y[l] and m<l: 
            return silumawig(X[0:l],Y[0:l])
        elif X[l] - Y[l] > X[m] and m>l:
            return silumawig(X[0:m],Y[0:m])
        else:
            d=(X[l]-Y[l]-X[m]+Y[m])/2
            shift=(X[l]-Y[l]+X[m]-Y[m])/2
            return d,shift           

    
