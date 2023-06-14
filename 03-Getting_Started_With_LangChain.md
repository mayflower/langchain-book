# Getting Started With LangChain

Harrison Chase begann das LangChain Projekt im Oktober 2022. Während ich dieses Buch im Februar 2023 schreibe, hat das GitHub-Repository für LangChain https://github.com/hwchase17/langchain 171 Beitragende.

LangChain[^1] ist ein Framework zur Erstellung von Anwendungen mit großen Sprachmodellen (LLMs) durch Verkettung verschiedener Komponenten. Einige Anwendungen von LangChain sind Chatbots, generative Fragebeantwortung, Zusammenfassungen, datengestützte Generierung und mehr. LangChain kann Zeit bei der Erstellung von Chatbots und anderen Systemen sparen, indem es eine Standardschnittstelle für Chains, Agents und Memory, sowie Integrationsmöglichkeiten mit anderen Tools und End-to-End-Beispielen bietet. Wir beziehen uns auf "Chains" als Sequenzen von Aufrufen (zu einem LLM und verschiedenen Programm-Utilities, Cloud-Services, usw.), die über einen einzigen LLM-API-Aufruf hinausgehen. LangChain bietet eine Standardschnittstelle für Chains, viele Integrationen mit anderen Tools und End-to-End Chains für gängige Anwendungen. Oft findest du bereits existierende Chains, die die Anforderungen deiner Anwendungen erfüllen.

[^1]: https://langchain.readthedocs.io/en/latest/index.html

So kann zum Beispiel eine Chain erstellt werden, die Benutzereingaben entgegennimmt, sie mit einem PromptTemplate formatiert und dann die formatierte Antwort zur Verarbeitung an ein Large Language Model (LLM) weitergibt.

LLMs sind sehr allgemein gehalten, was bedeutet, dass sie zwar viele Aufgaben effektiv ausführen können, aber oft nicht direkt spezifische Antworten auf Fragen oder Aufgaben geben können. Dieses erfordert tiefes Fachwissen oder Expertise. LangChain bietet eine Standardschnittstelle für Agents, eine Bibliothek von Agents aus der man wählen kann, und Beispiele für End-to-End-Agents.

LangChain Memory ist das Konzept, den Zustand zwischen Aufrufen einer Kette oder eines Agenten beizubehalten. LangChain bietet eine standardisierte Schnittstelle für den Speicher, eine Sammlung von Speicherimplementierungen sowie Beispiele für Ketten/Agenten, die den Speicher verwenden[^2]. LangChain bietet eine große Sammlung von allgemeinen Werkzeugen, die du in deiner Anwendung verwenden kannst. Chains gehen über einen einzelnen LLM-Aufruf hinaus und sind Sequenzen von Aufrufen (ob zu einem LLM oder einem anderen Dienstprogramm). LangChain bietet ebenfalls eine Standardschnittstelle für Chains, viele Integrationen mit anderen Werkzeugen sowie End-to-End-Chains für gängige Anwendungen.

LangChain kann mit einem oder mehreren Modellanbietern, Datenspeichern, APIs, etc. integriert werden. Es kann für ausführliche Frage-und-Antwort-Chat-Sitzungen, API-Interaktion oder die Durchführung von Aktionen verwendet werden. Über eine natürlichsprachliche API-Schnittstelle kann LangChain in die Zapier-Plattform integriert werden (wir haben ein ganzes Kapitel den Zapier-Integrationen gewidmet).

## Installation der erforderlichen Pakete

Für die Beispiele in diesem Buch empfiehlt es sich, eine neue Anaconda- oder andere Python-Umgebung zu erstellen und zu installieren:

```shell
1    pip install langchain llama_index openai
2    pip install kor pydrive pandas rdflib
3    pip install google-search-results SPARQLWrapper
```

Für den Rest dieses Kapitels werden wir das Unterverzeichnis **langchain_- getting_started** und im nächsten Kapitel **llama-index_case_-study** im GitHub-Repository für dieses Buch verwenden.

## Ein neues LangChain-Projekt anlegen

Einfache LangChain-Projekte bestehen oft nur aus einer einfachen Python-Skriptdatei. Wenn dir beim Lesen dieses Buches ein Beispiel interessant oder nützlich erscheint, schlage ich vor, die requirements.txt und die Python-Quelldateien in ein neues Verzeichnis zu kopieren und dein eigenes privates GitHub-Repository anzulegen, in dem du arbeiten kannst. Bitte nutze die Beispiele in diesem Buch als "deinen Code", d.h. verwende frei jeden Code oder jede Idee, die du hier findest.

