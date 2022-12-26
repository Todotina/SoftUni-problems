grade = float(input())

def grade_description(grade):
    if grade < 3.00:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif grade > 5.49:
        return "Excellent"
print(grade_description(grade))

# • 2.00 – 2.99 - "Fail"
# • 3.00 – 3.49 - "Poor"
# • 3.50 – 4.49 - "Good"
# • 4.50 – 5.49 - "Very Good"
# • 5.50 – 6.00 - "Excellent"