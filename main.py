def check_for_different():
    with open("text.txt", "r") as file1:
        first_text = file1.readlines()

    with open("new_text.txt", "r") as file2:
        second_text = file2.readlines()

    different_lines = [line for line in first_text if line not in second_text]

    if different_lines:
        for line in different_lines:
            print("Different lines: ", line.strip())

    file1.close()
    file2.close()


check_for_different()