## Grundlegende Anwendung und Beispiele

Während ich versuche, das Material in diesem Buch so zu gestalten, dass du es unabhängig und ohne externe Referenzen genießen kannst, solltest du auch die ausgezeichnete [Dokumentation](https://python.langchain.com/en/latest/getting_started/getting_started.html) und die einzelnen detaillierten Anleitungen für Prompts, Chat, document loading, Indizes usw. nutzen.

Während wir einige Beispiele durchgehen, beachte bitte, wie die ChatGPT-Webanwendung arbeitet: Du gibst Text ein und erhältst Antworten. Die Art und Weise, wie du ChatGPT aufforderst, ist offensichtlich wichtig, wenn du nützliche Antworten erhalten möchtest. In Code-Beispielen automatisieren und formalisieren wir diesen manuellen Prozess.

Du musst ein LLM auswählen, das du verwenden möchtest. In der Regel wählen wir die GPT-3.5-API von OpenAI, da sie universell einsetzbar und viel kostengünstiger ist als die früheren Modell-APIs von OpenAI. Du musst dich für einen API-Schlüssel anmelden[^2] und diesen als Umgebungsvariable festlegen:

```shell
1    export OPENAI_API_KEY="YOUR KEY GOES HERE"
```

Sowohl die Bibliotheken **openai** als auch **langchain** werden nach dieser Umgebungsvariablen suchen und diese verwenden. Wir werden uns ein paar einfache Beispiele in einer Python-REPL ansehen. Wir beginnen mit der Verwendung der Textvorhersage-API von OpenAI:

[^2]: https://platform.openai.com/account/api-keys

```shell
1    $python
2    >>> from langchain.llms import OpenAI
3    >>> llm = OpenAI(temperature=0.8)
4    >>> s = llm("John got into his new sportscar, and he dro\
5    ve it")
6    >>> s
7    'to work\n\nJohn started up his new sportscar and drove\
8    it to work. He had a huge smile on his face as he drove,
9    excited to show off his new car to his colleagues. The w\
10    ind blowing through his hair, and the sun on his skin, he
11    felt a sense of freedom and joy as he cruised along the
12    road. He arrived at work in no time, feeling refreshed an\
13    d energized.'
14    >>> s = llm("John got into his new sportscar, and he dro\
15    ve it")
16    >>> s
17    "around town\n\nJohn drove his new sportscar around tow\
18    n, enjoying the feeling of the wind in his hair. He stopp\
19    ed to admire the view froma scenic lookout, and then spe\
20    d off to the mall to do some shopping. On the way home, h\
21    e took a detour down a winding country road, admiring the
22    scenery and enjoying the feel of the car's powerful engi\
23    ne. By the time he arrived back home, he had a huge smile
24    on his face."
```

Beachte, wie wir bei zweifacher Ausführung des gleichen Eingabetextes unterschiedliche Ergebnisse erhalten. Durch das Erhöhen der Temperatur in Zeile 3 wird die Zufälligkeit erhöht.

Unser nächstes Beispiel befindet sich in der Quelldatei **directions_template.py** und verwendet die Klasse **PromptTemplate**. Eine Prompt-Vorlage ist eine reproduzierbare Methode zur Generierung einer Eingabeaufforderung. Es enthält einen Textstring ("die Vorlage"), der eine Reihe von Parametern des Endbenutzers entgegennehmen und einen Prompt erzeugen kann. Die Prompt-Vorlage kann Anweisungen für das Sprachmodell, Beispiele zur Verbesserung der Antwort des Modells oder spezifische Fragen enthalten, die das Modell beantworten soll.

```python
1    from langchain.prompts import PromptTemplate
2    from langchain.llms import OpenAI
3    llm = OpenAI(temperature=0.9)
4
5    def get_directions(thing_to_do):
6        prompt = PromptTemplate(
7            input_variables=["thing_to_do"],
8            template="How do I {thing_to_do}?",
9        )
10       prompt_text = prompt.format(thing_to_do=thing_to_do)
11       print(f"\n{prompt_text}:")
12       return llm(prompt_text)
13   
14    print(get_directions("get to the store"))
15    print(get_directions("hang a picture on the wall"))
```

Man könnte einfach Python-Code zur Manipulation von Zeichenketten schreiben, um eine Eingabeaufforderung zu erstellen, aber die Verwendung der Utility-Klasse **PromptTemplate** ist besser lesbar und funktioniert mit einer beliebigen Anzahl von Eingabevariablen.

Das Ergebnis ist:

```shell
1    $python directions_template.py
2
3    How do I get to the store?:
4
5    To get to the store, you will need to use a mode of trans\
6    portation such as walking, driving, biking, or taking pub\
7    lic transportation. Depending on the location of the stor\
8    e, you may need to look up directions or maps to determin\
9    e the best route to take.
10
11    How do I hang a picture on the wall?:
12
13    1. Find a stud in the wall, or use two or three wall anch\
14    ors for heavier pictures.
15    2. Measure and mark the wall where the picture hanger wil\
16    l go.
17    3.Pre-drill the holes and place wall anchors if needed.
18    4.Hammer the picture hanger into the holes.
19    5.Hang the picture on the picture hanger.
```

Das nächste Beispiel in der Datei **country_information.py** ist von einem Beispiel in der LangChain-Dokumentation abgeleitet. In diesem Beispiel verwenden wir die **PromptTemplate**, welche das gewünschte Muster enthält, um dem LLM zu ermöglichen, eine Antwort zu generieren.

```python
1    from langchain.prompts import PromptTemplate
2    from langchain.llms import OpenAI
3    llm = OpenAI(temperature=0.9)
4
5    def get_country_information(country_name):
6        print(f"\nProcessing {country_name}:")
7        global prompt
8        if "prompt" not in globals():
9            print("Creating prompt...")
10           prompt = PromptTemplate(
11              input_variables=["country_name"],
12              template = """
13    Predict the capital and population of a country.
14
15    Country:{country_name}
16    Capital: Population:""",
17            )
18        prompt_text = prompt.format(country_name=country_name)
19        print(prompt_text)
20        return llm(prompt_text)
21
22    print(get_country_information("Canada"))
23    print(get_country_information("Germany"))
```

Du kannst die ChatGPT-Weboberfläche verwenden, um mit Prompts zu experimentieren. Wenn du ein Muster gefunden hast, das gut funktioniert, schreibe es in ein Python-Skript wie im letzten Beispiel, ändere aber die Daten, die du in der **PromptTemplate**-Instanz angibst.

Die Ausgabe des letzten Beispiels ist:

```shell
1    $ python country_information.py
2
3    Processing Canada:
4    Creating prompt...
5
6    Predict the capital and population of a country.
7
8    Country: Canada
9    Capital:
10   Population:
11
12
13    Capital: Ottawa
14    Population: 37.058.856 (as of July 2020)
15
16    Processing Germany:
17
18    Predict the capital and population of a country.
19
20    Country: Germany
21    Capital:
22    Population:
23
24
25    Capital: Berlin
26    Population: 83,02 million (est.2019)
```

## Embeddings erstellen

Als Referenz hier die LangChain Embeddings Dokumentation[^3]. Mit einer Python REPL können wir verstehen, wie Text- zu Vektorraum-Einbettungen aussehen könnten:

[^3]: https://langchain.readthedocs.io/en/latest/modules/indexes/examples/embeddings.html

```shell
1  $ python
2  Python 3.10.8 (main, Nov 24 2022, 08:08:27) [Clang 14.0.6\
3   ] on darwin
4  Type "help", "copyright", "credits" or "license" for more\
5   information.
6  >>> from langchain.embeddings import OpenAIEmbeddings
7  >>> embeddings = OpenAIEmbeddings()
8  >>> text = "Mary has blond hair and John has brown hair. \
9  Mary lives in town and John lives in the country."
10 >>> doc_embeddings = embeddings.embed_documents([text])
11 >>> doc_embeddings
12 [[0.007727328687906265, 0.0009025644976645708, -0.0033224\
13 383369088173, -0.01794492080807686, -0.017969949170947075
14 , 0.028506645932793617, -0.013414892368018627, 0.00466768
15 16418766975, -0.0024965214543044567, -0.02662956342101097
16 ,
17 ...]]
18 >>> query_embedding = embeddings.embed_query("Does John l\
19 ive in the city?")
20 >>> query_embedding
21 [0.028048301115632057, 0.011499025858938694, -0.009440079\
22 33139801, -0.020809611305594444, -0.023904507979750633, 0
23 .018750663846731186, -0.01626438833773136, 0.018129095435
24 142517,
25 ...]
26 >>>
```

[^3]: https://langchain.readthedocs.io/en/latest/modules/indexes/examples/embeddings.html

Beachte, dass das **doc_embeddings** eine Liste ist, bei der jedes Listenelement das Embedding für ein einzugebendes Textdokument ist.

Das **query_embedding** ist ein einzelnes Embedding. Lies dir bitte die oben verlinkte Dokumentation zu Embeddings durch. 

Wir werden Vektor-Speicher verwenden, um berechnete Embeddings für zukünftige Verwendungszwecke zu speichern. Im nächsten Kapitel werden wir ein Beispiel einer Dokumentendatenbank-Suche mit LangChain und Llama-Index betrachten. 

## Verwendung von LangChain-Vektor-Stores zum Durchsuchen von Dokumenten

Wir verweisen auf die Dokumentation von LangChain Vector Stores (4). Du musst dafür ein paar Bibliotheken installieren:

```
1 pipinstallchroma
2 pipinstallchromadb
3 pipinstallunstructured
```

Das Beispielskript ist **doc_search.py**:

```
1 from langchain.text_splitter import CharacterTextSplitter
2 from langchain.vectorstores import Chroma
3 from langchain.embeddings import OpenAIEmbeddings
4 from langchain.document_loaders import DirectoryLoader
5 from langchain import OpenAI, VectorDBQA
6
7 embeddings = OpenAIEmbeddings() 8
9 loader=DirectoryLoader('../data/', glob="**/*.txt")
10 documents = loader.load()
11 text_splitter = CharacterTextSplitter(chunk_size=2500, ch\
12 unk_overlap=0)
13
14 texts = text_splitter.split_documents(documents)
15
16 docsearch = Chroma.from_documents(texts, embeddings)
17
18 qa = VectorDBQA.from_chain_type(llm=OpenAI(),
19                                 chain_type="stuff",
20                                 vectorstore=docsearch)
21
22 def query(q):
23     print(f"Query: {q}")
24     print(f"Answer: {qa.run(q)}")
25
26 query("What kinds of equipment are in a chemistry laborat\
27 ory?")
28 query("What is Austrian School of Economics?")
29 query("Why do people engage in sports?")
30 query("What is the effect of bodychemistry on exercise?")
```

Die Klasse DirectoryLoader ist nützlich, um ein Verzeichnis voller Eingabedokumente zu laden. In diesem Beispiel haben wir festgelegt, dass wir nur Textdateien verarbeiten wollen, aber das Muster für den Dateiabgleich hätte auch PDF-Dateien usw. enthalten können.
Das Ergebnis ist:

```
1 $ python doc_search.py
2 Created a chunk of size 1055, which is longer than the sp\
3 ecified 1000
4 Running Chroma using direct local API.
5 Using DuckDB in-memory for database. Data will be transie\
6 nt.
7 Query: What kinds of equipment are in a chemistry laborat\
8 ory?
9 Answer: A chemistry lab would typically include glasswar\
10 e, such as beakers, flasks, and testtubes, as well as ot
11 her equipment such as scales, Bunsenburners, and thermom
12 eters.
13 Query: What is Austrian School of Economics?
14 Answer: The Austrian School is a school of economic thou\
15 ght that emphasizes the spontaneous organizing power of t
16 he price mechanism. Austrians hold that the complexity of
17 subjective human choices makes mathematical modelling of
18 the evolving market extremely difficult and advocate a "
19 laissezfaire" approach to the economy. Austrian School e
20 conomists advocate the strict enforcement of voluntary co
21 ntractual agreements between economic agents, and hold th
22 at commercial transactions should be subject to the small
23 est possible imposition of forces they consider to be (in
24 particular the smallest possible amount of government in
25 tervention). The Austrian School derives its name from it
26 s predominantly Austrian founders and early supporters, i
27 ncluding Carl Menger, Eugen von Bohm-Bawerk and Ludwig vo
28 n Mises.
29 Query: Why do people engage in sports?
30 Answer: People engage in sports for leisure and entertai\
31 nment, as well as for physical exercise and athleticism.
32 Query: What is the effect of bodychemistry on exercise?
33 Answer: Body chemistry can affect the body's response to\
34 exercise, as certain hormones and enzymes produced by th
35 e body can affect the energy levels and muscleperformanc
36 e. Chemicals in the body, such as adenosinetriphosphate
37 (ATP) and urea, can affect the body's energy production a
38 nd muscle metabolism during exercise. Additionally,the b
39 ody's levels of electrolytes, vitamins, and minerals can
40 affect exercise performance.
41 Exiting: Cleaning up .chroma directory
```

## Verwendung von LangChain-Vektor-Stores zum Durchsuchen von Dokumenten

Wir verweisen auf die Dokumentation von LangChain Vector Stores (4). Du musst dafür ein paar Bibliotheken installieren:

```
1 pipinstallchroma
2 pipinstallchromadb
3 pipinstallunstructured
```

Das Beispielskript ist **doc_search.py**:

```
1 from langchain.text_splitter import CharacterTextSplitter
2 from langchain.vectorstores import Chroma
3 from langchain.embeddings import OpenAIEmbeddings
4 from langchain.document_loaders import DirectoryLoader
5 from langchain import OpenAI, VectorDBQA
6
7 embeddings = OpenAIEmbeddings() 8
9 loader=DirectoryLoader('../data/', glob="**/*.txt")
10 documents = loader.load()
11 text_splitter = CharacterTextSplitter(chunk_size=2500, ch\
12 unk_overlap=0)
13
14 texts = text_splitter.split_documents(documents)
15
16 docsearch = Chroma.from_documents(texts, embeddings)
17
18 qa = VectorDBQA.from_chain_type(llm=OpenAI(),
19                                 chain_type="stuff",
20                                 vectorstore=docsearch)
21
22 def query(q):
23     print(f"Query: {q}")
24     print(f"Answer: {qa.run(q)}")
25
26 query("What kinds of equipment are in a chemistry laborat\
27 ory?")
28 query("What is Austrian School of Economics?")
29 query("Why do people engage in sports?")
30 query("What is the effect of bodychemistry on exercise?")
```

Die Klasse DirectoryLoader ist nützlich, um ein Verzeichnis voller Eingabedokumente zu laden. In diesem Beispiel haben wir festgelegt, dass wir nur Textdateien verarbeiten wollen, aber das Muster für den Dateiabgleich hätte auch PDF-Dateien usw. enthalten können.
Das Ergebnis ist:

```
1 $ python doc_search.py
2 Created a chunk of size 1055, which is longer than the sp\
3 ecified 1000
4 Running Chroma using direct local API.
5 Using DuckDB in-memory for database. Data will be transie\
6 nt.
7 Query: What kinds of equipment are in a chemistry laborat\
8 ory?
9 Answer: A chemistry lab would typically include glasswar\
10 e, such as beakers, flasks, and testtubes, as well as ot
11 her equipment such as scales, Bunsenburners, and thermom
12 eters.
13 Query: What is Austrian School of Economics?
14 Answer: The Austrian School is a school of economic thou\
15 ght that emphasizes the spontaneous organizing power of t
16 he price mechanism. Austrians hold that the complexity of
17 subjective human choices makes mathematical modelling of
18 the evolving market extremely difficult and advocate a "
19 laissezfaire" approach to the economy. Austrian School e
20 conomists advocate the strict enforcement of voluntary co
21 ntractual agreements between economic agents, and hold th
22 at commercial transactions should be subject to the small
23 est possible imposition of forces they consider to be (in
24 particular the smallest possible amount of government in
25 tervention). The Austrian School derives its name from it
26 s predominantly Austrian founders and early supporters, i
27 ncluding Carl Menger, Eugen von Bohm-Bawerk and Ludwig vo
28 n Mises.
29 Query: Why do people engage in sports?
30 Answer: People engage in sports for leisure and entertai\
31 nment, as well as for physical exercise and athleticism.
32 Query: What is the effect of bodychemistry on exercise?
33 Answer: Body chemistry can affect the body's response to\
34 exercise, as certain hormones and enzymes produced by th
35 e body can affect the energy levels and muscleperformanc
36 e. Chemicals in the body, such as adenosinetriphosphate
37 (ATP) and urea, can affect the body's energy production a
38 nd muscle metabolism during exercise. Additionally,the b
39 ody's levels of electrolytes, vitamins, and minerals can
40 affect exercise performance.
41 Exiting: Cleaning up .chroma directory
```

## Zusammenfassung LangChain 

Für den Rest dieses Buches werden wir LangChain verwenden, genauso wie die LlamaIndex-Bibliothek, die wir im nächsten Kapitel vorstellen.
Ich behandle in diesem Buch nur die Teilmenge von LangChain, die ich in meinen eigenen Projekten verwende. Lies unbedingt auch die LangChain-Dokumentation und schau dir die LangChain-Chains an, die Benutzer auf
[Langchain-hub](https://github.com/hwchase17/langchain-hub)⁵ veröffentlicht haben.

(5) https://github.com/hwchase17/langchain-hub
