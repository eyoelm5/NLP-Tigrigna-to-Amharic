from read_and_write import read_file, write_file
import json

def shared_words(amharic, tigrigna):
    # Convert the text into a set
    amharic_word = set(amharic.split())
    tigrigna_word = set(tigrigna.split())

    # Find intersecting words and save them in a list
    same_words = amharic_word.intersection(tigrigna_word)
    result = list(same_words)
    return result

def shared_phonemes(amharic, tigrigna):
    # Convert the text into a set
    amharic_characters = set(list(amharic.replace(" ", "")))
    tigrigna_characters = set(list(tigrigna.replace(" ", "")))
    
    # Find intersecting phonemes and save them in a list
    same_words = amharic_characters.intersection(tigrigna_characters)
    result = list(same_words)
    return result

def shared_values():
    cleaned_amharic = read_file("Cleaned_texts", "Cleaned_amharic")
    cleaned_tigrigna = read_file("Cleaned_texts", "Cleaned_Tigrigna")
    phoneme_amharic = read_file("phoneme_texts", "phoneme_amharic")
    phoneme_tigrigna = read_file("phoneme_texts", "phoneme_tigrigna")
    shared_grapheme = shared_words(cleaned_amharic, cleaned_tigrigna)
    shared_phoneme = shared_phonemes(phoneme_amharic, phoneme_tigrigna)
    write_file("Shared", "shared_grapheme", json.dumps(shared_grapheme, ensure_ascii=False))
    write_file("Shared", "shared_phoneme", json.dumps(shared_phoneme, ensure_ascii=False))
    print("\nShared phonemes and words saved in Shared folder")
    