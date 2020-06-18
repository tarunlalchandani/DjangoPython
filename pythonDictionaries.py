Camps = {"First Year":["Inception","Sankalpa","Sphurti","Utkarsha"],"Second Year":["Remuna","Isri","Habipur","Kolkata"],"Third Year":["Pune","Mumbai","Talashrai","Govardhan Ecovillage"],"Fourth Year":["Mystery till Now"]}
s = int(input("Enter Your Year 1,2,3,4 or 5"))
if(s==1):
    print(Camps["First Year"])
elif(s==2):
    print(Camps["Second Year"])
elif(s==3):
    print(Camps["Third Year"])
else:
    print(Camps["Fourth Year"])

del(Camps["Third Year"])
for c in Camps:
    print(Camps[c])
