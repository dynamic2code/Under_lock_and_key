import os
# this file divides the file into two, encrypts one and leaves one part to be viewed

def file_divider(file, file_name:str):
    """Divides a file into two parts based on a given ratio.

    Args:
        file (_type_): File object from form input.
        file_name (str): Name for the output files.

    Returns:
        bytes: Content of the first divided file.
        bytes: Content of the second divided file.
    """
    file_content = file.read()

    file_size = len(file_content)
    split_point = int(file_size * 0.7)  # Split at 70% (adjust as needed)

    content1 = file_content[:split_point]
    content2 = file_content[split_point:]
    
    # Extracting the file extension
    _, file_extension = os.path.splitext(file_name)

    output_file1 = file_name + '_part1' + file_extension
    output_file2 = file_name + '_part2' + file_extension

    with open(output_file1, 'wb') as file1:
        file1.write(content1)

    with open(output_file2, 'wb') as file2:
        file2.write(content2)

    return output_file1, output_file2

def file_encrypting(file_part2):
    pass