
import numpy as np
import math
xx=np.array([[1,0,0,1],[1,1,0,1],[1,1,0,1],[0,0,0,1]])
x1,y1,x2,y2=1,1,4,1
r,c=xx.shape
start=(x1-1)*c+y1-1
end=(x2-1)*c+y2-1
found=[0 for i in range(r*c)]
turn=[-1 for i in range(r*c)]
queue=[]
queue.append(start)
found[start]=True
turn[start]=-1
direction=[(0,1),(0,-1),(1,0),(-1,0)]
print(start,end,queue,found,turn)
while len(queue) > 0:
    p = queue.pop(0)
    if p == end:
        break
    elif turn[p] == 2:
        continue
    else:
        i = math.floor(p / c)
        j = p % c
        for di in direction:
            step = 1
            while step > 0:
                x = i + di[0] * step
                y = j + di[1] * step
                l = c* x + y
                print(di,queue,step,x,y,l)
                if (x >= 0) and (x < r) and (y >= 0) and (y < c) and xx[x, y] == 0 and (found[l] ==0 or turn[l] > turn[p]):
                    if found[l] == 0:
                        queue.insert(0, l)
                        found[l] = True
                        turn[l] = turn[p] + 1
                        print(queue)
                    step += 1
                else:
                    break
print(found,turn)