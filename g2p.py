from read_and_write import read_file, write_file
from sera_convertor import converter, to_dic
from speed_up import speedup

def grapheme_to_phoneme():
    cleaned_amharic = read_file("Cleaned_texts", "Cleaned_amharic")
    cleaned_tigrigna = read_file("Cleaned_texts", "Cleaned_Tigrigna")
    SERA_dict = to_dic()
    phoneme_amharic = speedup(converter, cleaned_amharic, SERA_dict)
    phoneme_tigrigna = speedup(converter, cleaned_tigrigna, SERA_dict)
    write_file("phoneme_texts", "phoneme_amharic", phoneme_amharic)
    write_file("phoneme_texts", "phoneme_tigrigna", phoneme_tigrigna)
    print("\nText that is converted to phoneme saved in phoneme_texts folder")