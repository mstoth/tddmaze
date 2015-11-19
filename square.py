
s=makeEmptySoundBySeconds(2)
for i in range(0,getNumSamples(s),100):
  for j in range(50):
    setSampleValueAt(s,j+i,15000)
explore(s)


filter=[1,1,1]

for i in range(2,getNumSamples(s)):
  v=0
  for j in range(3):
    v=getSampleValueAt(s,i-j)*filter[j]/3.0+v
  setSampleValueAt(s,i,v)
explore(s)
