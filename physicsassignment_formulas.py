print("A - Speed (S=d/t)")
print("B - Work done (W=F*d)")
print("C - Pressure (P=F/A)")
print("D - Ohms Law (V=IR)")
print("E - Charge (Q=It)")

choice = input("Enter Formula: ").upper()

if choice =="A":
   d = float(input("Enter distance (m): "))
   t = float(input("Enter time (s): "))
   S = d * t
   print("Speed =", S, "m/s")

elif choice == "B":
    F = float(input("Enter force (N): "))
    d = float(input("Enter distance (m): "))
    W = F*d
    print("Work done =", W, "m/s")

elif choice == "C":
    F = float(input("Enter force (N): "))
    A = float(input("Enter Area (A): "))
    P = F/A
    print("Pressure =", P, "N/m^2")

elif choice == "D":
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (R): "))
    V = I*R
    print("Voltage =", V, "V")

elif choice == "E":
    I = float(input("Enter current (A): "))
    t = float(input("Enter time (s): "))
    Q = I/t
    print("Charge =", Q, "C")

else:
    print("Invalid choice")