#PV=nRT


#Pressure
pType = int(input("What type of Pressure mesurement are you useing? \n1. ATM \n2. Torr\n3. kPa \n4. Unknown"))
if 1 <= pType <= 4:
    print("Good Choice")
else:
    print("Try again!")
pAmmount = float(input("How many of said pressure is being applied?\nSay 0 if Unknown"))
if pAmmount<0:
    print("Good Choice")
else:
    print ("Time to figure out the pressure")

#Volume
vType =  int(input("Do you have Liters or Mili-Liters?\n1. Liters \n2. Mili-Liters\nSay 0 if Unknown"))
if 0 <= vType <= 2:
    print("Good Choice")
else:
    print("Try again")

vAmmount =  float(input("How many of said space do you have?\nSay 0 if Unknown"))
print ("Good job")

#Moles
mAmmount = float(input("How many moles of a substance do you have?\nSay 0 if Unknown"))
if mAmmount < 0:
    print("Good Choice")
else:
    print("Time to figure out how many moles")

#Temprature
tType = int(input("What type of Temparature mesurement are you useing? \n1. C \n2. K\n3. F\n Say 4 if Unknown"))
tAmmount = int(input("How many of said temprature is being applied?\nSay 0 if Unknown"))
if tType == 0:
    print("Time to figure it out")
else:
    print("Time to Have fun")
#R
rConstant = .08206


#MATH
if pType == 1:
    pType = pType
if pType == 2:
    pAmmount = (pAmmount / 760)
if pType == 3:
    pAmmount = (pAmmount / 101.325)

if vType == 1:
    vAmmount = vAmmount
if vType == 2:
    vAmmount = (vAmmount * 1000)

if tType == 1:
    tAmmount = (tAmmount + 273.15)
if tType == 2:
    tAmmount = tAmmount
if tType == 3:
    tAmmount = ((tAmmount - 32) * (5 / 9) + 273.15)


#Ending
#PV=nRT
if pType == 4:
    pAmmount = (mAmmount * rConstant * tAmmount) / vAmmount
    pFinal ="{:.3f}".format(pAmmount)
    print("There are " + pFinal + " ATM's of pressure." )

if vAmmount == 0:
    vAmmount = (mAmmount * rConstant * tAmmount) / pAmmount
    vFinal ="{:.3f}".format(vAmmount)
    print("There are " + vFinal + " Liters of Space." )

if mAmmount == 0:
    mAmmount = (pAmmount * vAmmount) / (rConstant * tAmmount)
    mFinal ="{:.3f}".format(mAmmount)
    print("There are " + mFinal + " moles of your substance." )

if tAmmount == 0:
    tAmmount = (pAmmount * vAmmount) / (rConstant * mAmmount)
    tFinal = "{:.3f}".format(tAmmount)
    print("Your space is " + tFinal + " kelvin.")

