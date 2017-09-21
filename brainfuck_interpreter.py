a = [0]
p = 0
s = raw_input("input brainfuck strings:")
# s = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.<."
jumptb = [-1] * len(s)
ps = 0
stack = []
for i in range(len(s)):
    if s[i] == "[":
        stack.append(i)
    elif s[i] == "]":
        left = stack.pop(len(stack) - 1)
        jumptb[left] = i
        jumptb[i] = left
i = 0
outout = ""
while i < len(s):
    c = s[i]
    if c == "+":
        a[p] += 1
    elif c == "-":
        a[p] -= 1
    elif c == ">":
        if p < len(a) - 1:
            p += 1
        else:
            a = a + [0]
            p += 1
    elif c == "<":
        if p == 0:
            a = [0] + a
        else:
            p -= 1
    elif c == "[":
        if a[p] == 0:
            i = jumptb[i]
    elif c == "]":
        if a[p] != 0:
            i = jumptb[i]
    elif c == ".":
        print chr(a[p])
    elif c == ",":
        a[p] = ord(raw_input().strip())
    i += 1

print outout
raw_input()
