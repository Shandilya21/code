class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)
        
        total_salary = sum(salary)
        avg_salary = total_salary - min_sal - max_sal
        net_avg = avg_salary/(len(salary)-2)
        return net_avg
        