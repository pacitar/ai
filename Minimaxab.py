maximum, minimum = 1000, -1000
def fun_alphabeta(d, node, maxP, v, A, B):
    if d==3:
        return v[node]
    if maxP:
        best = minimum
        for i in range(0,2):
            value = fun_alphabeta(d+1, node*2+i, False, v, A, B)
            best = max(best, value)
            A = max(A, best)
            if B<=A:
                break
        return best
    else:
        best = maximum
        for i in range(0,2):
            value = fun_alphabeta(d+1, node*2+i, True, v, A, B)
            best = min(best, value)
            B = min(B, best)
            if B<=A:
                break
        return best
scr=[]
x=int(input("Enter total number of leaf nodes: "))
for i in range(x):
    y=int(input("Enter node values: "))
    scr.append(y)
d=int(input("Enter depth value: "))
node=int(input("Enter node value: "))
print("The optimal value is: ", fun_alphabeta(d, node, True, scr, minimum, maximum))
