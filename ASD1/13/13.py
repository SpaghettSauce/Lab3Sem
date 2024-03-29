import hashlib

def hash_text(text):
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()

def make_hash_table_with_superimposition():
    words = []  

    with open('C:/Users/User/Desktop/PROGVS/ASD/13/english_text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            line = line.split()
            for word in line:
                if word and word[-1] in '.,:;!?)-':
                    word = word[:-1]
                if word and word[0] in '(':
                    word = word[1:]

                if word and word not in words:
                    words.append(word)

    hash_table = {} 

    for word in words:
        word_length = len(word)  
        hash_value = hash_text(word)

        # Если ключа с такой длиной еще нет в хеш-таблице, создаем пустой список
        if word_length not in hash_table:
            hash_table[word_length] = {}

        # Если хеш-значение уже существует для данной длины, добавляем слово в список
        if hash_value in hash_table[word_length]:
            hash_table[word_length][hash_value].append(word)
        else:
            hash_table[word_length][hash_value] = [word]

    for length, hash_values in hash_table.items():
        print(f'Key: {length}')
        for hash_value, word_list in hash_values.items():
            print(f'  Hash: {hash_value}\n  Value: {word_list}')
        print()

make_hash_table_with_superimposition()
