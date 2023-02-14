def solution(skill, skill_trees):
    order = list(skill)
    res = 0
    
    for i in skill_trees:
        order_count = 0
        flag = True
        
        for j in i:
            if j in order:
                if order_count == order.index(j):
                    order_count += 1
                else:
                    flag = False
                    break
                
        if flag:
            res += 1
                
    return res

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# def solution(skill, skill_trees):
#     res = 0
#     for skills in skill_trees:
#         order = ''
#         for spell in skills:
#             if spell in skill:
#                 order += spell
#         if order == skill[0:len(order)]:
#             res += 1
#     return res

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))