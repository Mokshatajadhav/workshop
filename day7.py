# import numpy as np
# listy=np.array([1,2,3,4,5])
# print(listy)
# print(type(listy))

# tup=np.array((1,2,3,))
# print(tup)

# listy1=np.array([[1,2,3],[2,3,4]])
# print(listy1)
# print(listy1.ndim)

# listy2=np.array([1,2,3,4],ndmin=5)
# print(listy2)

# listy=np.array([1,2,3,4,5,6,7])
# print(listy[3])

# listy2=np.array([[1,2,3],[4,5,6]])
# print(listy2[0,2])


# listy2=np.array([[1,2,3],[4,5,6]])
# print(listy2[0,2])
# listy3=np.array([[[1,2,3],[4,5,6]]])
# []
# [1,2,3],[4,5,6]
# 1,2,3
# print(listy3[0,0,1])

# array1=np.array([1,2,3,4])
# print(array1.dtype)
# array1=array1.astype("int64")
# print(array1.dtype)
# array1.astype("f")
# print(array1.dtype)

#view
# arr1=np.array([12,2,3,4])
# arr2=arr1.view()
# arr2[2]=8
# print(arr1)
# print(arr2)

#copy 
# arr1=np.array([12,2,3,4])
# arr2=arr1.copy()
# arr2[2]=8
# print(arr1)
# print(arr2)

# arr = np.array([[1,2,3,4], [5,6,7,8]])
# print(arr.shape)

# arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(6,2)
# print(newarr)

# myarr=newarr.reshape(-1)
# print(myarr)


import pandas as pd

data = {'Name':['Alice','Bob','Charlie'],
        'Age':[25,30,35]}
df = pd.DataFrame(data)
print(df)

# df = pd.read_excel("")
# print(df.head())

ages = df['Age']
print(ages)

subset = df[['Name','Age']]
print(subset)

filtered_df = df[df['Age']>30]
print(filtered_df)

df['City']=['New York','Los Angeles','Chicago']
print(df)













