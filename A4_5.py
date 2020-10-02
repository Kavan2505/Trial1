def month(n):
    m=['January','February','March','April','May','June','July','August','September','October','November','December']
    if n>=1 or n<=12:
        return m[n-1]

a=int(input("Enter a number(1-12):"))
print("Corresponding month:",month(a))

