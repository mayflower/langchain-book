# Die Nutzung von Googles Knowledge Graph APIs mit LangChain

Googles Knowledge Graph (KG) ist eine Wissensbasis, mit deren Hilfe Google relevante Informationen in einer Infobox neben den Suchergebnissen anzeigt. Sie ermöglicht es dem Nutzer, die Antwort mit einem Blick zu sehen, wie eine sofortige Antwort. Die Daten werden automatisch aus einer Vielzahl von Quellen ermittelt, die Orte, Personen, Unternehmen und mehr enthalten. Ich arbeitete 2013 in einem Projekt bei Google, das den eigenen KG für ein internes Projekt nutzte.

Mit der öffentlichen Knowledge Graph Search API von Google kannst du Entitäten im Google Knowledge Graph finden. Die API verwendet standardmäßige schema.org-Typen und ist konform mit der JSON-LD-Spezifikation. Sie unterstützt das Suchen und Nachschlagen von Entitäten.

Du kannst die Knowledge Graph Search API zur Erstellung von Anwendungen nutzen, die Google Knowledge Graph verwenden. Zum Beispiel kannst Du die API verwenden, um eine Suchmaschine zu bauen, die Ergebnisse auf der Grundlage der Entitäten im Knowledge Graph ausgibt.

Im nächsten Kapitel benutzen wir auch DBPedia und Wikidata aus dem öffentlichen KG. Eine Begrenzung von Googles KP API ist, dass sie zum Nachschlagen von Entitäten (Menschen, Orte, Organisationen, etc.) designt ist. DBPedia und Wikidata ermöglichen es, mit der SPARQL Query Language eine größere Bandbreite von Informationen zu finden, wie z.B. Beziehungen zwischen Entitäten. Du kannst mit der Google KP API einige Beziehungen zwischen Entitäten finden, z.B. alle Filme eines bestimmten Regisseurs oder alle Bücher eines bestimmten Autors. Du kannst mit der API auch Informationen finden wie etwa alle Menschen, die an einem bestimmten Film mitgewirkt haben, oder alle Schauspieler, die in einer bestimmten TV Show aufgetreten sind.

## Den Zugriff auf Google Knowledge Graph-APIs einrichten

Um einen API Key für die Google Knowledge Graph Search API zu bekommen, musst Du zur Google API Console gehen, die Google Knowledge Graph Search API aktivieren und einen API Key für dein Projekt erstellen. Dann kannst du mit diesem API Key Anfragen an die Knowledge Graph Search API stellen.

Mit diesen Schritten generierst du den API Key:

* gehe zur API Console
* wähle ein Projekt aus der Projektliste oder erstelle ein neues
* falls die Seite "APIs & Services" noch nicht geöffnet ist, öffne das Menü auf der linken Seite und wähle "APIs & Services" aus
* wähle links "Anmeldedaten" aus
* klicke "Anmeldedaten erstellen" und wähle dann API Key aus

Danach kannst du diesen API Key für Anfragen an die Knowledge Graph Search API verwenden.

Wenn ich Googles APIs verwende, setze ich den Access Key in **~/.google_api_key** und lese den Key so ein:

```
1 api_key=open(str(Path.home())+"/.google_api_key").read()
```

Du kannst auch Umgebungsvariablen zum Speichern von Access Keys nutzen. Hier ein Codeschnipsel für einen API-Aufruf, der Informationen über mich einholt:

```python
1   import json
2   from urllib.parse import urlencode
3   from urllib.request import urlopen
4   from pathlib import Path
5   from pprint import pprint
6
7   api_key =
8       open(str(Path.home()) + "/.google_api_key").read()
9   query = "Mark Louis Watson"
10  service_url =
11      "https://kgsearch.googleapis.com/v1/entities:search"
12  params = {
13      "query": query,
14      "limit": 10,
15      "indent": True,
16      "key": api_key,
17  }
18  url = service_url + "?" + urlencode(params)
19  response = json.loads(urlopen(url).read())
20  pprint(response)
```

Die Ausgabe von JSON-LD würde so aussehen:

