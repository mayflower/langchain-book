# Nutzung von DBPedia und WikiData als Wissensquellen

Sowohl DBPedia (1) als auch Wikidata (2) sind öffentliche Knowledge Graphs (KGs), die Daten als Resource Description Framework (RDF) (3) speichern und über die SPARQL Query Language for RDF (4) abrufbar sind. Die Beispiele für dieses Projekt befinden sich im GitHub-Repository für dieses Buch (5) im Verzeichnis kg_search.
Ich werde hier nicht viel Zeit auf die Behandlung von RDF und SPARQL verwenden. Stattdessen bitte ich Dich, das einführende Kapitel Linked Data, the Semantic Web, and Knowledge Graphs in meinem Buch A Lisp Programmer Living in Python-Land: The Hy Programming Language (6) online zu lesen.

Wie wir im letzten Kapitel gesehen haben, ist ein Knowledge Graph (den ich oft mit KG abkürze) eine Graphdatenbank, die ein Schema verwendet, um Typen (sowohl Objekte als auch Beziehungen zwischen Objekten) und Eigenschaften zu definieren, die Eigenschaftswerte mit Objekten verbinden. Der Begriff "Knowledge Graph" ist ein allgemeiner Begriff und bezieht sich manchmal auch auf den spezifischen Knowledge Graph, der bei Google verwendet wird und mit dem ich während meiner Tätigkeit dort im Jahr 2013 gearbeitet habe. Hier verwenden wir KG, um auf die allgemeine Technologie der Speicherung von Wissen in Graphdatenbanken zu verweisen.

DBPedia und Wikidata sind ähnlich, jedoch mit einigen wichtigen Unterschieden. Hier ist eine Zusammenfassung einiger Gemeinsamkeiten und Unterschiede zwischen DBPedia und Wikidata:

- Beide Projekte zielen darauf ab, strukturierte Daten aus Wikipedia in verschiedenen Formaten und Sprachen bereitzustellen. Wikidata enthält auch Daten aus anderen Quellen, so dass es mehr Daten und mehr Sprachen enthält.
- Beide Projekte verwenden RDF als gemeinsames Datenmodell und SPARQL als Abfragesprache.
- DBPedia extrahiert Daten aus den Infoboxen der Wikipedia-Artikel, während Wikidata Daten sammelt, die sowohl von Benutzern als auch von automatisierten Bots über die Interfaces eingegeben werden.
- Wikidata benötigt Quellen für seine Daten, während DBPedia dies nicht tut.
- DBpedia ist in der Semantic-Web- und Linked-Open-Data-Gemeinschaft populärer, während Wikidata stärker in die Wikimedia-Projekte integriert ist.

Zum letzten Punkt: Ich persönlich bevorzuge DBPedia, wenn ich mit dem semantischen Web und verknüpften Daten experimentiere, vor allem, weil DBPedia-URIs für Menschen lesbar sind, während Wikidata-URIs abstrakt sind. Die folgenden URIs repräsentieren die Stadt Sedona (Arizona), in der ich lebe:
- DBPedia: https://dbpedia.org/page/Sedona,_Arizona
- Wikidata: https://www.wikidata.org/wiki/Q80041
In RDF schließen wir URIs in spitze Klammern wie <https://www.wikidata.org/wiki/Q80041> ein.
Wenn Sie das Kapitel über RDF und SPARQL in meinem bereits erwähnten Buch gelesen haben, dann wissen Sie, dass RDF-Daten durch Tripel dargestellt werden, bei denen jeder Teil benannt ist:
- Subjekt
- Eigenschaft
- Objekt
Wir werden uns in diesem Kapitel zwei ähnliche Beispiele ansehen, eines mit DBPedia und eines mit Wikidata. Beide Dienste verfügen über SPARQL-Endpunkt-Webanwendungen, die Du für die Erkundung beider KGs verwenden möchtest. Wir werden uns die DBPedia-Weboberfläche später ansehen. Hier ist die Wikidata-Webschnittstelle:

>>>BILD EINFÜGEN<<<

In dieser SPARQL-Abfrage steht das Präfix wd: für Wikidata-Daten, während das Präfix wdt: für Wikidata-Typ (oder Eigenschaft) steht. Das Präfix rdfs: steht für RDF Schema.

(1) https://www.dbpedia.org
(2) https://www.wikidata.org/wiki/Wikidata:Main_Page
(3) https://www.w3.org/RDF/
(4) https://www.w3.org/TR/rdf-sparql-query/
(5) https://github.com/mark-watson/langchain-book-examples
(6) https://leanpub.com/hy-lisp-python/read

## DBPedia als Datenquelle

