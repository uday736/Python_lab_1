print("Enter Marks Obtained in 5 Subjects: ")
sub1 = int(input("Python: "))
sub2 = int(input("J2EE : "))
sub3= int(input("Cyber Security : "))
sub4 = int(input("C#: " ))
sub5 = int(input("HTML:"))

if sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100:
    print("Invalid marks")
    exit()

total = "Total marks : 500"
print(total)

tot=int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5)
avg = tot/5

print("Obtained marks: ",int(tot))

print("Percentage : ",avg)

if sub1>=33 and sub2>=33 and sub3>=33 and sub4>=33 and sub5>=33:
    print("You're pass")
else:
    print("You're fail!")

if avg >= 90 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 80 and avg < 90:
    print("Your Grade is A")
elif avg >= 70 and avg < 80:
    print("Your Grade is B1")
elif avg >= 60 and avg < 70:
    print("Your Grade is B")
elif avg >= 50 and avg < 60:
    print("Your Grade is C")
elif avg >= 40 and avg < 50:
    print("Your Grade is D")
elif avg >= 33 and avg < 40:
    print("Your Grade is E")