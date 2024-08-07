def f(c):
    fx=((9/5)*c)+32
    return fx

def k(c):
    kx = c+273.15
    return kx

c = float(input("อุณหภูมิ =" ))
print("F = %.2f ฟาเรนไฮส์" % f(c))
print("K = %.2f เคลวิน" % k(c))