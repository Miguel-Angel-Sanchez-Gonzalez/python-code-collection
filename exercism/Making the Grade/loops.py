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
            