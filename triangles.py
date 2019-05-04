def triangles():
    l=[1]
    while True:
        yield l
        l.append(0)#每次补0，就可以做到下次的迭代第一个元素是1且长度加一
        l=[l[i-1]+l[i] for i in range(len(l))]

'''
def triangles():
    l=[1]
    while True:
        yield l
        l=[1]+[l[i]+l[i-1] for i in range(len(l)-1)]+[1]]'''


'''def triangles():
    l=[1]
    while True:
        yield l
        l=[sum(i) for i in zip([0]+l,l+[0])]#补0思想'''
# tab 和 space不要混用




if __name__ == "__main__":
    n=0
    for t in triangles():
        print(t)
        n=n+1
        if n==10:
            break
    



