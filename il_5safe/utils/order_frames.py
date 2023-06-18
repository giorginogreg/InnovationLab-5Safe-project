import os
import glob
import sys


def sort_txt_files(folder_path):
    file_list = glob.glob(os.path.join(folder_path, "*.txt"))  # Get the list of all .txt files in the specified folder
    for file_name in file_list:
        rows = []
        with open(file_name, 'r') as file:
            for line in file:
                rows.append(line.strip().split())  # Read each line and add it to the 'rows' list

        # Sort the rows based on the first column (integer) and then the second column (float)
        sorted_rows = sorted(rows, key=lambda x: (int(x[0]), float(x[1])))

        # Write the sorted rows back to the original file
        with open(file_name, 'w') as file:
            for row in sorted_rows:
                file.write(' '.join(row) + '\n')

        print(f"The file {file_name} has been sorted.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python order_frames.py folder_path")
    else:
        folder_path = sys.argv[1]
        sort_txt_files(folder_path)
