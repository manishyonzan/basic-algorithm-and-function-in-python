age = 2
status = {
    (age<18):"very young",
    (age==18):"still too young",
    (18<age<20):"Old enough now",
    (20<=age<40):"perfect age",
    (age>=40):"welcome"
}[True]

print(status)