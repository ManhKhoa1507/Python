import random

#   Check if point in the circle or not ? 
def is_circle(x, y) :
    if(abs(x*x + y*y) <= 1) : 
        return 1
    else : 
        return 0 

#   Get the number of point
def get_total() :
    return int(input())

#   Calculate the pi 
def cal_pi(point) :
    num_point_circle = 0;
    num_point_square = 0;

    for i in range (point) :
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        
        if(is_circle(x,y) == 1) :
            num_point_circle += 1

    return 4* num_point_circle / point 

if __name__ == '__main__' :
    total = get_total()
    pi = cal_pi(total)
    
    print(pi)
