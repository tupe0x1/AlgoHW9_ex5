from algo import *

def main():
    budget = 100
    # citizen 1 votes 100 for sub 1 and 0 to all
    # citizen 2 votes 0 for all
    # citizen 3 votes 100 for sub3
    sub1 = [100,0,0]
    sub2 = [0,0,0]
    sub3 = [0,0,100]

    citizens_subjects_votes = [sub1, sub2, sub3]
    for i, re in enumerate(citizens_subjects_votes):
        print(f"Subject {i} votes: {re}")
    res = compute_budget(budget, citizens_subjects_votes)
    print(f"with Budget {budget} the results are: ")
    for i, re in enumerate(res):
        print(f"Subject {i}: {re:.2f}")

if __name__ == '__main__':
    main()