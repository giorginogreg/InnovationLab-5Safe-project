import os

folder_path = './../resources/yolo format/validation/labels'  # Replace with the path to your folder

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Process only .txt files
        file_path = os.path.join(folder_path, filename)
        output_file_path = os.path.join(folder_path, filename)

        # Open the input file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter out rows with negative values
        lines = [line for line in lines if not any(float(value) < 0 for value in line.split())]

        # Write the filtered lines to a new file
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(lines)

        print("Negative value rows removed. Output saved to '{}'.".format(output_file_path))
