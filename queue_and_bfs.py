# Queue and Breadth-First Search (BFS)
from collections import deque  # Queue Data Structure
from graph import graph # Graph Data Structure (Model) Made from Hash Map / Associative Array Data Structure

# Let's assume this is the case for demonstration or example purposes
def person_is_seller(name):
    return name[-1] == 'm'

# Breadth-First Search or BFS
def search(name):
    queue = deque()
    queue += graph[name]
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person," is a Mango Seller!")
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False

search("you")