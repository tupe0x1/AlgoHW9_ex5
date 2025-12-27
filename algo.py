from typing import List
from numpy import median
from functions import get_functions

def compute_subject_median(citizen_subject_votes: List[float], values: List[float]) -> float:
    tmp_csv = citizen_subject_votes.copy()
    tmp_csv.extend(values)
    return median(tmp_csv)

def compute_medians(citizens_votes: List[List[float]], values: List[float]) -> List[float]:
    medians_list = []
    for subject_id in range(len(citizens_votes)):
        subject_id_votes = citizens_votes[subject_id]
        medians_list.append(compute_subject_median(subject_id_votes, values))
    return medians_list

def compute_balanced_medians(total_budget: float, citizen_votes: List[List[float]], functions):
    min_t = 0
    max_t = 1
    t: float = -1
    for _ in range(1000):
        t = (min_t + max_t) / 2
        t_values = [func(t) for func in functions]
        medians = compute_medians(citizen_votes, t_values)
        if sum(medians) == total_budget:
            return t
        elif sum(medians) > total_budget:
            max_t = t
        else:
            min_t = t

    return t

def compute_budget(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    functions = get_functions(total_budget, len(citizen_votes))
    t_val = compute_balanced_medians(total_budget, citizen_votes, functions)
    t_values = [func(t_val) for func in functions]
    return compute_medians(citizen_votes, t_values)

def main():
    print(compute_subject_median([1,3,5,7], [2,4,6]))
    print(compute_medians([[1,2,3], [4,5,6]], [3,4]))

if __name__ == '__main__':
    main()