def gather_credits(needed_credit, *args):
    courses = []
    total = 0

    for c in args:
        name, creds = c

        if total >= needed_credit:
            break

        if name not in courses:
            total += creds
            courses.append(name)

    if total >= needed_credit:
        courses.sort()
        return f"Enrollment finished! Maximum credits: {total}.\nCourses: {', '.join(courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credit - total} credits more."


print(gather_credits(80, ("Basics", 27)))
print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27)))