```
1   {'@context': {'@vocab': 'http://schema.org/',
2                 'EntitySearchResult':
3                 'goog:EntitySearchResult',
4                 'detailedDescription':
5                 'goog:detailedDescription',
6                 'goog': 'http://schema.googleapis.com/',
7                 'kg': 'http://g.co/kg',
8                 'resultScore': 'goog:resultScore'},
9   '@type': 'ItemList',
10  'itemListElement': [{'@type': 'EntitySearchResult',
11                       'result': {'@id': 'kg:/m/0b6_g82',
12                                  '@type': ['Thing',
13                                            'Person'],
14                                  'description': 'Author',
15                                  'name':
16                                  'Mark Louis Watson',
17                                  'url':
18                                  'http://markwatson.com'},
19                       'resultScore': 43}]}
```

Damit der Code zum Abrufen von Entitätsinformationen von Google KG nicht wiederholt werden muss, habe ich das Dienstprogramm **Google_KG_helper.py** geschrieben, das den vorhergehenden Code einschließt und in eine Mini-Library generalisiert:

```python
1 """Client for calling Knowledge Graph Search API."""
2
3  import json
4  from urllib.parse import urlencode
5  from urllib.request import urlopen
6  from pathlib import Path
7  from pprint import pprint
8
9  api_key =
10       open(str(Path.home()) + "/.google_api_key").read()
11
12   # use Google search API to get information
13   # about a named entity:
14
15   def get_entity_info(entity_name):
16       service_url =
17         "https://kgsearch.googleapis.com/v1/entities:search"
18       params = {
19           "query": entity_name,
20           "limit": 1,
21           "indent": True,
22           "key": api_key,
23       }
24       url = service_url + "?" + urlencode(params)
25       response = json.loads(urlopen(url).read())
26       return response
27
28   def tree_traverse(a_dict):
29       ret = []
30       def recur(dict_2, a_list):
31           if isinstance(dict_2, dict):
32               for key, value in dict_2.items():
33                   if key in ['name', 'description',
34                              'articleBody']:
35                       a_list += [value]
36                   recur(value, a_list)
37           if isinstance(dict_2, list):
38               for x in dict_2:
39                   recur(x, a_list)
40       recur(a_dict, ret)
41       return ret
42
43
44   def get_context_text(entity_name):
45       json_data = get_entity_info(entity_name)
46       return ' '.join(tree_traverse(json_data))
47
48   if __name__ == "__main__":
49       get_context_text("Bill Clinton")
```

Das Haupttestskript ist in der Datei **Google_Knowledge_Graph_Search.py**:

```python
1   """Example of Python client calling the
2      Knowledge Graph Search API."""
3
4   from llama_index import GPTListIndex, Document
5
6   import Google_KG_helper
7
8   def kg_search(entity_name, *questions):
9        ret = ""
10       context_text =
11         Google_KG_helper.get_context_text(entity_name)
12       print(f"Context text: {context_text}")
13       doc = Document(context_text)
14       index = GPTListIndex([doc])
15       for question in questions:
16           response = index.query(question)
17           ret +=
18             f"QUESTION: {question}\nRESPONSE: {response}\n"
19       return ret
20
21   if __name__ == "__main__":
22       s = kg_search("Bill Clinton",
23                     "When was Bill president?")
24       print(s)
```

Die Ausgabe für das Beispiel ist:

```
1   $ python Google_Knowledge_Graph_Search.py
2   Context text: Bill Clinton 42nd U.S. President William Je\
3   fferson Clinton is an American retired politician who ser
4   ved as the 42nd president of the United States from 1993
5   to 2001.
6   INFO:root:> [build_index_from_documents] Total LLM token \
7   usage: 0 tokens
8   INFO:root:> [build_index_from_documents] Total embedding \
9   token usage: 0 tokens
10  INFO:root:> [query] Total LLM token usage: 77 tokens
11  INFO:root:> [query] Total embedding token usage: 0 tokens
12  QUESTION: When was Bill president?
13  RESPONSE:
14  Bill Clinton was president from 1993 to 2001.
```

Der Zugriff auf Knowledge Graphs von Google, DBPedia und Wikidata ermöglicht es dir, Fakten und Wissen aus der realen Welt in deine Anwendungen zu integrieren. Ich arbeite zwar hauptsächlich im Bereich des Deep Learning, benutze aber auch häufig Knowledge Graphs in meiner Arbeit und für meine persönlichen Recherche. Ich denke, dass du, werter Leser, den Zugriff auf hochstrukturierte Daten in KGs zuerlässiger und in vielen Fällen einfacher finden wirst als Web Scraping.
