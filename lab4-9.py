def BMI(w,h):
    c = (h/100)**2
    h = w/c
    return h

def bmi (y):   
    if y < 18.50 :
        n = ("น้ำหนักน้อย/ผอม")
    elif y >=18.50 and y <=22.90 :
        n = ("ปกติ(สุขภาพดี)")
    elif y >=23 and y <=24.90 :
        n = ("ท้วม/โรคอ้วนระดับ1")
    elif y >=25 and y <=29.90 :
        n = ("อ้วน/โรคอ้วนระดับ2")
    elif y >=30:
        n = ("อ้วนมาก/โรคอ้วนระดับ3")
        return n

w = int(input("น้ำหนัก(kg):"))
h = int(input("ส่วนสูง(m):"))
l = BMI(w,h)
cbmi= bmi(l)

print("ค่าดัชนีมวลกายคือ %.3f" % l)
print("ค่าดัชนีมวลกายอยู่ในเกณฑ์", cbmi)