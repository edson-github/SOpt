a = "11001100"
b = "01101100"

def p_and(a,b):
  return [(int(a[i]) and int(b[i])) for i in range(8)]

print (p_and(a,b))

#https://pt.stackoverflow.com/q/421873/101
