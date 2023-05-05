# # def min_ugliy_value(nums):
# #     n=len(nums)
# #     dp=[[0]*n for _ in range(n)]
# #     for i in range(1,n):
# #         for j in range(n):
# #           dp[i][j]=min(dp[i-1][k]+abs(nums[i]-j) for k in range(n))
# #     return min(dp[-1])
#
# # n=int(input())
# # nums=input()
# # nums=nums.split(' ')
# # for i in range(len(nums)):
# #     nums[i]=int(nums[i])
# # # print(nums)
# # print(min_ugliy_value(nums))
#
# # def min_ugliy_value(nums):
# #     n = len(nums)
# #     dp = [[0] * n for _ in range(n)]
# #     for i in range(1, n):
# #         for j in range(n):
# #             dp[i][j] = min(dp[i - 1][k] + abs(nums[i] - j) for k in range(n))
# #     return min(dp[-1])
# #
# #
# # n = int(input())
# # nums = input()
# # nums = nums.split(' ')
# # for i in range(len(nums)):
# #     nums[i] = int(nums[i])
# # # print(nums)
# # print(min_ugliy_value(nums))
#
# # def min_ugliy_value(nums):
# #     n=len(nums)
# #     dp=[[0]*n for _ in range(n)]
# #     for i in range(1,n):
# #         for j in range(n):
# #           dp[i][j]=min(dp[i-1][k]+abs(nums[i]-j) for k in range(n))
# #     return min(dp[-1])
#
# # n=int(input())
# # nums=input()
# # nums=nums.split(' ')
# # for i in range(len(nums)):
# #     nums[i]=int(nums[i])
# # # print(nums)
# # print(min_ugliy_value(nums))
#
# def min_ugliy_value(arr):
#     arr.sort()
#     n = len(arr)
#     ugliness = 0
#     for i in range(1, n):
#         ugliness += abs(arr[i] - arr[i - 1])
#     return ugliness
#
#
# n = int(input())
# arr = input()
# arr = arr.split(' ')
# for i in range(len(arr)):
#     arr[i] = (int)(arr[i])
# print(min_ugliy_value(arr))
#
#
#
c = input()
c = c.split(' ')
n, m = int(c[0]), int(c[1])
op = input()
op = op.split(' ')
for i in range(len(op)):
    op[i] = int(op[i])
x = input()
x = x.split(' ')
for i in range(len(x)):
    x[i] = int(x[i])
y = input()
y = y.split(' ')
for i in range(len(y)):
    y[i] = int(y[i])

pre = [0] * n
value = [0] * n

for i in range(m):
    op_i = op[i]
    x_i = x[i] - 1
    y_i = y[i]
    if op_i == 0:
        value[x_i] = y_i
    else:
        ans=0
        for j in range(x_i,y_i):
            ans+=value[j]
        print(ans,end=' ')





