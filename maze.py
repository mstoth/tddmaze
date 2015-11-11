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
    
  def colorInFront(self):
    if getHeading(self.t) == 90: # pointing EAST
      px=getPixelAt(self.image,self.t.getXPos()+20, self.t.getYPos())
    if getHeading(self.t) == 180: # pointing SOUTH
      px=getPixelAt(self.image,self.t.getXPos(), self.t.getYPos()+20)     
    if getHeading(self.t) == 270: # pointing WEST
      px=getPixelAt(self.image,self.t.getXPos()-20, self.t.getYPos())
    if getHeading(self.t) == 0: # pointing SOUTH
      px=getPixelAt(self.image,self.t.getXPos(), self.t.getYPos()-20)     
    c = getColor(px)
    if distance(c,white) < 150: 
      return white
    if distance(c,blue) < 150: 
      return blue
    if distance(c,red) < 150: 
      return red
    if distance(c,green) < 150: 
      return green
    return blue
    
  def travel2BranchOrWall(self):
    starting = true
    while self.colorInFront() == white:
      turn(self.t,90)
      r=self.colorInFront()
      turn(self.t,180)
      l=self.colorInFront()
      turn(self.t,90) 
      if r==white or l==white:
        if starting:
          starting = false
          self.forwardWithDraw(self.t,10)
        else:
          while getXPos(self.t)%10 or getYPos(self.t)%10:
            self.forwardWithDraw(self.t,1)
          return
      self.forwardWithDraw(self.t,1)
    self.forwardWithDraw(self.t,11)
    
  def forwardWithDraw(self,t,d):
    for i in range(d):
      if self.colorInFront()==green:
        x=getXPos(t); y=getYPos(t); addOvalFilled(self.image,x-10,y-10,20,20,red)
      else:      
        x=getXPos(t); y=getYPos(t); addOvalFilled(self.image,x-10,y-10,20,20,green)
      forward(t,1)
    
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
  
  m.reset()
  moveTo(m.t,390,160) # put the turtle next to the gold
  m.t.setHeading(180)
  assert m.solve()
  
  
  