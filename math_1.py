def add(a,b):
    answer = a+b
    return answer

def sub(c,d):
    result = c-d
    return result

def divi(e,f):
    results = e/f
    return results

def mult(g,h):
    result1 = g*h
    return result1

def remain(i,j):
    rem =i%j
    return rem


    

my_dict ={'Tom':'93', 'Hannah':'83', 'Jack':'94'}
value =2
count=len([x for x in my_dict.values()if x < value])
print(count) 
    