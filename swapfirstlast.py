#To swap the first and the last word of a string
a=input('Enter any string ')
n=len(a)
b=a[-1]+a[1:n-1]+a[0]
print(b)
