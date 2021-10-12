print("welcome to madlib code")

my_file=""

with open('assets/madlib.txt') as file:
    my_file=file.read()
    print(my_file)

arr=[]
myfile=my_file
while "}" in myfile:
    index1 = myfile.index("{")
    index2 = myfile.index("}")
    var = myfile[index1+1:index2]
    arr.append(var)

    myfile = myfile[index2+1:]
print(arr)


arr2 = []

for i in range(len(arr)) :
    print(f"Enter a/an {arr[i]}")
    user_response=input()
    arr2.append(user_response)
for i in range(len(arr)):
   my_file=my_file.replace(arr[i],arr2[i],1)
edited_file = my_file.replace("{","")
edited_file = edited_file.replace("}","")



print(edited_file)

with open("assets/edited.txt", "w") as f:

        f.write(edited_file)

    
    






