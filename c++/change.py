import random

b1 = (random.randint(1, 1000) % 2 == 0)
b2 = (random.randint(1, 1000) % 2 == 0)

_a = random.randint(-100, 100)
_b = random.randint(-100, 100)
_c = random.randint(-100, 100)
_d = random.randint(-100, 100)
_e = random.randint(-100, 100)

print("b1 is " + str(b1))
print("b2 is " + str(b2))
print("_a is " + str(_a))
print("_b is " + str(_b))
print("_c is " + str(_c))
print("_d is " + str(_d))
print("_e is " + str(_e))
print()


# Part 1: BOOLEAN EXPRESSION PRACTICE

print("b1 and b2 is " + str(b1 and b2))

# Write an expression that is true if
# EITHER b1 OR b2 (but NOT both!) is true
print("b1 or b2 is " + str((b1 or b2) and not (b1 and b2)))

# Write an expression that is true if
# EITHER b1 or b2 (or both) is false
print("b1 or b2 is false " + str(not (b1 and b2)))

# Write an expression that is true if _e
# is LESS THAN OR EQUAL to _c
print("_e <= _c " + str(_e <= _c))

# Write an expression that is true if _a
# and _d are EQUAL
print("_a == _d " + str(_a == _d))

# Write an expression that is true if the
# sum of _a and _c is GREATER THAN _c
print("_a + _c > _c " + str(_a + _c > _c))

# Write an expression that is true if *neither* of
# the following conditions apply:
#            _a and _d are EQUAL
#            the sum of _a and _c is GREATER THAN _c
print("not (_a == _d or _a + _c > _c) " + str(not (_a == _d or _a + _c > _c)))

print()


# Part 2: BASIC IF/ELSE STATEMENTS

if b1:
    print("b1 is true!")

if not b2:
    print("b2 is false!")

if not b1 and not b2:
    print("b1 and b2 are BOTH false!")
else:
    print("At least one, b1 or b2, is false!")

print()


# Part 3: NESTED IF/ELSE STATEMENTS

if _a < _b:
    print("_a is less than _b")
    if _a < _c:
        print("_a is less than _c, too!")
    else:
        print("_a may be less than _b, but it is greater than or equal to _c")
else:
    print("_a is greater than or equal to _b, but we don't know its relation to c")
    if _a < _d:
        print("_a is less than _d")

print()



