# Solución al ejercicio de Exercism: "Tisbury Treasure Hunt"
# Enunciado tomado de Exercism.org
def get_coordinate(record):

    return record[1]
  
# print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))

def convert_coordinate(coordinate):

    return tuple(coordinate)

# print(convert_coordinate("2A"))

def compare_records(azara_record, rui_record):

    coordinate_one = azara_record[1]
    temp_coordinate = rui_record[1]
    coordinate_two = temp_coordinate[0] + temp_coordinate[1]
    
    if coordinate_one == coordinate_two:
        return True
    
    return False

print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))
print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))