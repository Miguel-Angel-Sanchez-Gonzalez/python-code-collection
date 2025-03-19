# Solución al ejercicio de Exercism: "Chaitana's Colossal Coaster"
# Enunciado tomado de Exercism.org

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number."""

    if ticket_type == 1 :
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue
# Test cases
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))
print(add_me_to_the_queue(['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'))

def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index)."""

    if friend_name in queue:
        return queue.index(friend_name)
      
    return None

# Test cases     
print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"))



def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue."""

    queue.insert(index, person_name)
    return queue
  
# Test cases
print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"))

def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name."""

    try:
        queue.remove(person_name)
    except ValueError:
        pass
  
    return queue
  
# Test cases
print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"))

def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue."""

    number_of_times_name = queue.count(person_name)
    return number_of_times_name

# Test cases  
print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"))


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name."""

    last_person = queue.pop()
    return last_person

# Test cases
print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result."""

    queue_sort = queue.copy()
    queue_sort.sort()
    return queue_sort

# Test cases
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))