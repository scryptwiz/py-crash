from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

if not queue:
    print("empty")
else:
    print("not empty")
