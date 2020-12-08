def main ():
  list1 = ["a" ,"a","a", "b" , "c" , "d" , "s"]
  list2 = ["a" , "b","c" ,"d"  ,"s" ]
  equal(list1,list2)

def equal(list1 , list2):
  i = 0
  a = 0

  while i < len(list1):
    if list1[i] not in list2:
       a = a + 1
       break
    i+=1
  while i < len(list2):
    if list2[i] not in list1:
       a = a +1
       break
    i+=1
  if a == 0:
     print("They are the same")
  else:
     print("They are not the same")
main()
