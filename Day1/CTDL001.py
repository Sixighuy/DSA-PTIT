import itertools 
def sinh():
    n = int(input())
    half_n = (n + 1)//2
    for i in itertools.product([0,1], repeat = half_n):
        if n % 2 == 0:
            res = list(i) + list(i[::-1])
        else:
            res = list(i) + list(i[:-1][::-1])
        print(*res)
if __name__ =="__main__":
    sinh()