DBpedia ist ein von der Gemeinschaft getragenes Projekt, das strukturierte Inhalte aus Wikipedia extrahiert und sie im Web als Knowledge Graph (KG) zur Verfügung stellt. Der KG ist eine wertvolle Ressource für Forscher und Entwickler, die auf strukturierte Daten aus Wikipedia zugreifen müssen. Durch die Verwendung von SPARQL-Abfragen an DBpedia als Datenquelle können wir eine Vielzahl von Anwendungen schreiben, darunter natürliche Sprachverarbeitung, maschinelles Lernen und Datenanalyse. Wir demonstrieren die Effektivität von DBpedia als Datenquelle, indem wir mehrere Beispiele vorstellen, die den Einsatz in realen Anwendungen veranschaulichen. Nach meiner Erfahrung ist DBpedia eine wertvolle Ressource für Forscher und Entwickler, die auf strukturierte Daten aus Wikipedia zugreifen müssen.
Im Allgemeinen beginnst Du Projekte, die DBPedia verwenden, indem du die verfügbaren Daten mit der Web-App https://dbpedia.org/sparql untersuchst, die in diesem Screenshot zu sehen ist:

>>>BILD einfügen<<<

Das folgende Listing der Datei dbpedia_generate_rdf_as_nt.py zeigt Python-Code, um eine SPARQL-Abfrage an DBPedia zu stellen und die Ergebnisse als RDF-Tripel im NT-Format in einer lokalen Textdatei zu speichern:

```
1 from SPARQLWrapper import SPARQLWrapper
2 from rdflib import Graph
3
4 sparql = SPARQLWrapper("http://dbpedia.org/sparql")
5 sparql.setQuery("""
6    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
7    PREFIX dbpedia: <http://dbpedia.org/resource>
8    PREFIX dbpprop: <http://dbpedia.org/property>
9
10 CONSTRUCT {
11    ?city dbpedia-owl:country ?country .
12    ?city rdfs:label ?citylabel .
13    ?country rdfs:label ?countrylabel .
14    <http://dbpedia.org/ontology/country> rdfs:label \
15 "country"@en. 
16    }
17    WHERE {
18            ?city rdf:type dbpedia-owl:City .
19            ?city rdfs:label ?citylabel .
20            ?city dbpedia-owl:country ?country .
21            ?country rdfs:label ?countrylabel .
22            FILTER (lang(?citylabel) = 'en')
23            FILTER (lang(?countrylabel) = 'en')
24         }
25        LIMIT 50
26 """)
27 sparql.setReturnFormat("rdf")
28 results = sparql.query().convert()
29
30 g = Graph()
31 g.parse(data=results.serialize(format="xml"), format="xml\
32 ")
33
34 print("\nresults:\n")
35 results = g.serialize(format="nt").encode("utf-8").decode\
36 ('utf-8')
37 print(results)
38
39 text_file = open("sample.nt", "w")
40 text_file.write(results)
41 text_file.close()
```

Hier ist die Ausgabe der Ergebnisse dieses Skripts (die meisten Ausgaben werden nicht angezeigt, und sie wurden manuell an die Seitenbreite angepasst):

```
1 $ python generate_rdf_as_nt.py
2 results:
3
4 <http://dbpedia.org/resource/Ethiopia>
5   <http://www.w3.org/2000/01/rdf-schema#label>
6   "Ethiopia"@en .
7 <http://dbpedia.org/resource/Valentin_Alsina,_Buenos_Aire\
8 s>
9    <http://www.w3.org/2000/01/rdf-schema#label>
10   "Valentin Alsina, Buenos Aires"@en .
11 <http://dbpedia.org/resource/Davyd-Haradok>
12   <http://dbpedia.org/ontology/country>
13   <http://dbpedia.org/resource/Belarus> .
14 <http://dbpedia.org/resource/Davyd-Haradok>
15   <http://www.w3.org/2000/01/rdf-schema#label>
16   "Davyd-Haradok"@en .
17 <http://dbpedia.org/resource/Belarus>
18   <http://www.w3.org/2000/01/rdf-schema#label>
19   "Belarus"@en .
20 ...
 ```

 Diese Ausgabe wurde in eine lokale Datei sample.nt geschrieben. Ich habe dieses Beispiel in zwei separate Python-Skripte aufgeteilt, weil ich dachte, dass es für dich, lieber Leser, einfacher wäre, mit dem separaten Abrufen von RDF-Daten und der Verwendung eines LLM zur Verarbeitung der RDF-Daten zu experimentieren. In der Praxis wirst du vermutlich KG-Abfragen mit semantischer Analyse kombinieren wollen.
