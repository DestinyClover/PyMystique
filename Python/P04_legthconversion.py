from lengthconversion_mod import *
print("1.miletokm( )")
print("2.kmtomile( )")
print("3.feettoinches( )")
print("4.inchestofeet( )")
n=int(input("enter choice"))
v=int(input("enter value"))
if n==1:
    print(miletokm(v))
if n==2:
    print(kmtomile(v))
if n==3:
   print(feettoinches(v))
if n==4:
    print(inchestofeet(v))
