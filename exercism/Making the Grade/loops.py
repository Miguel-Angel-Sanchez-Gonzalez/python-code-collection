# Solución al ejercicio de Exercism: "Making the Grade"
# Enunciado tomado de Exercism.org


"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    scores_list_round = []
    for studend_score in student_scores: 
        scores_list_round.append(round(studend_score))

    return scores_list_round

def count_failed_students(student_scores):

    failed_students = []
    for student_score in student_scores:
        if student_score <= 40:
            failed_students.append(student_score)

    return len(failed_students)

def above_threshold(student_scores, threshold):
    
    best_students = []
    for student_score in student_scores:
        if student_score >= threshold:
            best_students.append(student_score)

    return best_students


def letter_grades(highest):
    
    list_grades = []
    temp_num = highest

    minum = (highest - 41) / 4     
    rounded_minum = round(minum)

    if rounded_minum == minum: #enteros
        minum = int(minum)
        for i in range(4) :
            temp_num -= minum
            list_grades.append(temp_num)  
    else:
        for i in range(4) : #decimales
            minum = int(minum)
            temp_num -= minum
            list_grades.append(temp_num - i) 
    
    
    list_grades.sort()
    return list_grades

print(letter_grades(100)) #deci
print(letter_grades(97)) #int
print(letter_grades(85)) #int
print(letter_grades(92)) #deci
print(letter_grades(81)) #int