Dieses Codebeispiel demonstriert die Verwendung des GPTSimpleVectorIndex zur Abfrage von RDF-Daten und zum Abrufen von Informationen über Länder. Die Funktion download_loader lädt Datenimporteure nach Stringnamen. Es ist zwar nicht typsicher, eine Python-Klasse über den Namen einer Zeichenkette zu laden, aber wenn du den Namen der zu ladenden Klasse beim Aufruf von download_loader falsch schreibst, wird ein Python ValueError("Loader class name not found in library") Fehler ausgegeben. Die Klasse GPTSimpleVectorIndex stellt eine Indexdatenstruktur dar, die zum effizienten Suchen und Abrufen von Informationen aus den RDF-Daten verwendet werden kann. Dies ist vergleichbar mit anderen Typen von LlamaIndex-Vektor-Index-Typen für unterschiedliche Arten von Datenquellen.
Hier ist das Skript dbpedia_rdf_query.py:

```
1 "Example from documentation"
2
3 from llama_index import GPTSimpleVectorIndex, Document
4 from llama_index import download_loader
5
6 RDFReader = download_loader("RDFReader")
7 doc = RDFReader().load_data("sample.nt")
8 index = GPTSimpleVectorIndex(doc)
9
10 result = index.query("list all countries in a quoted Pyth\
11 on array, then explain why")
12
13 print(result.response)
```

Hier das Ergebnis:

```
1 $ python rdf_query.py
2 INFO:root:> [build_index_from_documents] Total LLM token\
3 usage: 0 tokens
4 INFO:root:> [build_index_from_documents] Total embedding\
5 token usage: 761 tokens
6 INFO:root:> [query] Total LLM token usage: 921 tokens
7 INFO:root:> [query] Total embedding token usage: 12 tokens
8
9 ['Argentina', 'French Polynesia', 'Democratic Republic of\
10 the Congo', 'Benin', 'Ethiopia', 'Australia', 'Uzbekista
11 n', 'Tanzania', 'Albania', 'Belarus', 'Vanuatu', 'Armenia
12 ', 'Syria', 'Andorra', 'Venezuela', 'France', 'Vietnam',
13 'Azerbaijan']
14
15 This is a list of all the countries mentioned in the cont\
16 ext information. All of the countries are listed in the c
17 ontext information, so this list is complete.
```

Warum sind dort nur 18 Länder gelistet? Im Skript für die SPARQL Suche auf DBPedia hatten wir am Ende der Suche ein Statement **LIMIT 50**. Deshalb wurden nur 50 RDF Tripel in die Datei **sample.net** geschrieben, die nur Daten für 18 Länder enthält.

## Wikidata als Datenquelle

Im Vergleich zu DB-Pedia ist es etwas schwieriger, Wikidata zu erschließen. Schauen wir uns noch einmal an, wie ich Informationen über meine Heimatstadt Sedona Arizona erhalte.
Beim Schreiben dieses Beispiels habe ich mit SPARQL-Abfragen experimentiert, indem ich die Wikidata SPARQL Web App (7) verwendet habe.
Wir können damit beginnen, RDF-Anweisungen mit dem Objektwert "Sedona" zu erhalten, indem wir die Wikidata-Webanwendung verwenden:

```
1 select * where {
2    ?s ?p "Sedona"@en
3 } LIMIT 30
```

Zunächst schreiben wir ein Hilfsprogramm zur Erfassung von Prompt-Text für einen Entitätsnamen (z. B. Name einer Person, eines Ortes usw.) in die Datei **wikidata_generate_prompt_text.py**:

(7) https://query.wikidata.org

```
1 from SPARQLWrapper import SPARQLWrapper, JSON
2 from rdflib import Graph
3 import pandas as pd
4
5 def get_possible_eitity_uris_from_wikidata(entity_name):
6    sparql = SPARQLWrapper("https://query.wikidata.org/spa\rql")
7
8    sparql.setQuery("""
9        SELECT ?entity ?entityLabel WHERE {
10        ?entity rdfs:label "%s"@en .
11        } limit 5
12   """ % entity_name)
13
14    sparql.setReturnFormat(JSON)
15    results = sparql.query().convert()
16
17    results = pd.json_normalize(results['results']['bindin\
18 gs']).values.tolist()
19    results = ["<" + x[1] + ">" for x in results]
20    return [*set(results)] # remove duplicates
21    
22 def wikidata_query_to_df(entity_uri):
23    sparql = SPARQLWrapper("https://query.wikidata.org/spa\rql")
24
25   sparql.setQuery("""
26        SELECT ?description ?is_a_type_of WHERE {
27            %s schema:description ?description FILTER (lang(?\
28 description)='en') .
29            %s wdt:P31 ?instanceOf .
30            ?instanceOf rdfs:label ?is_a_type_of FILTER (lang\
31 (?is_a_type_of)='en') .
32      } limit 10
33   """ % (entity_uri, entity_uri))
34
35   sparql.setReturnFormat(JSON)
36    results = sparql.query().convert()
37    results2 = pd.json_normalize(results['results']['bindi\
38 ngs'])
39    prompt_text = ""
40    for index, row in results2.iterrows():
41        prompt_text += row['description.value'] + " is a \
42 typeof " + row['is_a_type_of.value'] + "\n"
43    return prompt_text
44
45 def generate_prompt_text(entity_name):
46    entity_uris = get_possible_eitity_uris_from_wikidata(e\
47 ntity_name)
48    prompt_text = ""
49    for entity_uri in entity_uris:
50    p = wikidata_query_to_df(entity_uri)
51    if "disambiguation page" not in p:
52        prompt_text += entity_name + " is " + wikidata\
53 _query_to_df(entity_uri)
54    return prompt_text
55
56 if__name__ == "__main__":
57    print("Sedona:", generate_prompt_text("Sedona"))
58    print("California:",
59        generate_prompt_text("California"))
60    print("Bill Clinton:",
61         generate_prompt_text("Bill Clinton"))
62   print("Donald Trump:",
63        generate_prompt_text("Donald Trump"))
```

