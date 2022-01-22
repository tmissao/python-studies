def myfunc(*args):
  return sum(args) * 0.05

def min(*args):
  if len(args) == 0: 
    return None
  min = args[0]
  for e in args:
    if e < min: min = e
  return min

print(myfunc(40,60,100,200,500))
print(myfunc(40,60,100,200))

print(min(40,60,100,200,500, 0))
print(min())