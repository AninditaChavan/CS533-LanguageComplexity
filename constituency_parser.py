import benepar, spacy

nlp = spacy.load('en_core_web_md')
nlp.add_pipe('benepar', config={'model': 'benepar_en3'})


doc = nlp("Tell us about an interesting trip that you went on when you were young adult, anywhere from twenty to forty years old. I would say Am in January of twenty twenty, I visited a lost Angeles, California, which was pretty fun. Am I really enjoy the weather when I was there? Ah, this was before the fandamac, and we didn't really know anything about the pan ti make, but the trip itself is really fun. Am, when a lat, I did a lout of sight seeing Am ate a lot, which is really fun. And Oh, did a height Soi the Hollywood sign, which is pretty Col am ji. I think of what else all Wark walks on? The. What is it called the star? The store, S pothe Star walk is not a starwalk. Don't walk a Fame Hollo, Fame star fame, Something with celebrities that was fun.")

print("Here")
sentences = list(doc.sents)
print("Parsing sentences =", sentences)
parsed = ""
for s in sentences:
    # (S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
    parsed += s._.parse_string
    # print(s._.labels)
    # ('S',)

    # print(list(s._.children)[0])

    #save parsed output to file

    # The time for action

parsed_output_file = open("parsed.txt", "w")
f = parsed_output_file.write(parsed)
parsed_output_file.close()


# import benepar, spacy
# nlp = spacy.load('en_core_web_md')
# nlp.add_pipe('benepar', config={'model': 'benepar_en3'})
# doc = nlp('The time for action is now. It is never too late to do something.')
# sent = list(doc.sents)[0]
# print(sent._.parse_string)
# # (S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
# print(sent._.labels)
# # ('S',)
# print(list(sent._.children)[0])
# # The time for action