import os
# this file divides the file into two, encrypts one and leaves one part to be viewed

def file_divider(file, file_name: str, output_folder1: str, output_folder2: str):
    """
    Divides a file into two parts based on a given ratio and saves them into separate folders.

    Args:
        file (file-like object): The file object containing the content to be divided.
        file_name (str): The name for the output files.
        output_folder1 (str): The folder to save the first output file.
        output_folder2 (str): The folder to save the second output file.

    Returns:
        tuple: A tuple containing the paths of the two output files.
    """
    file_content = file.read()

    file_size = len(file_content)
    split_point = int(file_size * 0.2)  # Split at 70% (adjust as needed)

    content1 = file_content[:split_point]
    content2 = file_content[split_point:]

    # Extracting the file extension
    _, file_extension = os.path.splitext(file_name)

    output_file1 = os.path.join(output_folder1, file_name + '_part1' + file_extension)
    output_file2 = os.path.join(output_folder2, file_name + '_part2' + file_extension)

    with open(output_file1, 'wb') as file1:
        file1.write(content1)

    with open(output_file2, 'wb') as file2:
        file2.write(content2)

    return output_file1, output_file2


def file_encrypting(file_part2):
    pass

def file_joiner(output_file1, output_file2):
    """
    Joins two divided files to reproduce the original file.

    Args:
        output_file1 (str): Path of the first divided file.
        output_file2 (str): Path of the second divided file.

    Returns:
        original_content (bytes): Content of the original file.
    """
    with open(output_file1, 'rb') as file1:
        content1 = file1.read()

    with open(output_file2, 'rb') as file2:
        content2 = file2.read()

    original_content = content1 + content2

    return original_content