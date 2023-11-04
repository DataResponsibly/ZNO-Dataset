import pandas as pd
import string

def merging(df1: pd.DataFrame, df2: pd.DataFrame, lst_on: list)->pd.DataFrame:
    '''Merging two pandas Dataframe df1 and df2 based on the list of
    parameters.'''
    try:
        output = df1.merge(df2, on=lst_on, how='left')
        output.loc[output['EDRPOU_y'].isna(), 'EDRPOU_y'] = ''
        output.loc[output['EDRPOU_x'] == '', 'EDRPOU_x'] = output.loc[output['EDRPOU_x'] == '', 'EDRPOU_y']
        output = output.drop(columns=['EDRPOU_y'], axis=1)
        output = output.rename(columns = {'EDRPOU_x':'EDRPOU'})
        print('Percentage matched:',round(output[output['EDRPOU'] != ''].shape[0]/output.shape[0]*100,1), '%')
        return output
    except:
        return None

def latin_to_cyrillic(dataset: pd.DataFrame,  attr: str)-> pd.DataFrame:
    '''replace all latin letters that are similar to cyrillic
    in the string attribute
    >>> dataset = pd.DataFrame({'id':['Настя', 'Hастя', 'Нiкiта', 'Нікіта']})
    >>> latin_to_cyrillic(dataset,'id')
           id
    0   Настя
    1   Настя
    2  Нікіта
    3  Нікіта
    '''
    letters = {'B':'В', 'E':'Е', 'H':'Н', 'M':'М',
            'T':'Т', 'I':'І', 'O':'О', 'P':'Р',
            'A':'А', 'K':'К', 'X':'Х', 'C':'С',
            'c':'с', 'e':'е', 'i':'і', 'o':'о',
            'y':'у', 'p':'р', 'a':'а', 'k':'к',
            'x': 'х', 'ы':'и'}

    for old_letter, new_letter in letters.items():
        dataset.loc[:,attr] = dataset[attr].str.replace(old_letter, new_letter)

    return dataset

def abbreviation_to_full_name(dataset: pd.DataFrame,  attr: str)-> pd.DataFrame:
    '''replace abbreviations by their full name
    in the string attribute
    >>> dataset = pd.DataFrame({'id':['КОНЗ " Новоселівський ЗЗСО I-III \
ступенів Куяльницької с/р Подільського району Одеської об"ласті']})
    >>> list(abbreviation_to_full_name(dataset,'id').id.unique())
    ['Комунальний опорний навчальний заклад " Новоселівський Заклад \
загальної середньої освіти I-III ступенів Куяльницької сільської ради Подільського \
району Одеської об"ласті']
    '''
    abbr = {
        'КЗЗСО ':'Комунальний заклад загальної середньої освіти ',
        'ОЗЗСО ':'Опорний заклад загальної середньої освіти ',
        'ЗЗСО ':'Заклад загальної середньої освіти ',
        'КОНЗ ':'Комунальний опорний навчальний заклад ',
        'ВСП ': 'Відокремлений структурний підрозділ ',
        'ЗДО ':'Заклад дошкільної освіти ',
        'ЗНЗ ':'Загальноосвітній навчальний заклад ',
        'ЗОШ ':'Загальноосвітня школа ',
        'КНЗ ':'Комунальний навчальний заклад ',
        'НВК ':'Навчально-виховний комплекс ', 
        'ОНЗ ':'Опорний навчальний заклад ',
        'ООЗ ':'Опорний освітній заклад ',
        'ПЗО ':'Приватний заклад освіти ',
        'СЗШ ':'Середня загальноосвітня школа ',
        'ТОВ ': 'Товариство з обмеженою відповідальністю ',
        "ЗШ ": "Загальноосвітня школа ",
        'КЗ ':'Комунальний заклад ', 
        'КУ ':'Комунальна установа ',
        'ОЗ ': 'Опорний заклад ',
        'с/р ': 'сільської ради '
        }

    for old_abb, new_abb in abbr.items():
        dataset.loc[:,attr] = dataset[attr].str.replace(old_abb, new_abb)

    return dataset

def dot_to_full_name(dataset: pd.DataFrame,  attr: str)-> pd.DataFrame:
    '''replace shor name with dot by their full name
    in the string attribute
    >>> dataset = pd.DataFrame({'id':['КОНЗ " Новоселівський ЗЗСО I-III \
ст. Куяльницької с/р м. Житомира']})
    >>> list(dot_to_full_name(dataset,'id').id.unique())
    ['КОНЗ " Новоселівський ЗЗСО I-III ступ Куяльницької с/р міста Житомира']
    '''
    abbr = {'ст.':'ступ', 'ім.':'імені', 'м.':'міста'}

    for old_abb, new_abb in abbr.items():
        dataset.loc[:,attr] = dataset[attr].str.replace(old_abb, new_abb)

    return dataset

def delete_punctuation(dataset: pd.DataFrame,  attr: str)-> pd.DataFrame:
    '''remove all punctuations
    in the string attribute
    >>> dataset = pd.DataFrame({'id':['КОНЗ " Новоселівський ЗЗСО I-III \
ступенів Куяльницької с/р (Подільського району} [Одеської об"ласті']})
    >>> list(delete_punctuation(dataset,'id').id.unique())
    ['КОНЗ  Новоселівський ЗЗСО IIII \
ступенів Куяльницької ср Подільського району Одеської області']
    '''
    punct = set(string.punctuation)
    punct |= {"»", "«", "“", "„", "’", "–", "№", '_x000D_'}

    for sign in punct:
        dataset.loc[:,attr] = dataset[attr].str.replace(sign, '')

    return dataset

