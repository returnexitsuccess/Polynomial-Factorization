def factor(num):
    if (num < 2):
        return [num]
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if (num % i == 0):
            factors.append(i)
    i = len(factors) - 1
    while (i >= 0):
        factors.append(num/factors[i])
        i -= 1
    return factors

def test(terms, root):
    s = 0
    for i in range(len(terms)):
        s += terms[i] * root**i
    return s

def newfactor(terms, term):
    root = -1.0 * term[0] / term[1]
    i = len(terms) - 1
    newterms = [int(terms[i] / term[1])]
    s = terms[i]
    i -= 1
    while (i > 0):
        s = s * root + terms[i]
        newterms.insert(0, int(s / term[1]))
        i -= 1
    return newterms
        

print "What is the order of the polynomial?"
order = int(raw_input())
terms = []
for i in range(order + 1):
    print "What is the x^" + str(i) + " coefficient?"
    terms.append(int(raw_input()))

#init complete

#q = factor(abs(terms[0]))
#p = factor(abs(terms[len(terms) - 1]))

factors = []

while True:
    ex = False
    p = factor(abs(terms[0]))
    q = factor(abs(terms[len(terms) - 1]))
    for i in p:
        for j in q:
            for k in [1.0,-1.0]:
                if (test(terms, i*k/j) == 0):
                    term = [int(-1*i*k),j]
                    ex = True
                    break
            if (ex):
                break
        if (ex):
            break
    if (ex):
        factors.append(term)
        terms = newfactor(terms,term)
    else:
        factors.append(terms)
        break
    if (len(terms) == 2):
        factors.append(terms)
        break

#print factors
piece = ""
for term in factors:
    piece += "("
    i = len(term) - 1 #degree of polynomial is i
    while (i >= 0):
        if (i != len(term) - 1):
            if (term[i] > 0):
                piece += " + "
            elif (term[i] < 0):
                piece += " - "
        if (i > 1):
            if (term[i] > 1):
                piece += str(term[i])
                piece += "x^"
                piece += str(i)
            elif (term[i] == 1 or term[i] == -1):
                piece += "x^"
                piece += str(i)
            elif (term[i] < -1):
                piece += str(-term[i])
                piece += "x^"
                piece += str(i)
        elif(i == 1):
            if (term[i] > 1):
                piece += str(term[i])
                piece += "x"
            elif (term[i] == 1 or term[i] == -1):
                piece += "x"
            elif (term[i] < -1):
                piece += str(-term[i])
                piece += "x"
        elif(i == 0):
            if (term[i] > 0):
                piece += str(term[i])
            elif (term[i] < 0):
                piece += str(-term[i])
        i-=1
    piece += ")"


print piece
raw_input()
