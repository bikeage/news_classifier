import data_prep

def count_ALLCAPS(df):
    '''counts occurnaces of 1+ char words in
    all caps
    '''
    df = df.append['caps'] = 0
    for article in df.text[1:]:
        caps = 0
        words = s.split()
        for word in words:
            if len(word) > 1:
                if word == word.upper():
                    caps += 1
    df['caps'] = caps

def count_misspellings():
    c = 0   
    return 0



if __name__ == '__main__':
    print 'building features'
