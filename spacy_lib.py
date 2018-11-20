import spacy
from spacy.matcher import Matcher

all_entities = []
def add_event_ent(matcher, doc, i, matches):
    label = doc.vocab.strings[matches[i][0]]
    print('Label====>', label)
    print('Doc  ====>', doc)
    _, start, end = matches[i]
    entity_type = None
    entity_type = doc.vocab.strings[label]

    entity = (entity_type, start, end)
    doc.ents += (entity,)


def initialize_spacy():
    nlp = spacy.load('en')

    ner = nlp.get_pipe('ner')
    ner.add_label('LICENSE')
    ner.add_label('EXPIRY')
    ner.add_label('ISSUED')

    matcher = Matcher(nlp.vocab)

    matcher.add('LICENSE', add_event_ent,
                # [{'LOWER': 'license'}, {'LOWER': 'number'}, {'ORTH': ':'}, {'IS_DIGIT': True}],
                [{'LOWER': 'license'}, {'LOWER': 'number'}, {'ORTH': ':'}, {}],
                [{'LOWER': 'credential'}, {'LOWER': 'number'}, {'ORTH': ':'}, {'ENT_TYPE': 'CARDINAL'}],
                [{'LOWER': 'identification'}, {'LOWER': 'number'}, {'ORTH': ':'}, {'ENT_TYPE': 'CARDINAL'}],
                [{'LOWER': 'identification'}, {'LOWER': 'number'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'license'}, {'LOWER': 'no'}, {'ORTH': '.'}, {'IS_DIGIT': True}],
                [{'LOWER': 'license'}, {'LOWER': 'no'}, {'ORTH': '.'}, {'IS_DIGIT': True}, {'ORTH': '.'}, {'IS_DIGIT': True}],
                )

    matcher.add('ISSUED', add_event_ent,
                # [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'issued'}, {'LOWER': 'on'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'issuance'}, {'lower': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'issuance'}, {'lower': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'effective'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {"SHAPE": "d/d/dddd"}],
                [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {"SHAPE": "dd/d/dddd"}],
                [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {"SHAPE": "d/dd/dddd"}],
                [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {"SHAPE": "dd/dd/dddd"}],
                [{'LOWER': 'issued'}, {'ORTH': ':'}, {"ENT_TYPE": "DATE", "IS_ALPHA": True}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "?"}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}],
                [{'LOWER': 'issued'}, {'ORTH': ':'}, {"ENT_TYPE": "DATE", "IS_ALPHA": True}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "?"},{}],
                [{'LOWER': 'issued'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {}]
                )

    matcher.add('EXPIRY', add_event_ent,
                [{'LOWER': 'expiration'}, {'LOWER': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True,'SHAPE': 'XXXX'}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {'ENT_TYPE': 'DATE', 'IS_DIGIT': True}],
                # [{'LOWER': 'date'}, {'LOWER': 'issued'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"SHAPE": "d/d/dddd"}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"SHAPE": "dd/d/dddd"}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"SHAPE": "d/dd/dddd"}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"SHAPE": "dd/dd/dddd"}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"ENT_TYPE": "DATE", "IS_ALPHA": True}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "?"}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {"ENT_TYPE": "DATE", "IS_ALPHA": True}, {"ENT_TYPE": "DATE", "IS_DIGIT": True}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "?"}, {}],
                # [{'LOWER': 'expiration'}, {'LOWER': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expiration'}, {'LOWER': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}, {'ENT_TYPE': 'DATE'}, {'ORTH': ','}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expiration'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expire'}, {'LOWER': 'on'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE'}],
                # [{'LOWER': 'expires'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {}],
                # [{'LOWER': 'expiration'}, {'LOWER': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True, 'SHAPE': 'XXXX'}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {}],
                # [{'LOWER': 'expiration'}, {'LOWER': 'date'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True, 'SHAPE': 'XXXX'}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {'ENT_TYPE': 'DATE', 'IS_DIGIT': True}],
                # [{'UPPER': 'EXPIRATION'}, {'UPPER': 'DATE'}, {'ORTH': ':'}, {'ENT_TYPE': 'DATE', 'IS_ALPHA': True,'SHAPE': 'XXXX'}, {'ENT_TYPE': 'DATE', 'ORTH': ',', 'OP': '?'}, {'ENT_TYPE': 'DATE', 'IS_DIGIT': True}]
            )

    return nlp, matcher


def split_entity(text):
    print('---------------SPACY----------------')
    print('---------------TEXT-----------------')
    print(text)
    nlp = None
    matcher = None
    doc = None
    nlp, matcher = initialize_spacy()
    doc = nlp(u"{}".format(text))
    matcher(doc)
    
    x = []
    labels = ('LICENSE', 'ISSUED', 'EXPIRY')
    for ent in doc.ents:
        if ent.label_ in labels:
            x.append(ent.text)

    return x



# {"example": ["September 30, 1971", "September 30 1971"], "pattern": [{"ENT_TYPE": "DATE", "IS_ALPHA": true}, {"ENT_TYPE": "DATE", "IS_DIGIT": true}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "*"}, {"ENT_TYPE": "DATE", "IS_DIGIT": true}], "label": "MY_DATE"}
# {"example": ["30 September, 1971", "30 September 1971"], "pattern": [{"ENT_TYPE": "DATE", "IS_DIGIT": true}, {"ENT_TYPE": "DATE", "IS_ALPHA": true}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "*"}, {"ENT_TYPE": "DATE", "IS_DIGIT": true}], "label": "MY_DATE"}
# {"example": ["1st day of September, 1971"], "pattern": [{"SHAPE": "dxx"}, {"LOWER": "day"}, {"LOWER": "of"}, {"ENT_TYPE": "DATE", "IS_ALPHA": true}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "*"}, {"ENT_TYPE": "DATE", "IS_DIGIT": true}], "label": "MY_DATE"}
# {"example": ["30th day of September, 1971"], "pattern": [{"SHAPE": "ddxx"}, {"LOWER": "day"}, {"LOWER": "of"}, {"ENT_TYPE": "DATE", "IS_ALPHA": true}, {"ENT_TYPE": "DATE", "ORTH": ",", "OP": "*"}, {"ENT_TYPE": "DATE", "IS_DIGIT": true}], "label": "MY_DATE"}
# {"example": ["1/1/1971"], "pattern": [{"SHAPE": "d/d/dddd"}], "label": "MY_DATE"}
# {"example": ["10/1/1971"], "pattern": [{"SHAPE": "dd/d/dddd"}], "label": "MY_DATE"}
# {"example": ["1/10/1971"], "pattern": [{"SHAPE": "d/dd/dddd"}], "label": "MY_DATE"}
# {"example": ["10/10/1971"], "pattern": [{"SHAPE": "dd/dd/dddd"}], "label": "MY_DATE"}
# {"example": ["1/1/71"], "pattern": [{"SHAPE": "d/d/dd"}], "label": "MY_DATE"}
# {"example": ["10/1/71"], "pattern": [{"SHAPE": "dd/d/dd"}], "label": "MY_DATE"}
# {"example": ["1/10/71"], "pattern": [{"SHAPE": "d/dd/dd"}], "label": "MY_DATE"}
# {"example": ["10/10/71"], "pattern": [{"SHAPE": "dd/dd/dd"}], "label": "MY_DATE"}