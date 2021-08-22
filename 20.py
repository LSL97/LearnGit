#有效的括号
class solution(object):
    def pipei(self,s):
        combine=['()','{}','[]']
        x=['(','[','{']
        y=[')',']','}']
        st=[]
        for i in s:x
            #左括号进展
            if i in x:
                st.append(i)
            #右括号与栈顶元素匹配
            elif i in y:
                #当前列表为空（即没有左括号，返回false）
                if not st:
                    return False
                #（i与栈顶元素匹配出栈）
                else:
                    temp=st.pop(-1)+i
                    if temp not in combine:
                        return False
        if st !=[]:
            return False
        else:
            return True
s=solution()
result=s.pipei('([]{}')
print(result)