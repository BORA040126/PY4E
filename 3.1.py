work_hours=float(input("일한 시간을 입력하시오:"))
work_rates=float(input("시급을 입력하시오:"))
def multiply(x,y):
    return x*y

money=multiply(work_hours, work_rates)

plus=0

while work_hours/40>=1:
    work_hours-=40
    plus+=10

print(money+plus)
