"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        queue = deque([id])
        total = 0
        
        while queue:
            curId = queue.popleft()
            
            for r in range(len(employees)):
                if employees[r].id != curId:
                    continue
                    
                total += employees[r].importance
                temp = [x  for x in employees[r].subordinates]
                
                for i in temp:
                    queue.append(i)
                    
                
        return total
                    
                    
                
                