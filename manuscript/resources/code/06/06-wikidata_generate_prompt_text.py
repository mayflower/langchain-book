from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph
import pandas as pd

def get_possible_eitity_uris_from_wikidata(entity_name):
  sparql = SPARQLWrapper("https://query.wikidata.org/spa\rql")

  sparql.setQuery("""
      SELECT ?entity ?entityLabel WHERE {
       ?entity rdfs:label "%s"@en .
       } limit 5
  """ % entity_name)

   sparql.setReturnFormat(JSON)
   results = sparql.query().convert()

   results = pd.json_normalize(results['results']['bindin\
gs']).values.tolist()
   results = ["<" + x[1] + ">" for x in results]
   return [*set(results)] # remove duplicates
    
def wikidata_query_to_df(entity_uri):
   sparql = SPARQLWrapper("https://query.wikidata.org/spa\rql")

   sparql.setQuery("""
       SELECT ?description ?is_a_type_of WHERE {
           %s schema:description ?description FILTER (lang(?\
description)='en') .
           %s wdt:P31 ?instanceOf .
           ?instanceOf rdfs:label ?is_a_type_of FILTER (lang\
(?is_a_type_of)='en') .
     } limit 10
  """ % (entity_uri, entity_uri))

   sparql.setReturnFormat(JSON)
   results = sparql.query().convert()
   results2 = pd.json_normalize(results['results']['bindi\
ngs'])
   prompt_text = ""
   for index, row in results2.iterrows():
       prompt_text += row['description.value'] + " is a \
typeof " + row['is_a_type_of.value'] + "\n"
   return prompt_text

def generate_prompt_text(entity_name):
    entity_uris = get_possible_eitity_uris_from_wikidata(e\
ntity_name)
    prompt_text = ""
    for entity_uri in entity_uris:
    p = wikidata_query_to_df(entity_uri)
    if "disambiguation page" not in p:
        prompt_text += entity_name + " is " + wikidata\
_query_to_df(entity_uri)
   return prompt_text
if__name__ == "__main__":
   print("Sedona:", generate_prompt_text("Sedona"))
   print("California:",
       generate_prompt_text("California"))
   print("Bill Clinton:",
        generate_prompt_text("Bill Clinton"))
   print("Donald Trump:",
       generate_prompt_text("Donald Trump"))