import pandas as pd

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


def create_id(dataset: pd.DataFrame, attr: str, id: str)-> pd.DataFrame:
    '''create id for schools'''
    dataset.loc[:,id] = dataset[attr]

    abbr = {'B':'В', 'E':'Е', 'H':'Н', 'M':'М',
            'T':'Т', 'I':'І', 'O':'О', 'P':'Р',
            'A':'А', 'K':'К', 'X':'Х', 'C':'С',
            'c':'с', 'e':'е', 'i':'і', 'o':'о',
            'y':'у', 'p':'р', 'a':'а', 'k':'к',
            'x': 'х', 'ы':'и',
            ' РАДИ':' ', ' РАДА': ' ',
            ' ради':' ', ' рада': ' ',
            'КЗ ':'Комунальний заклад ', 'КУ ':'Комунальна установа ',
            'ОНЗ ':'Опорний навчальний заклад ', 'ДНЗ ':'Державний навчальний заклад ',
            'ОЗЗСО ':'Опорний заклад загальної середньої освіти ', 'ЗНЗ ':'Загальноосвітній навчальний заклад ',
            'ЗЗСО ':'Заклад загальної середньої освіти ', 'ПЗО ':'Приватний заклад освіти ', 
            'ООЗ ':'Опорний освітній заклад ', 'ЗСО ':'Загальної середньої освіти ', 
            'ЗОШ ':'Загальноосвітня школа ', 'НВК ':'Навчально-виховний комплекс ', 
            'ВСП ': 'Відокремлений структурний підрозділ', 'СЗШ ':'Середня загальноосвітня школа ', 
            'ТОВ ': 'Товариство з обмеженою відповідальністю ', 
            'ОЗ ': 'Опорний заклад ', "-":'',  "–":'', "ЗШ ": "Загальноосвітня школа ",
            "'":'', "’":'', ",":'',"„":"","“": "", "«":'', "»":'',  "*":"", '"':"", ":":"", 
            ";": "", "!": "", "?":"", "_x000d_":'', '_x000D_':'', "_":'', 'нн':'н', 'НН':'Н', "№":""}

    for old_abb, new_abb in abbr.items():
        dataset.loc[:,id] = dataset[id].str.replace(old_abb, new_abb)

    dataset.loc[:,id] = dataset[id].str.replace(r"[\(\[\{].*?[\)\]\}]", '', regex=True)

    brackets = {"(", ")", "[", "]", "}", "{"}
    
    for bracket in brackets:
        dataset.loc[:,id] = dataset[id].str.replace(bracket, '')

    def del_rayon(name):
        t = name.split()
        t_lower = name.lower().split()
        for s in ['району', 'район']:
            if s in t_lower:
                i = t_lower.index(s)
                del t[i-1:i+1]
                return ' '.join(t)
        return name
    
    dataset['id'] = dataset['id'].apply(del_rayon)
    dataset.loc[:,id] = dataset[id].str.replace(r'[\s\r\n\t]+', '', regex=True)
    dataset.loc[:,id] = dataset[id].str.replace('ІШ', '3')
    dataset.loc[:,id] = dataset[id].str.replace('ІІІІ', '3')
    dataset.loc[:,id] = dataset[id].str.replace('ІІІ', '2')
    dataset.loc[:,id] = dataset[id].str.replace('||||', '3')
    dataset.loc[:,id] = dataset[id].str.replace('|||', '2')
    dataset.loc[:,id] = dataset[id].str.lower()

    dataset['id'] = dataset['id'].apply(lambda s: s if (len(s) and s[-1].isdigit()) else s[:-1])


    dct = {"no":"",
           'ої':'а',
           'села':'с', 'село':'с', 'селещна':'селищна',
           'сільська':'', 'сільськ':'', 'сільска':'', 'сільск':'',
           'района':'', 'район':'',
           'селищна':'', 'селищн':'',
           'міська':'', 'міськ':'',
           'обєднана':'',
           'ст.':'ступ', "ступ.":"ступ", 
           "ступеня":"ступ", "ступенів":"ступ", 
           "ступеню":"ступ",
           "області":"обл", "область":"обл", "област":"обл", 
           "місто":"м", "міста":"м",
           'і':'', 'ї':'', 
           'ґ':'г', 'є':'',
            ".":'',
           'загальносвтня':'загальноосвтня',
           'сльско':'сльсько',
           "фаховий":"",
           "комунальнийзакладосвти":"",
           "комунальногозакладу":'',
           "комунальнийзаклад":"",
           "комунальнийопорнийзакладосвти":'',
           "комунальнийопорнийзаклад":'',
           'державнаорганзацяустановазакладдержавнийнавчальнийзаклад':'',
           'державнаорганзацяустановазаклад':'',
           'державнийнавчальнийзаклад':'',
           'державнийзаклад':'',
           'ншорганзацйноправовформи':'',
           'товариствозобмеженоювдповдальнстю':'',
           'вдокремленийструктурнийпдроздл':'',
           'комунальнаорганзаця':'',
           'комунальнаустанова':'',
           'обднанатериторальнагромади':'',
           'територальнагромади':''}

    for symb in dct:
        dataset.loc[:,id] = dataset[id].str.replace(symb, dct[symb])
    

    dataset.loc[:,id] = dataset[id].str.replace('"', '', regex = True)
    dataset.loc[:,id] = dataset[id].str.replace(r'\\', '')

    return dataset
