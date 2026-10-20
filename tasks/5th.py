def cal (a: int,b: int,mo: str) -> int:
    if mo == '+':
        return a+b
    elif mo =='-':
        return a -b
    elif mo == "*":
        return a * b
    elif mo =='/':
        return a/b

print(cal(1,4,'+'))