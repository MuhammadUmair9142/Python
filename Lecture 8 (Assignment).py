# salary,bonus,name,depart


# using lambda funtion

# OR:

# Employee payroll system
# 1.filter bonus eligible Employee
# 2.with map funtion calculate its bonus in % 20%
# 3.with the help of reduce add all bonus eligible employee salary total and print


employees=[
    {"name":"Umair","salary":2000,"employee_id":1,"depart":"ET","bonus":True},
    {"name":"Osama","salary":4000,"employee_id":2,"depart":"MT","bonus":False},
    {"name":"Owais","salary":6000,"employee_id":3,"depart":"MT","bonus":True},
    {"name":"Siddiq","salary":7000,"employee_id":4,"depart":"ET","bonus":False},
    {"name":"Uzair","salary":9000,"employee_id":5,"depart":"CIT","bonus":False}
]

employees_with_bonus=list(filter(lambda emp:emp["bonus"]== True,employees))
bonus_calculated=list(map(lambda emp:emp["salary"]*0.8,employees_with_bonus))

for employee in employees_with_bonus:
    print(employee["name"])
    print(f"bonus_calculated: {bonus_calculated}")


print(bonus_calculated)