def del_rayon(name:str)->str:
    '''delete name of rayon
    >>> del_rayon('КОНЗ " Новоселівський ЗЗСО I-III \
ступенів Куяльницької с/р Подільського району Одеської об"ласті')
    'КОНЗ " Новоселівський ЗЗСО I-III \
ступенів Куяльницької с/р Одеської об"ласті'
    '''
    t = name.split()
    t_lower = name.lower().split()
    for s in ['району', 'район']:
        if s in t_lower:
            i = t_lower.index(s)
            del t[i-1:i+1]
            return ' '.join(t)
    return name

def delete_status(dataset: pd.DataFrame,  attr: str)-> pd.DataFrame:
    '''replace abbreviations by their full name
    in the string attribute
    >>> dataset = pd.DataFrame({'id':['комунальнийопорнийнавчальнийзакладновоселвський\
закладзагальноїсередньоїосвіти3ступенівкуяльницькоїсільськоїодеськоїобласт']})
    >>> list(delete_status(dataset,'id').id.unique())
    ['новоселвськийзакладзагальноїсередньоїосвіти3ступенівкуяльницькоїсільськоїодеськоїобласт']
    '''
    status = {"фаховий", "no",
              "комунальнийзакладосвти", "комунальногозакладу",
              "комунальнийзаклад","комунальнийопорнийзакладосвти",
              'комунальнийопорнийнавчальнийзаклад',
              "комунальнийопорнийзаклад", 'закладзагальнасередньаосвти',
              'державнаорганзацяустановазакладдержавнийнавчальнийзаклад',
              'державнаорганзацяустановазаклад','державнийнавчальнийзаклад',
              'державнийзаклад','ншорганзацйноправовформи',
              'товариствозобмеженоювдповдальнстю',
              'вдокремленийструктурнийпдроздл',
              'комунальнаорганзаця',
              'комунальнаустанова',
              'обднанатериторальнагромади',
              'територальнагромади',
              'обєднана'}

    for stat in status:
        dataset.loc[:,attr] = dataset[attr].str.replace(stat, '')

    return dataset

def create_id(dataset: pd.DataFrame, attr: str, id_: str)-> pd.DataFrame:
    '''create id for schools
    >>> dataset = pd.DataFrame({'id':['КОНЗ " Новоселівський ЗЗСО I-III \
ступенів ім.М.В.Марченка Куяльницької с/р Подільського району Одеської об"ласті']})
    >>> list(create_id(dataset,'id', 'id_').id_.unique())
    ['новоселвський2ступменмвмарченкакуяльницькаодеськаобл']
    '''
    dataset.loc[:,id_] = dataset[attr]
    #delete everything inside brackets
    dataset.loc[:,id_] = dataset[id_].str.replace(r"[\(\[\{].*?[\)\]\}]", '', regex=True)
    dataset = latin_to_cyrillic(dataset, id_)
    dataset = abbreviation_to_full_name(dataset, id_)
    dataset = dot_to_full_name(dataset, id_)
    dataset = delete_punctuation(dataset, id_)

    to_change = {' РАДИ':' ', ' РАДА': ' ',
            ' ради':' ', ' рада': ' ',  
            'нн':'н', 'НН':'Н'}

    for old, new in to_change.items():
        dataset.loc[:,id_] = dataset[id_].str.replace(old, new)
    
    dataset[id_] = dataset[id_].apply(del_rayon)

    #delete spaces
    dataset.loc[:,id_] = dataset[id_].str.replace(r'[\s\r\n\t\b]+', '', regex=True)

    #replace roman numerals by digits
    dataset.loc[:,id_] = dataset[id_].str.replace('ІШ', '3')
    dataset.loc[:,id_] = dataset[id_].str.replace('ІІІІ', '3')
    dataset.loc[:,id_] = dataset[id_].str.replace('||||', '3')
    dataset.loc[:,id_] = dataset[id_].str.replace('ІІІ', '2')
    dataset.loc[:,id_] = dataset[id_].str.replace('|||', '2')
    
    dataset.loc[:,id_] = dataset[id_].str.lower()

    dataset[id_] = dataset[id_].apply(lambda s: s if (len(s) and s[-1].isdigit()) else s[:-1])

    dct = {'ої':'а',
           'села':'с', 'село':'с', 'селещна':'селищна', 'селищна':'', 'селищн':'',
           'сільська':'', 'сільськ':'', 'сільска':'', 'сільск':'',
           'района':'', 'район':'',
           'міська':'', 'міськ':'', 
           "ступеня":"ступ", "ступенів":"ступ", 
           "ступеню":"ступ",
           "області":"обл", "область":"обл", "област":"обл", 
           "місто":"м", "міста":"м",
           'і':'', 'ї':'',
           'ґ':'г', 'є':'',
           'загальносвтня':'загальноосвтня'}

    for old_symb, new_symb in dct.items():
        dataset.loc[:,id_] = dataset[id_].str.replace(old_symb, new_symb)
    
    dataset = delete_status(dataset, id_)
    return dataset


if __name__=='__main__':
    # import doctest
    # print(doctest.testmod())
    dataset = pd.DataFrame({'id':['Школа І-ІІІ ступенів № 1 Шевченківського району м. Київ']})
    print(list(create_id(dataset,'id', 'id_').id_.unique()))