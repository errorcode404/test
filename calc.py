#-*- coding:utf-8 -*-

import re

string = input("계산하고 싶은 식을 입력 해 주세요.\n")

rule = re.compile(r"[+|\-|\*|\/|\*\*]")
operator = rule.findall(string) #['-', '+', '/', '*']
string = rule.split(string)
string = list(map(int, string))
num = string.pop(0)
for i in operator:
    try:
        if i == "+":
            num = num+string.pop(0)
        elif i == "-":
            num = num-string.pop(0)
        elif i == "*":
            num = num*string.pop(0)
        elif i == "/":
            num = num/string.pop(0)
        elif i == "**":
            num = num**string.pop(0)
    except  Exception as ex:
        print("Error!! \n", ex)
    print(num)
