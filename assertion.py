def avg(scores):
    print("Length: ", len(scores))
    assert len(scores) != 0, "This list is empty!"
    return sum(scores)/len(scores)

scores1 = [23,34,55,89]
print("Average1: ", avg(scores1))

scores2 = [1,2,44]
print("Average2: ", avg(scores2))