Dieses Dienstprogramm erledigt den größten Teil der Arbeit, um den Prompt-Text für eine Entität zu erhalten.
Die Klasse GPTTreeIndex ähnelt den anderen Indexklassen von LlamaIndex. Diese Klasse baut einen baumbasierten Index der Prompt-Texte auf, der verwendet werden kann, um Informationen basierend auf der Eingabefrage abzurufen. In LlamaIndex wird ein GPTTreeIndex verwendet, um die Child-Knoten auszuwählen, an die die Anfrage gesendet werden soll. Ein GPTKeywordTableIndex verwendet Keyword Matching und ein GPTVectorStoreIndex verwendet Embedding Cosine Similarity. Die Wahl der zu verwendenden Indexklasse hängt davon ab, wie viel Text indiziert werden soll, wie granular der Inhalt des Textes ist und ob Sie eine Zusammenfassung wünschen.
GPTTreeIndex ist auch effizienter als GPTSimpleVectorIndex, da er eine Baumstruktur zur Datenspeicherung verwendet. Dies ermöglicht ein schnelleres Suchen und Abrufen von Daten im Vergleich zu einer linearen Listenindexklasse wie GPTSimpleVectorIndex.
Der LlamaIndex-Code ist relativ einfach im Skript wikidata_query.py zu implementieren (an die Seitenbreite angepasst):

```
1 from llama_index import StringIterableReader, GPTTreeIndex
2 from wikidata_generate_prompt_text import generate_prompt\
3 _text
4
5 def wd_query(question, *entity_names):
6    prompt_texts = []
7       for entity_name in entity_names:
8           prompt_texts +=
9            [generate_prompt_text(entity_name)]
10   documents =
11    StringIterableReader().load_data(texts=prompt_texts)
12    index = GPTTreeIndex(documents)
13    return index.query(question)
14
15 if__name__== "__main__":
16    print("Sedona:", wd_query("What is Sedona?", "Sedona"))
17    print("California:",
18        wd_query("What is California?", "California"))
19    print("Bill Clinton:",
20    wd_query("When was Bill Clinton president?",
21             "Bill Clinton"))
22    print("Donald Trump:",
23    wd_query("Who is Donald Trump?",
24             "Donald Trump"))
```

Hier ist die Testausgabe (einige Zeilen wurden entfernt):

```
1 $ python wikidata_query.py
2 Total LLM token usage: 162 tokens
3 INFO:llama_index.token_counter.token_counter:> [build_ind\
4 ex_from_documents] INFO:llama_index.indices.query.tree.le
5 af_query:> Starting query: WhatisSedona?
6 INFO:llama_index.token_counter.token_counter:> [query]To\
7 tal LLM token usage: 154 tokens
8 Sedona: Sedona is a city in the United States located in \
9 the counties of Yavapai and Coconino, Arizona. It is also
10 the title of a 2012 film, a company, and a 2015 single b
11 y Houndmouth.
12
13 Total LLM token usage: 191 tokens
14 INFO:llama_index.indices.query.tree.leaf_query:> Starting\
15 query: What is California?
16 California: California is a U.S. state in the UnitedStat\
17 es of America.
18
19 Total LLM token usage: 138 tokens
20 INFO:llama_index.indices.query.tree.leaf_query:> Starting\
21 query: When was Bill Clinton president?
22 Bill Clinton: Bill Clinton was the 42nd President of  the\
23 United States from 1993 to 2001.
24
25 Total LLM token usage: 159 tokens
26 INFO:llama_index.indices.query.tree.leaf_query:> Starting\
27 query: Who is Donald Trump?
28 Donald Trump: Donald Trump is the 45th President of the U\
29 nited States, serving from 2017 to 2021.
```
