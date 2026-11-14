
student_info = [
    {
        'Name': "Umair",
        'subjects': {
            'English': 18,
            'Urdu': 38,
            'Maths': 48,
        }
    },
    {
        'Name': "Osama",
        'subjects': {
            'English': 58,
            'Urdu': 68,
            'Maths': 78,
        }
    }
]


def studentInfo(*args, **kwargs):

    for info in args:
        for student in info:

            print("\nStudent Name:", student['Name'])

            total = 0

            for subject, marks in student['subjects'].items():
                print(subject, ":", marks)
                total += marks

            print("Total Marks:", total)
            print("----------------------")


studentInfo(student_info)
