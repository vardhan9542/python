# Using line continuation character (\)
sum1 = 10 + 20 + 30 + \
       40 + 50 + 60

print("Sum using line continuation:", sum1)

# Using implicit continuation with parentheses ()
sum2 = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print("Sum using parentheses:", sum2)
