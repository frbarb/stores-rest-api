# Write a function that returns true if the brackets in a given string are balanced.
# The function must handle parenthesis (), square brackets [], and curly braces {}.

# Test Cases
# (a[0]+b[2c[6]]){24 + 53} -> true
# f(e(d)) -> true
# [()]{}([]) -> true
# ((b) -> false
# (c] -> false
# (c] -> false
# {(a[]) -> false
# ([)] - false
# )( -> false
# empty -> false

def matching(char):
    parenthesis = {"{": "}", "(": ")", "[": "]"}
    bucket = []
    for par in char:
        if par in "{[(":
            bucket.append(par)
        elif bucket and par == parenthesis[bucket[-1]]:
            bucket.pop()
        else:
            return False
    return len(bucket) == 0


userinput = (
    "{[]{()}}",
    "[{}{})(]",
    "((()",
    "(a[0]+b[2c[6]]){24 + 53}",
    "f(e(d))",
    "[()]{}([])",
    "((b)",
    "(c]",
    "(c]",
    "{(a[])",
    "([)]",
    ")(",
    ""
)

for chars in userinput:
    if chars == "" or " ":
        print (chars + "False")
    else:
        print(chars, matching(chars))