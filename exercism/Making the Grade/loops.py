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

# Test cases
# print(letter_grades(100)) #deci
# print(letter_grades(97)) #int
# print(letter_grades(85)) #int
# print(letter_grades(92)) #deci
# print(letter_grades(81)) #int


def student_ranking(student_scores, student_names):
    
    list_ranking = []

    for index, (i, j) in enumerate(zip(student_scores, student_names)):
        table = f"{index + 1}. {j}: {i}"
        print(table)
        list_ranking.append(table)
        
    return list_ranking

# Test cases
# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']

# print(student_ranking(student_scores, student_names))

def perfect_score(student_info):
    for i in student_info:
        if 100 in i :
            return i
    
    return []

perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
