import numpy as np

def show_array_info(data):
    print(f"Dimensions: {data.ndim}")
    print(f"Shape: {data.shape}")
    print(f"Size: {data.size}")
    print(f"Data type: {data.dtype}")

def create_list_array(data_type):
    numbers = input("Enter numbers separated by commas: ")
    items = numbers.split(',') # Separamos por comas
    num_list = list(map(float, items))  # Convierte cada elemento de texto en un número y los guarda en una lista
    array = np.array(num_list, dtype=data_type)
    print(array)
    show_array_info(array)

def create_2d_array(data_type):
    numbers1 = input("Enter numbers separated by commas: ")
    numbers2 = input("Enter numbers separated by commas: ")
    items1 = numbers1.split(',')
    items2 = numbers2.split(',')
    num_list_1 = list(map(float, items1))
    num_list_2 = list(map(float, items2))
    array_list = [
        num_list_1,
        num_list_2 
        ]
    array = np.array(array_list, dtype=data_type)
    print(array)
    show_array_info(array)

def create_zeros_array(data_type):
    rows = int(input("Enter a number of rows: "))
    columns = int(input("Enter a number of columns: "))
    array = np.zeros((rows, columns), dtype=data_type)
    print(array)
    show_array_info(array)

def create_ones_array(data_type):
    rows = int(input("Enter a number of rows: "))
    columns = int(input("Enter a number of columns: "))
    array = np.ones((rows, columns), dtype=data_type)
    print(array)
    show_array_info(array)

def create_range_array(data_type):
    range_value = int(input("Enter a number to set the range: "))
    array = np.arange(range_value, dtype=data_type)
    print(array)
    show_array_info(array)

def create_space_array(data_type):
    start_value = int(input("Enter the start value: "))
    end_value = int(input("Enter the end value: "))
    number_of_points = int(input("Enter the number of points: "))
    array = np.linspace(start_value, end_value, number_of_points, dtype=data_type)
    print(array)
    show_array_info(array)

def main():
    print("1) int32")
    print("2) float64")
    data_type_option = int(input("Enter data type: "))
    if data_type_option == 1:
        data_type = np.int32
    else:
        data_type = np.float64
    print("1) Create list array")
    print("2) Create 2D array")
    print("3) Create zeros array")
    print("4) Create ones array")
    print("5) Create range array")
    print("6) Create space array")
    option = int(input("Select an option: "))
    if option == 1:
        create_list_array(data_type)
    elif option == 2:
        create_2d_array(data_type)
    elif option == 3:
        create_zeros_array(data_type)
    elif option == 4:
        create_ones_array(data_type)
    elif option == 5:
        create_range_array(data_type)
    elif option == 6:
        create_space_array(data_type)

if __name__ == "__main__":
    main()