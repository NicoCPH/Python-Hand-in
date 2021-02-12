import csv

def print_file_content(file):
    with open(file, "r") as f:
        content = f.read()
        print(content)

def write_list_to_file(output_file, lst):
    with open(output_file, "a") as o:
        for el in lst:
            o.write(",".join(el) + "\n")

def read_csv(input_file):
    with open(input_file, "r") as f:
        new_list = []
        csv_reader = csv.reader(f)
        for row in csv_reader:
            new_list.append(row)
    
    return new_list

def write_lines_to_file(output_file, lst):
    print(lst)
    with open(output_file, "w") as o:
        for el in lst:
            for ele in el:
                o.write(ele + "\n")