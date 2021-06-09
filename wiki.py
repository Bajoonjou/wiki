import wikipedia
import yake

def ExtractKeysFromWiki(subject):
    wikipedia.set_lang("pt")
    sumario= wikipeida.summary(subject)

    kws = yake.KeywordExtractor(lan="pt")
    keyword = kws.extract_keywords(sumario)

    return keywords