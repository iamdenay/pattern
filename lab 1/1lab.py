from ipywidgets import interact_manual
from pyDatalog import pyDatalog
pyDatalog.create_terms('working_time, employee, net_salary, tax_rate, months, total_salary')
+(tax_rate[None]==0.33)

def calculate_tax_rate(salary):
    return 0.33 + salary*0.001

@interact_manual
def get_input(name='User', salary=100, months = 12):
    employee[name]=salary
    working_time[X] = months
    net_salary[X] = employee[X]*(1-calculate_tax_rate(salary))
    total_salary[X] = net_salary[X] * working_time[X]
    print((net_salary[X]==Y )&(Y > 30)& (total_salary[X] == Z))
