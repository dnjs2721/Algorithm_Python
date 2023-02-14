# 복권 여러 개 중 하나만 구입가능
# 당청자 수, 구매한 사람 수, 당첨 금액

# 당첨자 수 <= 구매한 사람 : 전부 당첨
# 당첨자 수 < 구매한 사람 : 당청자 수 만큼 랜덤 당첨

# 당첨 확률이 가장 높은 확률이 여러개라면 당첨 금액이 제일 높은거 구매
## 당첨 확률이 가장 높으며 금액이 가장 높은 것은 하나만 존재

def solution(lotteries):
    tmp = []
    tmp2 = []
    answer = 0
    index = 0
    for total, buy, price in lotteries:
        index += 1
        if int(total)/int(buy+1) > 1:
            percent = 1
        else:
            percent = int(total)/int(buy+1)
            
        tmp.append((percent, price, index))
        
    for i in range(len(tmp)):
        if len(tmp2) == 0:
            tmp2.append(tmp[i])
            continue
        
        before_percent, before_price, index = tmp2.pop()
        
        if tmp[i][0] > before_percent:
            tmp2.append(tmp[i])
            
        elif tmp[i][0] == before_percent:
            if tmp[i][1] > before_price:
                tmp2.append(tmp[i])
            else:
                tmp2.append((before_percent, before_price, index))
        else:
            tmp2.append((before_percent, before_price, index))
    
    before_percent, before_price, index = tmp2.pop()
    answer = index
    
    return answer

# [당첨자 수, 구매한 사람 수, 당첨 금액]
print(solution([[100, 100, 500],[1000, 1000, 100]]))
print(solution([[10, 19, 800],[20, 39, 200], [100, 199, 500]]))
print(solution([[50, 1, 50],[100, 199, 100], [1, 1, 500]]))