st1=int(input("Vpišite 1. število: "))
st2=int(input("Vpišite 2. število: "))
st3=int(input("Vpišite 3. število: "))

if st1 >= st2 >= st3:
    print("Minimum:", st3 , ", Maksimum:", st1)
elif st1 >= st3 >= st2:
    print("Minimum:", st2 , ", Maksimum:", st1)
elif st2 >= st3 >= st1:
    print("Minimum:", st1 , ", Maksimum:", st2)
elif st2 >= st1 >= st3:
    print("Minimum:", st3 , ", Maksimum:", st2)
elif st3 >= st2 >= st1:
    print("Minimum:", st1 , ", Maksimum:", st3)
elif st3 >= st1 >= st2:
    print("Minimum:", st2 , ", Maksimum:", st3)

    