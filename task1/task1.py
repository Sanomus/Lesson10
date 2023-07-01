import random
import os
#using variables for avoiding mistypes and non explicit errors
start_letter = ord('A')
length_row = 26
adding_number_range = (1, 100)
ext_of_created_files = '.txt'
file_for_summary = 'summary.txt'


def collect_files_with_target_ext(files, traget_ext):
    filtered_files = []
    for file in files:
        name, ext = os.path.splitext(file)
        if ext == traget_ext:
            filtered_files.append(file)
    return filtered_files
            
#delete all txt files before start
files_path = os.getcwd()
files = os.listdir(files_path)
files_to_remove  = collect_files_with_target_ext(files, ext_of_created_files)
for file in files_to_remove:
    os.remove(file)

#create files and write to it random numbers in range(1-100) every time new
for i in range(start_letter, start_letter + length_row):
    file_name = chr(i)
    with open(f'{file_name}{ext_of_created_files}', 'w') as file:
        file.write(str(random.randint(*adding_number_range)))

#get all txt files from folder
files_path = os.getcwd()
files = os.listdir(files_path)
txt_files_in_folder = collect_files_with_target_ext(files, ext_of_created_files)

for index, file_name in enumerate(txt_files_in_folder):
    with open(f'{file_name}', 'r') as input_file, open(f'{file_for_summary}', 'a') as output_file:
        content = input_file.read()
        if index == 0:
            output_file.write(f'{file_name}:{content}')
        else:
            output_file.write(f'\n{file_name}:{content}')

