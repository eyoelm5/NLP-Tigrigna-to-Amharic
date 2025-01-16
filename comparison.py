from read_and_write import read_file
import json

def comparison(amharic, tigrigna, shared, dataType):
    amharic_length = len(set(amharic))
    tigrigna_length = len(set(tigrigna))
    shared_length = len(shared)
    unique_amharic = amharic_length - shared_length
    unique_tigrigna = tigrigna_length - shared_length 
    try:
        shared_percentage = (shared_length * 100)/(amharic_length + tigrigna_length - shared_length)
    except ZeroDivisionError:
        print("No Input Data")

    response = f"""
        Unique Amharic {dataType}s: {unique_amharic}
        Unique Tigrigna {dataType}s: {unique_tigrigna}
        Shared {dataType}s: {shared_length}
        {dataType} level overlap percentage: {str(shared_percentage)}
    """

    return response

def compared_values():
    cleaned_amharic = read_file("Cleaned_texts", "Cleaned_amharic").split()
    cleaned_tigrigna = read_file("Cleaned_texts", "Cleaned_Tigrigna").split()
    phoneme_amharic = list(read_file("phoneme_texts", "phoneme_amharic").replace(" ", ""))
    phoneme_tigrigna = list(read_file("phoneme_texts", "phoneme_tigrigna").replace(" ", ""))
    shared_grapheme = json.loads(read_file("Shared", "shared_grapheme"))
    shared_phoneme = json.loads(read_file("Shared", "shared_phoneme"))
    percentage_grapheme = comparison(cleaned_amharic, cleaned_tigrigna, shared_grapheme, "Word")
    percentage_phoneme = comparison(phoneme_amharic, phoneme_tigrigna, shared_phoneme, "Phoneme")
    return f"\n{percentage_grapheme}\n\t{percentage_phoneme}\n"