from read_and_write import read_file
def to_dic():
    delimiter = '='
    SERA_data = read_file("", "SERA_Mapping")
    SERA_dict = {}
    for line in SERA_data.splitlines():
        dict_key = line.split(delimiter)[0].strip()
        dict_value = line.split(delimiter)[1].strip()
        SERA_dict[dict_key] = dict_value
    
    return SERA_dict
     

def converter(SERA_dict, text):
    words = text.split()
    phoneme_words = ""
    for word in words:
        phoneme_word = ""
        for char in word:
            phoneme_word += SERA_dict[char]
        phoneme_words = f"{phoneme_words} {phoneme_word}"
    return phoneme_words
