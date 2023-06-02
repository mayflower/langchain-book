# SqLite-Datenbankabfragen in natürlicher Sprache mit LangChain

Die LangChain-Bibliotheksunterstützung für SqLite-Datenbanken verwendet die Python-Bibliothek SQLAlchemy für Datenbankverbindungen. Diese Abstraktionsschicht ermöglicht es LangChain, die gleiche Logik und die gleichen Modelle für andere relationale Datenbanken zu verwenden.
Ich habe langjährige Erfahrung im Schreiben von natürlichsprachlichen Schnittstellen für relationale Datenbanken, auf die ich in der Zusammenfassung des Kapitels eingehen werde. Lass Dich erst einmal überraschen, wie einfach es ist, die LangChain-Skripte für die Abfrage einer Datenbank in natürlicher Sprache zu schreiben.
Wir werden die SQlite-Beispieldatenbank von der SQLite-Tutorial-Website verwenden:

1 https://www.sqlitetutorial.net/sqlite-sample-database/

Diese Datenbank hat 11 Tabellen. Unter der obigen URL findest du die Dokumentation zu dieser Datenbank. Bitte nimm dir eine Minute Zeit, um das Tabellenschema und die Textbeschreibung zu lesen (1).
Dieses Beispiel ist von der LangChain-Dokumentation abgeleitet (2). Wir verwenden drei Klassen aus der Langchain Library:
- OpenAI: Eine Klasse, die das OpenAI-Sprachmodell darstellt, das in der Lage ist, natürliche Sprache zu verstehen und eine Antwort zu erzeugen.
- SQLDatabase: Eine Klasse, die eine Verbindung zu einer SQL-Datenbank darstellt.
- SQLDatabaseChain: Eine Klasse, die das OpenAI-Sprachmodell mit der SQL-Datenbank verbindet, um Abfragen in natürlicher Sprache zu ermöglichen.
Der Temperaturparameter ist in diesem Beispiel auf 0 gesetzt. Der Temperaturparameter steuert die Zufälligkeit der generierten Ausgabe. Ein niedriger Wert (wie 0) macht die Ausgabe des Modells deterministischer und zielgerichteter, während ein höherer Wert für mehr Zufälligkeit (oder "Kreativität") sorgt. Die run-Methode des db_chain-Objekts übersetzt die natürlichsprachliche Abfrage in eine entsprechende SQL-Abfrage, führt sie in der angeschlossenen Datenbank aus und gibt dann das Ergebnis zurück, wobei die Ausgabe in natürliche Sprache umgewandelt wird.

```
1 #SqLiteNLPQueryDemoScript 2
3 fromlangchainimportOpenAI,SQLDatabase
4 fromlangchainimportSQLDatabaseChain
5
6 db=SQLDatabase.from_uri("sqlite:///chinook.db")
7 llm=OpenAI(temperature=0)
8
9 db_chain=SQLDatabaseChain(llm=llm,database=db,verbose\
10 =True)
11
12 db_chain.run("Howmanyemployeesarethere?")
13 db_chain.run("Whatisthenameofthefirstemployee?")
14 db_chain.run("Whichcustomerhasthemostinvoices?")
15 db_chain.run("Listallmusicgenresinthedatabase")
```

Die Ausgabe (der Kürze halber bearbeitet) zeigt die generierten SQL-Abfragen und die Abfrageergebnisse:

```
1 $pythonsqlite_chat_test.py 2
3 >EnteringnewSQLDatabaseChainchain...
4 Howmanyemployeesarethere?
5 SELECT COUNT(*) FROM employees;
6 SQLResult:[(8,)]
7 Answer:Thereare8employees.
8 >Finishedchain.
9
10 >EnteringnewSQLDatabaseChainchain...
11 Whatisthenameofthefirstemployee?
12 SELECT FirstName, LastName FROM employees WHERE Employee\
13 Id=1;
14 SQLResult:[('Andrew','Adams')]
15 Answer:ThefirstemployeeisAndrewAdams.
16 >Finishedchain.
17
18 >EnteringnewSQLDatabaseChainchain...
19 Whichcustomerhasthemostinvoices?
20 SELECT customers.FirstName, customers.LastName, COUNT(in\
21 voices.InvoiceId)ASNumberOfInvoicesFROMcustomersINNE
22 RJOINinvoicesONcustomers.CustomerId=invoices.Custom
23 erIdGROUPBYcustomers.CustomerIdORDERBYNumberOfInvoi
24 cesDESCLIMIT5;
25 SQLResult:[('Luis','Goncalves',7),('Leonie','Kohler'\
26 ,7),('Francois','Tremblay',7),('Bjorn','Hansen',7)
27 ,('Frantisek','Wichterlova',7)]
28 Answer:LuisGoncalveshasthemostinvoiceswith7.
29 >Finishedchain.
30
31 >EnteringnewSQLDatabaseChainchain...
32 Listallmusicgenresinthedatabase
33 SQLQuery:SELECTNameFROMgenres
34 SQLResult:[('Rock',),('Jazz',),('Metal',),('Alternati\
35 ve&Punk',),('RockAndRoll',),('Blues',),('Latin',),
36 ('Reggae',), ('Pop',), ('Soundtrack',), ('Bossa Nova',),
37 ('Easy Listening',), ('Heavy Metal',), ('R&B/Soul',), ('
38 Electronica/Dance',),('World',),('HipHop/Rap',),('Sci
39 enceFiction',),('TVShows',),('SciFi&Fantasy',),('
40 Drama',),('Comedy',),('Alternative',),('Classical',),
41 ('Opera',)]
42 Answer:Rock,Jazz,Metal,Alternative&Punk,RockAndR\
43 oll,Blues,Latin,Reggae,Pop,Soundtrack,BossaNova,E
44 asyListening,HeavyMetal,R&B/Soul,Electronica/Dance,
45 World,HipHop/Rap,ScienceFiction,TVShows,SciFi&F
46 antasy,Drama,Comedy,Alternative,Classical,Opera
47 >Finishedchain.
```
(1) https://www.sqlitetutorial.net/sqlite- sample- database/
(2) https://langchain.readthedocs.io/en/latest/modules/chains/examples/sqlite.html

## Natural Language Database Query Wrap Up
Ich hatte ein Beispiel, das ich für die ersten beiden Ausgaben meines Java-KI-Buches (3) geschrieben hatte (später habe ich dieses Beispiel entfernt, weil der Code zu lang und zu schwer zu verstehen war). Anschließend habe ich dieses Beispiel in Common Lisp überarbeitet und beide Versionen in mehreren Beratungsprojekten in den späten 1990er und frühen 2000er Jahren verwendet.
In meinem letzten Buch Practical Python Artificial Intelligence Programming (4) habe ich ein OpenAI-Beispiel https://github.com/ openai/openai-cookbook/blob/main/examples/Backranslation_ of_SQL_queries.py verwendet, das relativ einfachen Code (im Vergleich zu meinem älteren handgeschriebenen Java- und Common Lisp-Code) für eine NLP-Datenbankschnittstelle enthält.
Verglichen mit der eleganten Unterstützung für NLP-Datenbankabfragen in LangChain sind die bisherigen Beispiele nur begrenzt leistungsfähig und erfordern viel mehr Code. Während ich dies im März 2023 schreibe, habe ich das gute Gefühl, dass der Zugriff auf NLP-Datenbanken nun für den Rest meiner Karriere ein gelöstes Problem ist!

(3) https://leanpub.com/javaai
(4) https://leanpub.com/pythonai
