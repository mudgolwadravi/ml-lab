import statistics as st
import numpy as np

arr=np.array([1,1,2,3,4,5,6,7,8,9])

res1=st.mean(arr)
res2=st.median(arr)
res3=st.mode(arr)
res4=st.variance(arr.tolist())
res5=st.stdev(arr.tolist())

print("Mean :",res1)
print("mode :",res2)
print("mode :",res3)
print("variance :",res4)
print("stddev :",res5)

