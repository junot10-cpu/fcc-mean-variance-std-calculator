import numbers

import numpy as np 

def calculate(p):
    numbers=np.array(p);
    if (len(p) !=9):
          print('the vector should have 9 elements')
    else:
          A=numbers.reshape(3,3);
          B={ 'mean':[ [ np.mean(A, axis=0).tolist(), np.mean(A, axis=1).tolist(), np.mean(A).item()   ]],
             'variance':[ [ np.var(A, axis=0).tolist(), np.var(A, axis=1).tolist(), np.var(A).item()   ]],
             'standard deviation':[[np.std(A, axis=0).tolist(), np.std(A, axis=1).tolist(), np.std(A).item() ]], 
             'max':[[np.max(A, axis=0).tolist(), np.max(A, axis=1).tolist(), np.max(A).item() ]], 
             'min':[[np.min(A, axis=0).tolist(), np.min(A, axis=1).tolist(), np.min(A).item() ]],
             'sum':[[np.sum(A,axis=0).tolist(),np.sum(A,axis=1).tolist(),np.sum(A).item() ]]
             }
    return (B)        


C=calculate([0,1, 2, 3, 4, 5, 6, 7, 8])
print(C)

