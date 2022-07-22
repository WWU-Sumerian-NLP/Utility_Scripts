import pandas as pd 

'''
1. Import to a pandas pd 
2. Only Keep dataframes with xpostags of NE (to denote Named Entity)
3. Sort by NER tags
4. Iterae through each category of NER tags
    5. Open up the corresponding csv file 
    6. Append name to taglist 


One minor bug exists - If a csv file has no entiries, it will write it on the headers

This is easy to fix post-processing, but something to be aware of
'''

def load_and_organize_data(pathToLabeledNERData):
    df = pd.read_csv(pathToLabeledNERData)
    df.drop(df.loc[df['XPOSTAG'] != 'NE'].index, inplace=True)
    df.drop(columns=['ID', 'XPOSTAG'], inplace=True)
    df.sort_values('NER', inplace=True)
    return df 

def extract_ner_tags(df, tag):
    df_w_tag = df[df["NER"] == tag]
    print(df_w_tag)
    return df_w_tag 

def write_to_existing_ner_lists(df, corresponding_ner_list, isTest):
    if isTest:
        corresponding_ner_list = "tests/extract_ner_tags_from_mtacc_test.csv"
        df.to_csv(corresponding_ner_list, mode="a", index=False, header=False)
    else:
        entire_path = "../Data_Pipeline_go/Annotation_lists/NER_lists/" + corresponding_ner_list
        df.to_csv(entire_path, mode="a", index=False, header=False)


def main():
    df = load_and_organize_data("Augmented_NER_training_ml.csv")
   

    ner_tags = ["LN", "AN", "CN", "QN", "DN", "EN", "FN", "GN", "ON", "TN", "WN"]
    ner_lists = ["ancestral_clan_line_ner.csv", "agricultural_locus_ner.csv", "celestial_ner.csv",
    "city_quarter_ner.csv", "divine_ner.csv", "ethnos_ner.csv", "field_ner.csv", "geographical_ner.csv",
    "object_ner.csv", "temple_ner.csv", "watercourse_ner.csv"]

    for i in range(len(ner_tags)):
        print(ner_tags[i])
        df_w_tag = extract_ner_tags(df, ner_tags[i])
        write_to_existing_ner_lists(df_w_tag, ner_lists[i], True) #test
        # write_to_existing_ner_lists(df_w_tag, ner_lists[i], False) #real


main()
'''
NER Tags 
________________

DN	Divine Name
EN	Ethnos Name
GN	Geographical Name*
MN	Month Name
ON	Object Name
PN	Personal Name
RN	Royal Name
SN	Settlement Name
TN	Temple Name
WN	Watercourse Name
AN	Agricultural (locus) Name
CN	Celestial Name
FN	Field Name
LN	Line Name (ancestral clan)
QN	Quarter Name (city area)
YN	Year Name


'''