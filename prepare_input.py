from nemo.collections.nlp.models import PunctuationCapitalizationModel
import argparse
import contextualSpellCheck
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm") 

contextualSpellCheck.add_to_pipe(nlp)

# to get the list of pre-trained models
#PunctuationCapitalizationModel.list_available_models()

# Download and load the pre-trained BERT-based model
model = PunctuationCapitalizationModel.from_pretrained("punctuation_en_bert")

parser = argparse.ArgumentParser(description='baseline')
parser.add_argument('--path', type=str, default='./input.txt')
parser.add_argument('--mode', type=str, default='single')
parser.add_argument('--save', type=str, default='./')


args = parser.parse_args()

mode = args.mode
path = args.path
save = args.save
save_path = args.save + 'punctuated.txt'

if mode == 'single':
    with open(path, "r") as f:
        text = f.read().replace('\n', '')
    
    print("Text = ", text)
    punkted = model.add_punctuation_capitalization([text.lower()])[0]
    #corrected = str(TextBlob(text.lower()).correct())
    print("Punkted =", punkted)
    doc = nlp(punkted.lower())
    corrected = doc._.outcome_spellCheck

    print("Corrected = ", corrected)
    #doc = nlp(punkted)
    # corrected = doc._.outcome_spellCheck

    f = open(save_path, "w")
    f.write(str(punkted))
    f.close()
