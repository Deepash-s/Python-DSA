#Brute force approach

arr = [1, 1, 2, 2, 3, 3]

st = set()

for i in range(len(arr)):
    st.add(arr[i])
    
k = len(st)

print(list(st))