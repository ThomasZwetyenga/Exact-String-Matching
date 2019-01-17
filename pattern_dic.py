def pattern_count(list_of_proteins, size_pattern):
    dic={}
    for z in range(len(list_of_proteins)):
        text = list_of_proteins[z][0]
        text=text.replace(' ','')
        for x in range(len(text)):
            temporary_str=''
            for y in range(x, x+size_pattern):
                if x+size_pattern <= len(text):
                    temporary_str+=text[y]
            if temporary_str and temporary_str not in dic:
                    dic[temporary_str]=1
            elif temporary_str:
                dic[temporary_str]+=1

    return dic
