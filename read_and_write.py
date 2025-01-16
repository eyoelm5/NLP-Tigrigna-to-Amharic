import os

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

def read_file(folder,filename):
    #Setting Path for input directory
    if folder:
        input_path = os.path.join(current_dir, folder)
    else:
        input_path = os.path.join(current_dir)
        
    #Reading the file
    file = open(os.path.join(input_path, f"{filename}.txt"), "r", encoding='utf-8')
    file_txt = file.read()
    file.close()
    return file_txt

def write_file(folder,filename,data):
    #Setting Path for output directory
    if folder:
        output_path = os.path.join(current_dir, folder)
    else:
        output_path = os.path.join(current_dir)

    # Checking if file exists
    try:
        os.makedirs(output_path)
    except FileExistsError:
        pass

    #Writing files into the output directory
    file = open(os.path.join(output_path, f"{filename}.txt"), "w", encoding='utf-8')
    file.write(data)
    file.close()