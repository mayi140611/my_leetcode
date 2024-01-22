# 面试题-dw https://zhuanlan.zhihu.com/p/673571423

# 相邻不同的字符串个数
# 一个字符串由 '0', '1', '2', '?' 四种字符组成，请将所有 '?' 字符替换为 ['0', '1', '2'] 里面的任意一种，
# 但是需保证替换后的相邻字符不同，一共能够生成多少种替换方式

# 示例：
# 输入: S = '?0'
# 输出: 2
# 解释: 替换为 '10', '20'。'00'不符合要求，因为和后一个字符相等

# 输入: S = '??'
# 输出: Result = 6
# 解释: 01, 02,10,12,20,21

# 输入: std::string s = "?0??????2??201???";
# 输出: 1376

def f(s:str):
    def dfs(ss, i, rlist):
        if i == len(s):
            rlist.append(ss)
        else:
            if s[i]=='?':
                for ix in ['0', '1', '2']:
                    if ss=='' or ix != ss[-1]: # 判断和左边字符不同
                        if i==len(s)-1 or  ix != s[i+1]: # 判断和右边字符不同
                            dfs(ss+ix, i+1, rlist)
            else:
                dfs(ss+s[i], i+1, rlist)
    rlist = []
    dfs('', 0, rlist)
    # print(rlist)
    return len(rlist)

if __name__ == '__main__':
    print(f('??'))
    print(f("?0??????2??201???"))