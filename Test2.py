s = ["21", "132", "645", "+", "-"]
print (s)
a = s

a = a[:3] + a[2] + a[3:]  #// Just keeps processing. Nothing gets displayed when we say print "s"
#s = s[:3] + a + s[3:]
#print (s)