n = input()
nums = input()

op_number = input()
op_concrect = input()

# nums=' '.split(nums)
n = int(n)
nums = nums.split(' ')
op_number = int(op_number)
op_concrect = op_concrect.split(' ')

# print(nums)
s = ""
# 记录每个+号的位置
# add_pos = []
# inital_pos = -1
# # for i in range(len(nums)):
#     # prin(byn)
#     s += nums[i]
#
#     if i < n - 1:
#         s += "+"
#         inital_pos += len(nums[i]) + 1
#         add_pos.append(inital_pos)


# nums = nums.split(' ')
for i in range(len(nums)):
    nums[i] = int(nums[i])

# 存储前缀和
n = len(nums)
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + nums[i - 1]


for j in range(0, op_number):
    index = int(op_concrect[j * 2])
    # before=pre[index-1]
    after = pre[n] - nums[index] - nums[index - 1]
    op = op_concrect[j * 2 + 1]
    if op == '+':
        ans = after + nums[index - 1] + nums[index]
    elif op == '-':
        ans = after + nums[index - 1] - nums[index]
    elif op == '*':
        ans = after + nums[index - 1] * nums[index]
    elif op == '/':
        ans = after + nums[index - 1] / nums[index]

    # print(s)
    print("{:.1f}".format(round(ans, 1)), end=' ')





