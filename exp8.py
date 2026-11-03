# Unification and Resolution in First-Order Logic

# ---------- UNIFICATION ----------

def unify(x, y, subs):
    if x == y:
        return subs

    if isinstance(x, str) and x.islower() and len(x) == 1:
        subs[x] = y
        return subs

    if isinstance(y, str) and y.islower() and len(y) == 1:
        subs[y] = x
        return subs

    return None


# ---------- RESOLUTION ----------

def resolution(clause1, clause2):
    for literal1 in clause1:
        for literal2 in clause2:

            # Check for complementary literals
            if literal1 == "~" + literal2:
                result = [
                    x for x in clause1 if x != literal1
                ] + [
                    x for x in clause2 if x != literal2
                ]

                return result

            if literal2 == "~" + literal1:
                result = [
                    x for x in clause1 if x != literal1
                ] + [
                    x for x in clause2 if x != literal2
                ]

                return result

    return None


# ---------- MAIN PROGRAM ----------

print("UNIFICATION")
x = input("Enter first term: ")
y = input("Enter second term: ")

result = unify(x, y, {})

if result is not None:
    print("Unification successful!")
    print("Substitution:", result)
else:
    print("Unification failed!")


print("\nRESOLUTION")
clause1 = input("Enter first clause (comma-separated): ").split(",")
clause2 = input("Enter second clause (comma-separated): ").split(",")

result = resolution(clause1, clause2)

if result is not None:
    print("Resolvent:", result)
else:
    print("Resolution not possible!")

