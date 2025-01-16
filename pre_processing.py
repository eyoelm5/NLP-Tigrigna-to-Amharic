from read_and_write import write_file, read_file

import re
import string

def removing_puntuation(text):
    punctuation = string.punctuation + '፡።፣፤፥፦፧፨'
    translation_table = str.maketrans('', '', punctuation)
    return text.translate(translation_table)
    
def removing_non_phonetic(text):
    ethiopic_pattern = re.compile(r'[^\u1200-\u137F\s]')
    return ethiopic_pattern.sub('', text)

def text_cleanup(text):
    puntuation_removed = removing_puntuation(text)
    cleaned_text = removing_non_phonetic(puntuation_removed)
    return cleaned_text

def text_pre_processing(parallel_text_number, custom_files):
    if custom_files:
        amharic_file, tigrigna_file = custom_files
        cleaned_amharic = text_cleanup(amharic_file)
        cleaned_tigrigna = text_cleanup(tigrigna_file)
    else:
        amharic_file = f"amharic{parallel_text_number}"
        tigrigna_file = f"tigrigna{parallel_text_number}"
        cleaned_amharic = text_cleanup(read_file("Inputs", amharic_file))
        cleaned_tigrigna = text_cleanup(read_file("Inputs", tigrigna_file))

    write_file("Cleaned_texts", "Cleaned_amharic", cleaned_amharic)
    write_file("Cleaned_texts", "Cleaned_Tigrigna", cleaned_tigrigna)
    print("\nCleaned text saved in Cleaned_texts folder")