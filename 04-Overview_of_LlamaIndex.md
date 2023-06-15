# Überblick über LlamaIndex

Das beliebte LlamaIndex-Projekt hieß früher GPT-Index, wurde aber erweitert, um mit mehr Modellen als nur GPT-3 zu funktionieren. Zum Beispiel werden [Hugging Face embeddings](https://gpt-index.readthedocs.io/en/latest/how_to/embeddings.html)[^1] verwendet.

[LlamaIndex](https://github.com/jerryjliu/gpt_index/blob/main/docs/index.rst)[^2] ist ein Projekt, das eine zentrale Schnittstelle zur Verbindung von Language models mit externen Daten bereitstellt. Es wurde im Herbst 2022 von Jerry Liu und seinem Team entwickelt. Es besteht aus einer Reihe von Datenstrukturen, [die die Nutzung großer externer Wissensdatenbanken mit Language models erleichtern sollen](https://gpt-index.readthedocs.io/en/latest/index.html)[^3]. Anwendungsfälle sind z.B.:

* Abfrage strukturierter Daten wie Tabellen oder Datenbanken über natürliche Sprache 
* Abrufen von relevanten Fakten oder Informationen aus großen Textkörpern
* Anreicherung von Sprachmodellen mit domänenspezifischem Wissen

LlamaIndex unterstützt eine Vielzahl von Dokumenttypen, u.a.:

* Textdokumente sind die häufigsten Dokumenttypen. Sie können in einer Vielfalt von Formaten gespeichert werden, wie z. B. .txt, .doc und .pdf.
* XML Dokumente sind Textdokumente, die zur Speicherung von Daten in strukturiertem Format verwendet werden.
* JSON-Dokumente sind Textdokumente, die zur Speicherung von Daten in schlankem Format verwendet werden.
* HTML-Dokumente sind Textdokumente, mit denen Webseiten erstellt werden.
* PDF-Dokumente sind Textdokumente, die zur Speicherung von Dokumenten in einem festen Format verwendet werden. 

[^1]: https://gpt-index.readthedocs.io/en/latest/how_to/embeddings.html
[^2]: https://github.com/jerryjliu/gpt_index/blob/main/docs/index.rst
[^3]: https://gpt-index.readthedocs.io/en/latest/index.html

LlamaIndex kann auch Daten indizieren, die in einer Vielzahl von Datenbanken gespeichert sind, u.a.:

* SQL-Datenbanken wie MySQL, PostgreSQL und Oracle. NoSQL-Datenbanken wie MongoDB, Cassandra und CouchDB.
* Solr ist eien beliebte Open-Source Suchmaschine mit hoher Performance und Skalierbarkeit.
* Elasticsearch ist eine weitere beliebte Open-Source Suchmaschine, die eine Vielzahl von Features aufweist, darunter Volltextsuche, Geodatensuche und Machine learning.
* Apache Cassanda ist eine NoSQL-Datenbank, die zur Speicherung großer Datenmengen verwendet werden kann.
* MongoDB ist eine weitere NoSQL-Datenbank, die einfach zu verwenden und skalieren ist.
* PostgreSQL ist eine relationale Datenbank, die verbreitet in Unternehmensappliaktionen verwendet wird

LlamaIndex ist ein flexibles Framework, das zur Indizierung einer Vielzahl von Dokumenttypen und Datenquellen benutzt werden kann.

Wir werden uns zuerst ein kurzes Beispiel aus der LllamaIndex-Dokumentation anschauen und später dann die Teile des LlamaIdex-Quellcodes, die LangChain verwenden.

## Verwendung von LlamaIndex für die Suche in lokalen Dokumenten mit GPT-3

Das folgende Beispiel ähnelt dem letzten Beispiel im Überblickskapitel zu LangChain. In Zeile 8 verwenden wir eine Hilfsfunktion zum Laden von Daten, die von LlamaIndex bereitgestellt wird, um Dokumente aus einem Eingabeordner zu lesen. Zur Demonstration speichern wir den Index (bestehend aus Document Embeddings) auf der Festplatte und laden ihn erneut. Diese Vorgehensweise ist nützlich, wenn man eine große Anzahl von statischen Dokumenten hat, wodurch der Indizierungsvorgang eine Weile dauern und viele OpenAI-API-Aufrufe erfordern kann. Man kann zum Beispiel viele Gigabytes an Firmendokumentation haben, die sich nicht oft ändert, sodass es sinnvoll ist, den Index nur gelegentlich neu zu erstellen.

```python
1 # Derived from a documentation example at:
2 # https://github.com/jerryjliu/gpt_index
3
4 # make sure you set the following environment variable
5 # is set: OPENAI_API_KEY
6
7 from llama_index import GPTSimpleVectorIndex,
8                         SimpleDirectoryReader
9 documents = SimpleDirectoryReader('../data').load_data()
10 index = GPTSimpleVectorIndex(documents)
11
12 # save to disk
13 index.save_to_disk('index.json')
14 # load from disk
15 index = GPTSimpleVectorIndex.load_from_disk('index.json')
16
17 # search for a document
18 r = index.query("effect of body chemistry on exercise?")
19 print(r)
```

Du hast sicherlich bemerkt, dass die in Zeile 17 definierte Abfrage dieselbe ist, die wir im vorigen Kapitel verwendet haben.

>REVIEW: vollständig andere Ausgabe in Version 2023-10-05

```
1 INFO:root:> [build_index_from_documents] Total LLM token\
2 usage: 0 tokens
3 INFO:root:> [build_index_from_documents] Total embedding\
4 token usage: 2272 tokens
5 INFO:root:> [query] Total LLM token usage: 1018 tokens
6 INFO:root:> [query] Total embedding token usage: 7 tokens
7
8 The effect of body chemistry on exercise can vary dependi\
9 ng on the individual. Factors such as hydration levels, e
10 lectrolyte balance, and the availability of energy-storin
11 g molecules such as adenosine triphosphate (ATP) can all
12 affect the bodys ability to perform exercise. Additionall
13 y, hormones such as adrenaline and cortisol can influence
14 the bodys response to exercise, as can the presence of c
15 ertain nutrients and minerals.
```

>REVIEW: nächster Absatz nicht mehr in Version 2023-10-05 enthalten

Beachten Sie, dass im Allgemeinen viele organische Chemikalien als Antwort auf die "Abfrage effect of body chemistry on exercise?" aufgelistet werden könnten, dass aber nur Adenosintriphosphat (ATP) in dem Testdokument in der Datei data/chemistry.txt erwähnt wurde.

## Verwendung von LlamaIndex zur Beantwortung von Fragen aus einer Liste von Webseiten

In diesem Beispiel verwenden wir die Bibliotheken **trafilatura** und **html2text**, um Text von einer Webseite zu erhalten, den wir indizieren und durchsuchen werden. Die Klasse **TrafilaturaWebReader** übernimmt die Erstellung lokaler Dokumente aus einer Liste von Webseiten-URIs und die Indexklasse **GPTListIndex** erstellt einen lokalen Index für die Verwendung mit OpenAI-API-Aufrufen zur Implementierung der Suche.

Das folgende Codebeispiel zeigt die Datei **web_page_QA.py**:

```python
1 # Derived from the example at:
2 # https://github.com/jerryjliu/gpt_index/blob/main/exampl\
3 es/data_connectors/WebPageDemo.ipynb
4
5 # pip install llama-index, html2text, trafilatura
6
7 from llama_index import GPTListIndex
8 from llama_index import TrafilaturaWebReader
9
10 def query_website(url_list,*questions):
11     documents = TrafilaturaWebReader().load_data(url_list)
12    index = GPTListIndex(documents)
13    for question in questions:
14        print(f"\n== QUESTION: {question}\n")
15        response = index.query(question)
16        print(f"== RESPONSE: {response}")
17
18 if __name__ == "__main__":
19    url_list = ["https://markwatson.com"]
20    query_website(url_list, "What programming languages doe\
21 s Markuse?",
22    "How many books has Mark writte\
23 n?",
24    "What musical instruments does \
25 Mark play?")
```

Dieses Beispiel ist nicht effizient, weil wir für jede Webseite, die wir durchsuchen wollen, einen neuen Index erstellen. Dennoch bietet es (das von einem Beispiel in der LlamaIndex-Dokumentation abgeleitet wurde) ein Muster, das du beispielsweise verwenden kannst, um einen wiederverwendbaren Index für die Website deines Unternehmens zu erstellen und eine Web-Suchanwendung für Endbenutzer zu entwickeln.

Die Ergebnisse für diese drei Testfragen im letzten Codebeispiel lauten:

>REVIEW: in neuer Version völlig andere Ausgabe

```shell
1 INFO:root:> [build_index_from_documents] Total LLM token\
2 usage: 0 tokens
3 INFO:root:> [build_index_from_documents] Total embedding\
4 token usage: 0 tokens
5
6 == QUESTION: What programming languages does Mark use?
7
8 INFO:root:> [query] Total LLM token usage: 2210 tokens
9 INFO:root:> [query] Total embedding token usage: 0 tokens
10 ==RESPONSE:
11 Mark uses a variety of programming languages, including H\
12 askell, Ruby, Clojure, JavaScript, Java, Common Lisp, Pyt
13 hon, and Smalltalk.
14
15 ==QUESTION: How many books has Mark written?
16
17 INFO:root:> [query] Total LLM token usage: 2189 tokens
18 INFO:root:> [query]Total embedding token usage: 0 tokens
19 ==RESPONSE:
20 Mark has written 20+ books.
21
22 ==QUESTION: What musical instruments does Markp lay?
23
24 INFO:root:> [query] Total LLM token usage: 2197 tokens
25 INFO:root:> [query] Total embedding token usage: 0 tokens
26 ==RESPONSE:
27 Mark plays guitar, didgeridoo,and American Indian flute.
```

## Zusammenfassung der LlamaIndex/ GPT-Index-Fallstudie

LlamaIndex ist eine Sammlung von Datenstrukturen und Bibliothekscode, die entwickelt wurden, um die Verwendung großer externer Wissensbasen wie Wikipedia zu erleichtern. LlamaIndex erstellt einen vektorisierten Index aus Dokumentendaten, wodurch Abfragen äußerst effizient werden. Es verwendet dann diesen Index, um auf Basis der Abfrage die relevantesten Abschnitte des Dokuments zu identifizieren.

LlamaIndex ist nützlich, weil es eine zentrale Schnittstelle bereitstellt, die deine LLM mit externen Daten verknüpft, und Datenverbindungen zu deinen bestehenden Datenquellen und -formaten (APIs, PDFs, docs, SQL, etc.) bietet. Es ist eine einfache, flexible Schnittstelle zwischen externen Daten und LLMs.

Einige Projekte, die LlamaIndex verwenden, umfassen den Aufbau von persönlichen Assistenten mit LlamaIndex und GPT-3.5, die Verwendung von LlamaIndex für die Dokumentenabfrage und das Zusammenführen von Antworten aus verschiedenen Dokumenten.