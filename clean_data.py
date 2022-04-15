#clean the "Venim de" and "Venim d'" from the Cat towns


def clean_data(file_path, output_path):
    # Read in the file
    with open(file_path, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("Venim de ", '')
    filedata = filedata.replace("Venim del ", '')
    filedata = filedata.replace("Venim dels ", '')
    filedata = filedata.replace("Venim d'", '')
    filedata = filedata.replace(".", '')
    # Write the file out again
    with open(output_path, 'w') as file:
        file.write(filedata)

clean_data("data\raw\muni-bal.txt", "data\raw\muni-bal-cleaned.txt")
clean_data("data\raw\muni-cat.txt", "data\raw\muni-cat-cleaned.txt")
clean_data("data\raw\muni-val.txt", "data\raw\muni-val-cleaned.txt")