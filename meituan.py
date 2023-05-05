print(eval("3+6"))
# a=input()
# b=input()
# print(a,b)

n=input()
nums=input()

op_number=input()
op_concrect=input()

# nums=' '.split(nums)
n=int(n)
nums=nums.split(' ')
op_number=int(op_number)
op_concrect=op_concrect.split(' ')

# print(nums)
s=""
#记录每个+号的位置
add_pos=[]
inital_pos=-1
for i in range(len(nums)):
    # prin(byn)
    s+=nums[i]

    if i<n-1:
        s+="+"
        inital_pos+=len(nums[i])+1
        add_pos.append(inital_pos)

list_s=list(s)
# print(list_s)
origin_s=list_s[:]
# print(add_pos)
for j in range(0,len(op_concrect)//2):
    list_s=origin_s.copy()
    list_s[add_pos[int(op_concrect[j*2])-1]]=op_concrect[j*2+1]
    s="".join(list_s)
    # print(s)
    print("{:.1f}".format(round(eval(s),1)),end=' ')





