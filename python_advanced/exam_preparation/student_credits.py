def students_credits(*args):
    dict = {}
    result = ''
    for el in args:
        current_data = el.split("-")
        name, credits, max_points, diyan_points = current_data[0], int(current_data[1]), int(current_data[2]), int(current_data[3])
        dict[name] = (diyan_points/max_points) * credits
    total_credits = sum(dict.values())
    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits." + '\n'
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma." + '\n'
    sorted_credits = sorted(dict.items(), key= lambda x: -x[1])
    for element in sorted_credits:
        result += f"{element[0]} - {element[1]:.1f}" + '\n'

    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)