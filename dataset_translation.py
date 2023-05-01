import pandas as pd
from deep_translator import GoogleTranslator
from dictionaries_translation import *

def translate_with_google(zno_orig):
    
    translate_features = ['areaname', 'tername', 'eoname', 'eoareaname', 'eotername', 'eoparent', \
                        'ukrptname', 'ukrptareaname', 'ukrpttername', 'histptname', 'histptareaname', \
                        'histpttername', 'mathptname', 'mathptareaname', 'mathpttername', \
                        'physptname', 'physptareaname', 'physpttername', 'chemptname', 'chemptareaname', \
                        'chempttername', 'bioptname', 'bioptareaname', 'biopttername', 'geoptname', \
                        'geoptareaname', 'geopttername', 'engptname', 'engptareaname', 'engpttername', \
                        'deuptname', 'deuptareaname', 'deupttername', 'fraptname', 'fraptareaname', \
                        'frapttername', 'spaptname', 'spaptareaname', 'spapttername']
    translator_google = GoogleTranslator(source='uk', target='en')

    # translate all pharases and save them to the list
    translated_columns = []
    for feature in translate_features:
        to_tr = zno_orig[feature].unique()
        print("translating", feature, len(to_tr))
        translated_google = {}
        for el in to_tr:
            if not pd.isnull(el):
                translated_google[el] = translator_google.translate(el)
        translated_columns.append(translated_google)
    
    # change dataset by replacing original phrases with the translated ones
    for feat_i in range(len(translate_features)):
        print("translating", translate_features[feat_i], len(zno_orig[translate_features[feat_i]].unique()))
        for i in range(0, len(translated_columns[feat_i]) + 1, 1000):
            tr_now = dict(list(translated_columns[feat_i].items())[i:i+1000])
            zno_orig.replace({translate_features[feat_i]: tr_now}, inplace=True)
        print(len(zno_orig[translate_features[feat_i]].unique()))

    return zno_orig

def translate_lang_dict(zno_translated):
    lang_features = ["classlangname", "histlang", "mathlang", "physlang", "chemlang", "biolang", "geolang"]
    for feature in lang_features:
        zno_translated[feature] = zno_translated[feature].replace(lang_dict)
    return zno_translated

def translate_region_dict(zno_translated):
    region_features = ["regname", "eoregname", "ukrptregname", "histptregname", "mathptregname", \
                       "physptregname", "chemptregname", "bioptregname", "geoptregname", \
                       "engptregname", "deuptregname", "fraptregname", "spaptregname"]
    for feature in region_features:
        zno_translated[feature] = zno_translated[feature].replace(region_dict)
    return zno_translated

def translate_tests_dict(zno_translated):
    tests_features = ["ukrtest", "histtest", "mathtest", "phystest", "chemtest", "biotest", \
                      "geotest", "engtest", "deutest", "fratest", "spatest"]
    for feature in tests_features:
        zno_translated[feature] = zno_translated[feature].replace(tests_dict)
    return zno_translated

def translate_test_status_dict(zno_translated):
    test_status_features = ["ukrteststatus", "histteststatus", "mathteststatus", "physteststatus", "chemteststatus", \
                            "bioteststatus", "geoteststatus", "engteststatus", "deuteststatus", "frateststatus", "spateststatus"]
    for feature in test_status_features:
        zno_translated[feature] = zno_translated[feature].replace(test_status_dict)
    return zno_translated

def translate_dpa_level_dict(zno_translated):
    dpa_level_features = ["engdpalevel", "fradpalevel", "deudpalevel", "spadpalevel"]
    for feature in dpa_level_features:
        zno_translated[feature] = zno_translated[feature].replace(dpa_level_dict)
    return zno_translated

def translate_manually(zno_translated):
    zno_translated["sextypename"] = zno_translated["sextypename"].replace(sex_type_dict)
    zno_translated["classprofilename"] = zno_translated["classprofilename"].replace(class_profile_dict)
    zno_translated = translate_lang_dict(zno_translated)
    zno_translated = translate_region_dict(zno_translated)
    zno_translated["regtypename"] = zno_translated["regtypename"].replace(grad_type_dict)
    zno_translated["eotypename"] = zno_translated["eotypename"].replace(school_type_dict)
    zno_translated["tertypename"] = zno_translated["tertypename"].replace(settlment_type_dict)
    zno_translated = translate_tests_dict(zno_translated)
    zno_translated = translate_test_status_dict(zno_translated)
    zno_translated = translate_dpa_level_dict(zno_translated)
    return zno_translated

def translate_dataset():
    zno_orig = pd.read_csv('zno_preprocessed.csv')
    zno_translated = translate_with_google(zno_orig)
    zno_translated = translate_manually(zno_translated)
    zno_translated.to_csv("translated.csv", index=False)
