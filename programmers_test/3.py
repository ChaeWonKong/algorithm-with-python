"""3번

XX 게임의 유저들이 보스 몬스터를 사냥하려고 팀을 만들었습니다. 그리고 팀에 속한 캐릭터에 아이템을 사용해 공격력을 높이려 합니다.

이 게임의 아이템은 캐릭터의 공격력은 높이고 체력을 낮춥니다. 그래서 아이템을 적절히 사용해 팀의 공격력을 최대한 끌어올리려 합니다. 캐릭터별로 아이템을 사용할지 말지는 자유지만, 아이템을 사용한 캐릭터는 체력이 반드시 100 이상 남아야 합니다. 또, 한 캐릭터에 아이템 하나씩만 사용할 수 있으며, 사용한 아이템은 사라집니다.

예를 들어 캐릭터의 체력이 [200, 120, 150]이고 아이템의 효과는 다음과 같습니다.

높여줄 공격치	낮추는 체력
30	100
500	30
100	400
이때 팀의 공격력을 최대로 올리려면 첫 번째 캐릭터에 첫 번째 아이템을, 세 번째 캐릭터에 두 번째 아이템을 사용하면 됩니다.

캐릭터들의 체력을 담은 배열 healths와 아이템별 효과를 담은 이차원 배열 items가 solution 함수의 매개변수로 주어질 때, 팀의 공격력을 최고로 끌어올리려면 어떤 아이템을 사용해야 하는지 return 하도록 solution 함수를 완성해주세요.

제한 조건
healths의 길이는 1 이상 10,000 이하입니다.
healths의 원소(캐릭터의 체력)는 1 이상 1,000,000 이하인 자연수입니다.
items의 길이는 1 이상 5,000 이하입니다.
items에는 아이템이 [올려줄 공격력, 낮출 체력]이 번호 순서대로 들어있습니다.
아이템 번호는 1번 부터 시작합니다.
items[i]에는 i + 1번 아이템이 [올려줄 공격력, 낮출 체력]이 들어있습니다.
아이템이 올리는 공격력은 1 이상 500,000 이하인 자연수입니다.
아이템이 내리는 체력은 1 이상 500,000 이하인 자연수입니다.
아이템 번호는 오름차순으로 정렬해 return 해주세요.
올려주는 공격력이 같은 아이템은 없습니다.
아이템을 사용하는 방법이 여러 가지라면, 그러한 방법 중 아무거나 하나를 return 해주세요. 단, 아이템 번호는 오름차순으로 정렬되어 있어야 합니다.
입출력 예
healths	items	return
[200,120,150]	[[30,100],[500,30],[100,400]]	[1,2]
[300,200,500]	[[1000, 600], [400, 500], [300, 100]]	[3]
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2

첫 번째, 두 번째 아이템을 사용하면 캐릭터의 체력이 100 미만이 됩니다. 따라서 세 번째 아이템만 사용할 수 있습니다.
"""
import sys
sys.setrecursionlimit(10000)


# def solution(healths, items):
#     answer = []
#     maximum = 0

#     def calc(healths, items, attackpoints, used):
#         nonlocal answer, maximum
#         for i in range(len(items)):
#             if items[i][0] not in attackpoints:
#                 for j in range(len(healths)):
#                     if healths[j] - 100 >= items[i][1]:
#                         remain_healths = healths[:]
#                         remain_healths.pop(j)
#                         attackpoints.append(items[i][0])
#                         used.append(i)
#                         calc(remain_healths, items, attackpoints, used)
#                         attackpoints.pop()
#                         used.pop()
#         if sum(attackpoints) > maximum:
#             maximum = sum(attackpoints)
#             answer = used[:]
#         return
    
#     calc(healths, items, [], [])
#     ret = [i+1 for i in answer]
#     return ret

print(solution([200,120,150], [[30,100],[500,30],[100,400]]))


def items_to_use(healths, items):
    ret = []
    item_dict = []
    h = i = 0

    # preprocess item elements into dicts for sorting
    for i in range(len(items)):
        el = {'d': items[i][0], 'hp': items[i][1], 'n': i+1}
        item_dict.append(el)

    healths.sort()
    item_dict.sort(key=lambda x: x['hp'])
    item_dict.sort(key=lambda x: x['d'], reverse=True)

    for h in range(len(healths)):
        for i in range(len(item_dict)):
            if healths[h] - item_dict[i]['hp'] >= 100:
                ret.append(item_dict[i]['n'])
                item_dict.pop(i)
                break

    ret.sort()
    return ret