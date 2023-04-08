from collections import defaultdict


def solution(players, callings):
    rankDic = defaultdict(int)
    playerDic = defaultdict(str)
    for rank, player in enumerate(players):
        rankDic[rank + 1] = player
        playerDic[player] = rank + 1

    for call in callings:
        now_rank = playerDic[call]
        before_rank = now_rank - 1
        before_player = rankDic[before_rank]

        rankDic[before_rank], rankDic[now_rank] = rankDic[now_rank], before_player
        playerDic[before_player], playerDic[call] = playerDic[call], playerDic[before_player]

    return list(rankDic.values())
