import streamlit as st
import pandas as pd
st.title("my app")
st.markdown("smark")
st.header("header")
st.subheader("sub header")
st.write("write")
st.write("## write")  #  ##double hashtag for bold 
# st.write([1,2,3,4])
# data={1:"Mokshata",2:"Bhoomi"}
# st.write(pd.DataFrame(data))
# st.write(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}))

# st.markdown("_1234_")  #_ underscore for italic font

# st.sidebar.title("sidebar")
# st.sidebar.markdown("w")

# st.code("pip install pandas")

# check = st.checkbox('check me')
# print(check)
# star=st.selectbox('select',{1:'one', 2:'two'})
# print(star)

# st.file_uploader("enter file",type=["pdf","jpeg"])

# if st.button("check"):
#     st.success("done")

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[6,5,4,9,3,5]
plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title('bar plot')
st.pyplot()


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[6,5,4,9,3,5]
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title('scatter plot')
st.pyplot()


import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[6,5,4,9,3,5]
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title('plot')
st.pyplot()


labels = ['A','B','C','D','E']
sizes = [15,20,25,10,30]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('pie chart')
st.pyplot()


x = ['A','B','C','D','E']
y = [10,15,7,10,5]
fig, ax = plt.sub
plt.figure()
plt.bar(x,y)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar plot')
st.pyplot(fig)

labels = ['A','B','C','D','E']
sizes = [15,20,25,10,30]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('pie chart')
st.pyplot()


