x= int(input("Please Enter nuber x"))
y= int(input("Please Enter nuber y"))
op =input("Operator + - * /")

result ={
    "+":lambda x, y: x+y,
    "-":lambda x, y: x-y,
    "*":lambda x, y: x*y,
    "/":lambda x, y: x/y
}
def add(x,y):
    return x+y
add2 =lambda x, y:x+y

print(result[op](x,y))