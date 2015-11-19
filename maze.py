# Maze by Michael Toth
# CSI 106
# Muhlenberg College
# 610-216-4131

setMediaPath('/users/michaeltoth/Documents/tddmaze/')
class Maze(object):
  """ solves a maze given by the maze.jpg image."""
  def __init__(self):
    self.image = makePicture('maze.jpg')
    self.w = makeWorld(self.image.getWidth(),self.image.getHeight())
    self.t = makeTurtle(self.w)
    self.reset()
      
  def reset(self):
    self.image = makePicture('maze.jpg')
    self.w.setPicture(self.image)
    self.t.penUp()
    moveTo(self.t,30,190)
    self.t.setHeading(90)
    
  def colorInFront(self,d=20):
    assert getHeading(self.t)%90==0
    if getHeading(self.t) == 90 or getHeading(self.t)==-270: # pointing EAST
      px=getPixelAt(self.image,self.t.getXPos()+d, self.t.getYPos())
    if getHeading(self.t) == 180 or getHeading(self.t)==-180: # pointing SOUTH
      px=getPixelAt(self.image,self.t.getXPos(), self.t.getYPos()+d)     
    if (getHeading(self.t) == 270) or (getHeading(self.t) == -90): # pointing WEST
      px=getPixelAt(self.image,self.t.getXPos()-d, self.t.getYPos())
    if getHeading(self.t) == 0: # pointing SOUTH
      px=getPixelAt(self.image,self.t.getXPos(), self.t.getYPos()-d)     
    c = getColor(px)
    if distance(c,white) < 150: 
      return white  
    if distance(c,blue) < 150: 
      return blue
    if distance(c,red) < 150: 
      return red
    if distance(c,yellow) < 150: 
      return yellow
    if distance(c,green) < 150: 
      return green
    return blue
    
  def travel2BranchOrWall(self):
    starting = true
    while self.colorInFront() == white or self.colorInFront() == green:
      turn(self.t,90)
      r=self.colorInFront()
      turn(self.t,180)
      l=self.colorInFront()
      turn(self.t,90) 
      if r==white or l==white or r==green or l==green:
        if starting:
          starting=false
          self.forwardWithDraw(self.t,12)
        else:
          self.forwardWithDraw(self.t,2)
          while getXPos(self.t)%10!=0 or getYPos(self.t)%10!=0:
            self.forwardWithDraw(self.t,1)
          return
      else:
        starting = false
        self.forwardWithDraw(self.t,1)
    self.forwardWithDraw(self.t,2)
    while getXPos(self.t)%10!=0 or getYPos(self.t)%10!=0:
      self.forwardWithDraw(self.t,1)
    
  def forwardWithDraw(self,t,d):
    for i in range(d):
      if self.colorInFront(10)==green:
        x=getXPos(t); y=getYPos(t); addOvalFilled(self.image,x-10,y-10,20,20,red)
      else:      
        x=getXPos(t); y=getYPos(t); addOvalFilled(self.image,x-10,y-10,20,20,green)
      forward(t,1)
      
  def solve(self):
    if self.colorInFront()==yellow:
      return True
    else:
      

      assert self.t.getHeading()%90==0
      turn(self.t,-90) # face left from the direction we were going
      for i in range(3):
        if self.colorInFront()==white or self.colorInFront()==green:
          print("trying in direction " + str(getHeading(self.t)))
          saveX=self.t.getXPos()
          saveY=self.t.getYPos()
          saveH=self.t.getHeading()
          self.travel2BranchOrWall()
          print("calling solve from " + str(getXPos(self.t)) + "," + str(getYPos(self.t)))
          if self.solve():
            return true
          turnToFace(self.t,saveX,saveY)
          if self.colorInFront()==white or self.colorInFront()==green:
            self.forwardWithDraw(self.t,int(sqrt((self.t.getXPos()-saveX)**2+(self.t.getYPos()-saveY)**2)))
            self.t.setHeading(saveH)
        turn(self.t,90)
      return False
      
    
# tests
if true:
  m=Maze()
  assert m.__class__==Maze
  assert m.image.__class__==Picture
  assert m.w.__class__==World
  # test picture in world
  p = m.w.getPicture()
  assert p.getFileName() != 'None', 'No file name for world picture.'
  # test for a turtle
  assert m.t.__class__==Turtle
  # test that it is in the right place
  assert m.t.getXPos() == 30
  assert m.t.getYPos() == 190
  # test that we can get the color in front of the turtle
  assert m.colorInFront() == white
  # turn to the right and check for blue
  m.t.setHeading(180)
  assert m.colorInFront() == blue
  # check next two directions
  m.t.setHeading(270)
  assert m.colorInFront() == blue
  m.t.setHeading(0)
  assert m.colorInFront() == white
  
  m.t.setHeading(90)
  m.travel2BranchOrWall()
  assert getXPos(m.t)==110
  assert getYPos(m.t)==190
  
  m.image = makePicture('maze.jpg')
  m.w.setPicture(m.image)
  moveTo(m.t,30,190)
  m.t.setHeading(0)
  m.travel2BranchOrWall()
  assert getXPos(m.t)==30
  assert getYPos(m.t)==110
  
  m.t.setHeading(90)
  m.travel2BranchOrWall()
  assert getXPos(m.t)==110
  assert getYPos(m.t)==110
  turn(m.t,90)
  m.travel2BranchOrWall()
  assert getXPos(m.t)==110
  assert getYPos(m.t)==150
  
  moveTo(m.t,30,190)
  m.t.setHeading(90)
  m.travel2BranchOrWall()
  turn(m.t,180)
  assert m.colorInFront() == green
  
  m.reset()
  assert getXPos(m.t)==30
  assert getYPos(m.t)==190
  assert m.colorInFront() == white
  assert getHeading(m.t)==90
  
  m.travel2BranchOrWall() # makes a green trail
  m.t.setHeading(270)
  m.forwardWithDraw(m.t,40) # makes a red trail
  m.t.setHeading(90)
  assert m.colorInFront() == red
  
  printNow("Testing next to gold")
  m.reset()
  moveTo(m.t,390,150) # put the turtle next to the gold
  m.t.setHeading(180)
  assert m.solve()
  
  printNow("Testing farther from gold")
  m.reset()
  moveTo(m.t,390,120) # put the turtle farther from the gold
  m.t.setHeading(180)
  assert m.solve()
  
  
  printNow("Testing second to last path")
  m.reset()
  moveTo(m.t,350,110) # put the turtle on the last path
  m.t.setHeading(180)  # face south
  # m.travel2BranchOrWall()
  # assert m.solve()
  m.travel2BranchOrWall()
  assert m.t.getYPos()==150
  m.travel2BranchOrWall()
  assert m.t.getYPos()==270
  
  m.reset()
  moveTo(m.t,150,230) # put the turtle on the isolated path
  m.t.setHeading(0)  # face north
  m.travel2BranchOrWall()
  turn(m.t,90)
  m.travel2BranchOrWall()
  turn(m.t,90)
  m.travel2BranchOrWall()
  turn(m.t,-90)
  m.travel2BranchOrWall()
  turn(m.t,-90)
  m.travel2BranchOrWall()
  turn(m.t,180)
  m.travel2BranchOrWall()
  m.solve()
  

  #m.reset()
  #moveTo(m.t,150,230) # put the turtle on the isolated path
  #m.t.setHeading(0)  # face north
  #m.solve()

