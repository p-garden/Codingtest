from datetime import datetime, timedelta

def solution(today, terms, privacies):
    answer = []
    date_format = "%Y.%m.%d"
    date_object = datetime.strptime(today, date_format)
    result_dict = {
    k: int(v)
    for item in terms
    for k, v in [item.split()]
    }
    cnt=1
    for item in privacies:  
        k,v = item.split()
        k_date = datetime.strptime(k,date_format)
        v_months = result_dict.get(v)
        
        total_months = k_date.month + v_months
        target_year = k_date.year + (total_months - 1) // 12
        target_month = (total_months - 1) % 12 + 1
        target_day = k_date.day 
        n_months_later = datetime(target_year, target_month, target_day)
        expiration_date = n_months_later - timedelta(days=1)        
        if date_object > expiration_date:
            answer.append(cnt)
        cnt += 1    
    return answer