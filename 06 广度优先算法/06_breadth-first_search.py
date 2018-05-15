"""
场景如下：
你需要在你的人际关系网中找到一名芒果供应商（假设名字以m结尾的），且是关系最近的。关系网（单向关系）如下：
你的朋友：alice, bob, claire
alice的朋友：peggy
bob的朋友：anuj, peggy
claire的朋友：thom, jonny
anuj的朋友：未知
peggy的朋友：未知
thom的朋友：未知
jonny的朋友：未知
"""

from collections import deque

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = set()   # 保存检查过的人，避免无限循环
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return
            else:
                searched.add(person)
                search_deque += graph[person]
    print('not found')


if __name__ == '__main__':
    search('you')








