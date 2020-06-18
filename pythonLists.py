


KrsnaNames = ["Govinda","MadhuSudana","Rama","Nrsimha","Varaha","Vishnu","MadanaMohana","Rasbihari","Krsna","Narayana","cakrapani","Padmanaksha","Murari","Acyuta","Mukunda","Damodar","Janardana","Sri Vallabh"]
Number = int(input("Enter your favourite number in {} ".format(len(KrsnaNames))))
ans = input("do you love {} say yes or no".format(KrsnaNames[Number]))
if(ans=="yes"):
    reason = input("Why you love him, state reason")
    print("Thankyou for your response")
else:
    del(KrsnaNames[Number])
