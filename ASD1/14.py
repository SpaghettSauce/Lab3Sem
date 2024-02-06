import hashlib

def hash_text(text):
    hasher = hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()


def make_hash_table_with_lists():
    words = [] 
    with open('C:/Users/User/Desktop/PROGVS/ASD/13/english_text.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:       
            line = line.split()
            for word in line:
                if (word[-1] not in '.,:;!?)-') and (word[0] not in '('):
                    if word not in words:
                        words.append(word)

                elif (word[-1] in '.,:;!?)-') and (word[0] in '('):
                    word = word[:-1]
                    word = word[0:]
                    if word not in words:
                        words.append(word)

                elif (word[-1] in '.,:;!?)-') and (word[0] not in '('):
                    word = word[:-1]
                    if word not in words:
                        words.append(word)

                elif (word[-1] not in '.,:;!?)-') and (word[0] in '('):
                    word = word[0:]
                    if word not in words:
                        words.append(word)

    hash_table = {} 

    for word in words:
        word_length = len(word)  
        hash_value = hash_text(word)

        # Если ключа с такой длиной еще нет в хеш-таблице, создаем пустой список
        if word_length not in hash_table:
            hash_table[word_length] = []
        hash_table[word_length].append(word)


    print()
    for length, word_list in hash_table.items():
        print(f'Hash: {hash_value}\nKey: {length}\nValue: {word_list}')
        print()

make_hash_table_with_lists()