
s=makeEmptySoundBySeconds(1)
for j in range(22050):
  t=j/22050.0
  v=16000*(-1.0*sin(2*pi*440*t)+\
        -1.0/3/3*sin(2*pi*3*440*t)+\
        -1.0/5/5*sin(2*pi*5*440*t))
  #      -1.0/7/7*sin(2*pi*7*440*t)+\
  #      -1.0/9/9*sin(2*pi*9*440*t))
  setSampleValueAt(s,j,v)
explore(s)
q  