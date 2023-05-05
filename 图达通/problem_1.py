import sys

'''
测试样例说明
10
8
2 2
2 4
-1 -1

3
3
1 1
-1 -1

上面的例子，第一行和第二行表示M和N的大小，接下来的每一行表示蛇的位置信息，如第三行为1 2，说明在位置（1,2）有一只蛇，蛇的位置信息以数字-1为结束,
保证所有输入数据合法。
'''



#读取测试样例的输出，根据测试样例的输入构建M×N的矩阵，无蛇的位置用'.'表示，有蛇的位置用'S'表示
m=(int)(input())
n=(int)(input())

grid=[['.' for j in range(n)] for i in range(m)]

for line in sys.stdin:
    a=line.split()
    snake_pos_row=(int)(a[0])
    snake_pos_column=(int)(a[1])
    if snake_pos_row==-1 and snake_pos_column==-1:
        break
    else:
        grid[snake_pos_row][snake_pos_column]='S'


#Question A的代码实现
def count_paths_question_a(grid):
    m, n = len(grid), len(grid[0])
    # 初始化动态规划矩阵，所有元素都设置为0，除了左上角的单元格，它的值为1。
    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                # 如果当前单元格是蛇单元格，则将其值设置为0。
                dp[i][j] = 0
            else:
                # 否则，更新到达该单元格的路径数量为左侧和上方单元格的值之和。
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    # 返回从左上角到右下角的路径数目。
    return dp[m - 1][n - 1]

#Question B代码实现，空间复杂度降至了O(min(M,N)
def count_paths_question_b(grid):
    """
    统计从左上角到右下角的所有路径数量。
    兔子只能向右或向下移动，不能进入有蛇的格子。

    Args:
        grid: 一个二维列表，表示棋盘。'.'表示空白格子，'S'表示有蛇的格子。

    Returns:
        从左上角到右下角所有合法路径的数量。
    """
    # 获取矩阵的行数和列数
    m, n = len(grid), len(grid[0])
    # 如果列数小于行数，则将矩阵进行转置，确保列数大于等于行数
    if n < m:
        grid = list(zip(*grid))
        m, n = n, m

    # 定义动态数组 dp，长度为 min(m,n)，用来保存路径数
    dp = [0] * min(m, n)
    # 初始化第一个格子的路径数
    dp[0] = 1 if grid[0][0] == '.' else 0
    # 遍历每一列
    for i in range(n):
        # 如果当前格子有障碍物，则路径数为 0；否则路径数不变
        if i > 0 and grid[0][i] == 'S':
            dp[i % len(dp)] = 0

        # 遍历每一行，计算当前格子的路径数
        for j in range(1, m):
            # 如果当前格子有障碍物，则路径数为 0；否则更新路径数
            if grid[j][i] == 'S':
                dp[j % len(dp)] = 0
            else:
                dp[j % len(dp)] += dp[(j - 1) % len(dp)]

        # 特殊处理第一行的路径数，如果当前格子有障碍物，则路径数为 0；否则路径数与前一列的路径数相同
        dp[0] = dp[0] if grid[0][i] == '.' else 0

    # 返回最后一个格子的路径数（即从起点到终点的路径数）
    return dp[-1]


# Questions C答案
'''
#边界测试样例1：只有一个格子，该格子是障碍物
输入：
1
1
0 0
-1 -1

grid = [['S']]

# 边界测试样例2：只有一行的矩阵，该行存在障碍物
输入：
3
1
1 0
-1 -1

grid = [['.'], ['S'], ['.']]

# 边界测试样例3：所有格子都是障碍物
输入：
2
2
0 0
0 1
1 0
1 1
-1 -1

grid = [['S', 'S'], ['S', 'S']]

# 边界测试样例4：所有格子都不是障碍物
输入：
3
3
-1 -1

grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

# 边界测试样例5：只有一条斜线的矩阵
3
3
0 1
0 2
1 0
1 2
2 0
2 1
-1 -1

grid = [['.', 'S', 'S'], ['S', '.', 'S'], ['S', 'S', '.']]

# 边界测试样例6：只有两条斜线的矩阵
4 
4
0 1
0 2
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
-1 -1

grid = [['.', 'S', 'S', 'S'], ['S', '.', 'S', 'S'], ['S', 'S', '.', 'S'], ['S', 'S', 'S', '.']]
'''


# Questions D的代码实现  定义一个函数来查找从起点到终点的所有路径
def find_paths_question_d(grid, row, col, path, paths):
    # 如果当前位置越界或者有蛇，则返回
    if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 'S':
        return
    # 将当前位置添加到路径中
    path.append((row, col))
    # 如果已经到达终点，则将当前路径添加到路径列表中
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        paths.append(path.copy())
    else:
        # 否则，尝试向右和向下移动，并在每个方向上递归调用findPaths函数
        find_paths_question_d(grid, row, col + 1, path, paths)
        find_paths_question_d(grid, row + 1, col, path, paths)
    # 在完成递归后，从路径中删除当前位置
    path.pop()

#Question E代码实现 主要增加了是否访问过的数组
def find_paths_question_e(grid, row, col, path, paths,visited):
    # 如果当前位置越界或者有蛇，则返回
    if row<0 or col<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 'S' or visited[row][col]:
        return
    # 将当前位置添加到路径中
    path.append((row, col))
    visited[row][col]=True
    # 如果已经到达终点，则将当前路径添加到路径列表中
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        paths.append(path.copy())
    else:
        # 否则，尝试向上，下，左，右移动，并在每个方向上递归调用findPaths函数
        find_paths_question_d(grid, row-1, col, path, paths)
        find_paths_question_d(grid, row + 1, col, path, paths)
        find_paths_question_d(grid, row , col-1, path, paths)
        find_paths_question_d(grid, row , col+1, path, paths)
    # 在完成递归后，从路径中删除当前位置
    path.pop()

# num_paths = countPaths_question_b(grid)
# print(f"从左上角到右下角共有 {num_paths} 条可行路径。")

if __name__ == '__main__':

    #Question A调用
    print(f"Ans A:从左上角到右下角共有 {count_paths_question_a(grid)} 条可行路径。")

    #Question B调用
    print(f"Ans B:从左上角到右下角共有 {count_paths_question_b(grid)} 条可行路径。")
    #Question C见上面样例

    #Question D调用
    paths=[]
    find_paths_question_d(grid,0,0,[],paths)
    print(f"Ans D:从左上角到右下角共有 {len(paths)} 条可行路径。")
    for path in paths:
        print(path)

    #Question E调用
    paths = []
    visited=[[0 for i in range(len(grid)) for j in range(len(grid[0]))]]
    find_paths_question_e(grid, 0, 0, [], paths,visited)
    print(f"Ans E:从左上角到右下角共有 {len(paths)} 条可行路径。")
    for path in paths:
        print(path)





