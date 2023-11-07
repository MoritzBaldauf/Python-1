
def grade_calculator(assignments: list, bonus_assignment: int, exam: int): # Return tuple[bool, int]
    grade = (False, 5)
    # Check that each value is int (ther is most likley a better solution)
    for i in range(len(assignments)):
        if assignments[i] is None:
            assignments[i] = 0

    if bonus_assignment is None:
        bonus_assignment = 0

    if exam is None:
        exam = 0

    # Check if >= 50% of all achivable assignment points
    assignments.append(bonus_assignment)

    avrg_point_assignments = sum(assignments) / len(assignments)
    if avrg_point_assignments < 50:
        return grade
    elif exam < 50:
        return grade
    else:
        assignments.sort(reverse=True)
        for i in range(len(assignments[:8])):
            if assignments[i] < 25:
                return grade

    # Calc grade if != 5
    assignments.append(exam)
    average_final_score = (sum(assignments)/1100)*100
    if average_final_score >= 87.5:
        grade = (True, 1)
        return grade
    elif 75 <= average_final_score < 87.5:
        grade = (True, 2)
        return grade
    elif 62.5 <= average_final_score < 75:
        grade = (True, 3)
    elif not (not (average_final_score >= 50) or not (average_final_score < 62.5)):
        grade = (True, 4)
    return grade



#grade_received = grade_calculator([0,100,100,13,100,100,20,100,100,100], 0, 100)

#print(grade_received)
