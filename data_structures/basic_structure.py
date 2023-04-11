# using list as stucks 

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
stack.pop()
print(stack)

# using list as queues
from collections import deque

queue = deque(["Eric", "John", "Peter"])
queue.append("Mike")
queue.append("jane")
print(queue)

queue.popleft()
queue.popleft()
print(queue)

# using list as list comprehensions

squares = []
print("Using traditional for loop")
for x in range(10): 
    squares.append(x**2)

print(squares)

print("Using list comprehensions")
squares = [x**2 for x in range(10)]
print(squares)

# Looping over dictionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v) 

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
