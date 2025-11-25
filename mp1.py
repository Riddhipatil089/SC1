def mp(s, t):
    return 1 if s >= t else 0
X = [(0,0), (0,1), (1,0), (1,1)]

# AND
print("AND: x1\tx2\tw1\tw2\tt\to")
w1 = w2 = 1
t = 2
for x1, x2 in X:
    o = mp(x1*w1 + x2*w2, t)
    print(x1, "\t", x2, "\t", w1, "\t", w2, "\t", t, "\t", o)

# OR 
print("\nOR: x1\tx2\tw1\tw2\tt\to")
w1 = w2 = 1
t = 1
for x1, x2 in X:
    o = mp(x1*w1 + x2*w2, t)
    print(x1, "\t", x2, "\t", w1, "\t", w2, "\t", t, "\t", o)


# XOR 
print("\nXOR: x1\tx2\tw1\tw2\tt1\tt2\to")
w1 = w2 = 1
t1 = 1  
t2 = 2  

for x1, x2 in X:
    h1 = mp(x1*w1 + x2*w2, t1)       # OR OP
    h2 = mp(x1*w1 + x2*w2, t2)       # AND OP
    o = mp(h1 * (1 - h2), 1)         # XOR OP
    print(x1, "\t", x2, "\t", w1, "\t", w2, "\t", t1, "\t", t2, "\t", o)

