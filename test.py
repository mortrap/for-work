
def unic(dd):
    ddset = set()
    for elem in dd:
        ddset.add(elem)
    newdd = []
    for elem in ddset:
           newdd.append(elem)
    return newdd
res = unic([1,1,1,2,3,3])
print(res)


def primal(min , max):
    
    prim_list = []
    if min ==1:
        min = min +1
    for el in range(min, max):
        if all(el%i!=0 for i in range(min,el)):
                prim_list.append(el)
    return prim_list
print (primal(1,1344))
import math
class Point2D():
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def distanceFromOrigin(self, x , y):
        origin = Point2D(x, y)
        distance = self.distanceFromPoint(origin)
        return distance
    def distanceFromPoint(self, point):
        
        return math.sqrt((self.x- point.x)**2 +(self.y-point.y)**2)
po = Point2D(10,101)
po.x = 125
print (po.distanceFromOrigin(0,0))


string_arr = ["raza", "dwa", "chetire","piat","superwosem"]
def sort_standart (arr):
    sort_arr = sorted(arr, key=lambda x:len(x))
    
    return sort_arr
def sort_reverse(arr):
    sort_arr = sorted(arr, key=lambda x:len(x))
    sort_arr.reverse()
    return  sort_arr
arrs = sort_reverse(string_arr)
print(arrs)