selected_file = 'patch.txt'
target_file = 'new.txt'
text = '“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.'

with open(selected_file, 'w') as input_file:
    input_file.write(text)

with open(selected_file, 'r') as input_file, open(target_file, 'w') as output_file:
    content = input_file.read()
    output_file.write(content.upper())