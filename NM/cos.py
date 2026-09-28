def f(x):
    return x**3+x-1
a=0
b=1
old_root=0
tol=0.0000001
print("iteration\troot\terror")
for i in range(1,100):
  root=(a+b)/2
  error=abs(root-old_root)
  print(i,"\t\t",round(root,6),"\t\t",round(root,6))
  if error<tol:
    break
  if f(a)*f(root)<0:
    b=root
  else :
    a=root

    old_root=root


print("Final root",round(root,6))