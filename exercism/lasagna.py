"""Functions used in preparing Guido's gorgeous lasagna."""

# The Lasagna should be in the oven for 40 minutes
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the remaining bake time for the lasagna.

    :param elapsed_bake_time: int - Minutes the lasagna has already been baking.
    :return: int - Minutes remaining to reach the expected bake time.

    This function takes the elapsed baking time and returns the remaining 
    time needed based on the expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on the number of lasagna layers.

    :param number_of_layers: int - Number of layers being added.
    :return: int - Total preparation time in minutes.

    Each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed cooking time.

    :param number_of_layers: int - Number of layers in the lasagna.
    :param elapsed_bake_time: int - Minutes the lasagna has been baking.
    :return: int - Total elapsed time in minutes.

    This function returns the total time spent cooking, including 
    preparation time and the time in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
