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
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    minum = int((highest - 41) / 4 )
    list_grades = []
    temp_num = highest
    
    for i in range(4) :
      temp_num -= minum
      list_grades.append(temp_num)
      
    list_grades.sort()
    return list_grades
      
    
    
print(letter_grades(100))

# print(letter_grades(highest=88))
# print(letter_grades(97))