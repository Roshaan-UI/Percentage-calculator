mark=int(input("Enter your total marks:"))
mar=int(input("Enter your obatained marks:"))
per=(mar/mark)*100

print(round(per,4))
if per>=39 and per<45:
    print("You are passed and your grade is D")
elif per>=45 and per<60:
    print("You are passed and your grade is C")
elif per>=60 and per<75:
    print("You are passed and your grade is B")
elif per>=75 and per<85:
    print("You are passed and your grade is A")
elif per>=86 and per<=100:
    print("You are passed and your grade is A+")
else:
    print("Failed")