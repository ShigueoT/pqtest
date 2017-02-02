from queue import PriorityQueue

pq = PriorityQueue()
pq.put([5,1,'abc'])
pq.put([1,3,'abc'])
pq.put([1,2,'bcd'])
pq.put([1,2,'abc'])
pq.put([1,1,'abc'])
pq.put([3,10,'abc'])

while not(pq.empty()):
    print(pq.get())
