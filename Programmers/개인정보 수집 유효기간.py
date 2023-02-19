from collections import defaultdict

def convert(date):
    cv_year, cv_month, cv_day = str(date).split('.')
    cv_date = int(cv_year) * 336 + int(cv_month) * 28 + int(cv_day)
    return cv_date
    
def solution(today, terms, privacies):
    answer = []
    term = defaultdict(int)
    for i in terms:
        ty, month = str(i).split()
        term[ty] = int(month) * 28
        
    today_con_date = convert(today)
    
    for i in range(len(privacies)):
        date, pr_ty = str(privacies[i]).split()
        pr_con_date = convert(date)
        pr_con_date += term[pr_ty]
        
        if pr_con_date <= today_con_date:
             answer.append(i+1)
    
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))