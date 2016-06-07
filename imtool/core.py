######################################
#Open ST
#Core
#Author:steven.miaoliang@gmail.com
#Data:2016/5/26
######################################
def min(v1,v2):
    if(v1>v2):
        return v2
    else:
        return v1

def max(v1,v2):
    if(v1>v2):
        return v1;
    else:
        return v2;

def abs(v1):
    if v1<0:
        return -v1
    else:
        return v1

class Point:
    def __init__(self, pt):
        if type(pt) != Point:
            raise ValueError('Type error')
        self.x = pt.x;
        self.y = pt.y;

    def __init__(self,_x,_y):
        self.x = _x;
        self.y = _y;

    def __sub__(self, other):
        if type(other) != Point:
            raise ValueError('Type error')
        addPt = Point();
        addPt.x = self.x - other.x
        addPt.y = self.y - other.y
        return addPt
    def x(self):
        return self.x;
    def y(self):
        return self.y;
    def distance(self,other):
        if type(other) != Point:
            raise ValueError('Type error')
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def offset(self,offsetX,offsetY):
        self.x = self.x+offsetX;
        self.y = self.y+offsetY;

class Rect:
    'Rect define'
    def __init__(self, _x, _y, _width, _height):
        self.x = _x;
        self.y = _y;
        self.width = _width;
        self.height = _height;

    def __init__(self, pt1, pt2):
        self.x = min(pt1.x, pt2.x)
        self.y = min(pt1.y, pt2.y)
        self.width = abs(pt1.x - pt2.x)
        self.height = abs(pt1.y - pt2.y)

    def x(self):
        return  self.x
    def y(self):
        return  self.y
    def width(self):
        return self.width
    def height(self):
        return self.height
    def area(self):
        return self.width*self.height
    def offset(self,offsetX,offsetY):
        self.x = self.x + offsetX;
        self.y = self.y + offsetY;
    def containPoint(self,pt):
        if type(pt) != Point:
            raise ValueError('Type Error')
        if(pt.x>= self.x and pt.x<=self.x+self.width and
           pt.y >= self.y and pt.y <= self.y + self.height):
            return True;
        return False;
    def points(self):
        topLeft = Point(self.x,self.y)
        topRight = Point(self.x+self.width,self.y)
        bottomRight = Point(self.x+self.width,self.y+self.height)
        bottomLeft = Point(self.x,self.y+self.height)
        pts = {topLeft,topRight,bottomRight,bottomLeft}
        return  pts;

    def union(self,other):
        minX = min(self.x,other.x)
        minY = min(self.y,other.y)
        maxX = max(self.x+self.width,other.x+self.width)
        maxY = max(self.y+self.height,other.y+self.height)
        return Rect(Point(minX,minY),Point(maxX,maxY))

    def intersection(self,other):
        pass


