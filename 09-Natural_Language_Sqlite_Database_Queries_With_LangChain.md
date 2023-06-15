# SqLite-Datenbankabfragen in natürlicher Sprache mit LangChain

Die LangChain-Bibliotheksunterstützung für SqLite-Datenbanken verwendet die Python-Bibliothek SQLAlchemy für Datenbankverbindungen. Diese Abstraktionsschicht ermöglicht es LangChain, die gleiche Logik und die gleichen Modelle für andere relationale Datenbanken zu verwenden.
Ich habe langjährige Erfahrung im Schreiben von Schnittstellen für relationale Datenbanken in natürlicher Sprache, auf die ich in der Zusammenfassung des Kapitels eingehen werde. Lass Dich erst einmal überraschen, wie einfach es ist, die LangChain-Skripte für die Abfrage einer Datenbank in natürlicher Sprache zu schreiben.
Wir werden die SQlite-Beispieldatenbank von der SQLite-Tutorial-Webseite verwenden:

´´´
1 https://www.sqlitetutorial.net/sqlite-sample-database/
´´´

Diese Datenbank hat 11 Tabellen. Unter der obigen URL findest du die Dokumentation zu dieser Datenbank. Bitte nimm dir eine Minute Zeit und betrachte das [Diagramm des Tabellenschemas und die Textbeschreibung](/)[^1].
Dieses Beispiel ist von der [LangChain-Dokumentation](https://langchain.readthedocs.io/en/latest/modules/chains/examples/sqlite.html)[^2] abgeleitet. Wir verwenden drei Klassen aus der Langchain-Bibliothek:

- OpenAI: Eine Klasse, die das OpenAI-Sprachmodell enthält, welches natürliche Sprache verstehen und eine Antwort erzeugen kann.
- SQLDatabase: Eine Klasse, die eine Verbindung zu einer SQL-Datenbank enthält.
- SQLDatabaseChain: Eine Klasse, die das OpenAI-Sprachmodell mit der SQL-Datenbank verbindet, um Abfragen in natürlicher Sprache zu ermöglichen.

[^1]https://www.sqlitetutorial.net/sqlite-sample-database
[^2]ttps://langchain.readthedocs.io/en/latest/modules/chains/examples/sqlite.html

Der Temperaturparameter ist in diesem Beispiel auf 0 gesetzt. Der Temperaturparameter steuert die Zufälligkeit der generierten Ausgabe. Ein niedriger Wert (wie 0) macht die Ausgabe des Modells deterministischer und zielgerichteter, während ein höherer Wert für mehr Zufälligkeit (oder "Kreativität") sorgt. Die Methode run des db_chain-Objekts übersetzt die in natürlicher Sprache geschriebene Abfrage in eine entsprechende SQL-Abfrage, führt sie in der verknüpften Datenbank aus und gibt dann das Ergebnis - in natürliche Sprache umgewandelt - zurück.

```py
1 #SqLiteNLPQueryDemoScript 2
3 from langchain import OpenAI,SQLDatabase
4 from langchain import SQLDatabaseChain
5
6 db=SQLDatabase.from_uri("sqlite:///chinook.db")
7 llm=OpenAI(temperature=0)
8
9 db_chain=SQLDatabaseChain(llm=llm,database=db,
10                          verbose=True)
11
12 db_chain.run("Howmanyemployeesarethere?")
13 db_chain.run("Whatisthenameofthefirstemployee?")
14 db_chain.run("Whichcustomerhasthemostinvoices?")
15 db_chain.run("Listallmusicgenresinthedatabase")
```

Die Ausgabe (gekürzt) zeigt die generierten SQL-Abfragen und die Abfrageergebnisse:

```
1 $ python sqlite_chat_test.py
2
3 > Entering new SQLDatabaseChain chain...
4 How many employees are there?
5 SELECT COUNT(*) FROM employees;
6 SQLResult: [(8,)]
7 Answer: There are 8 employees.
8 > Finished chain.
9
10 > Entering new SQLDatabaseChain chain...
11 What is the name of the first employee?
12 SELECT FirstName, LastName FROM employees WHERE Employee\
13 Id = 1;
14 SQLResult: [('Andrew', 'Adams')]
15 Answer: The first employee is Andrew Adams.
16 > Finished chain.
17
18 > Entering new SQLDatabaseChain chain...
19 Which customer has the most invoices?
20 SELECT customers.FirstName, customers.LastName, COUNT(in\
21 voices.InvoiceId) AS NumberOfInvoices FROM customers INNE
22 R JOIN invoices ON customers.CustomerId = invoices.Custom
23 erId GROUP BY customers.CustomerId ORDER BY NumberOfInvoi
24 ces DESC LIMIT 5;
25 SQLResult: [('Luis', 'Goncalves', 7), ('Leonie', 'Kohler'\
26 , 7), ('Francois', 'Tremblay', 7), ('Bjorn', 'Hansen', 7)
27 , ('Frantisek', 'Wichterlova', 7)]
28 Answer: Luis Goncalves has the most invoices with 7.
29 > Finished chain.
30
31 > Entering new SQLDatabaseChain chain...
32 List all music genres in the database
33 SQLQuery: SELECT Name FROM genres
34 SQLResult: [('Rock',), ('Jazz',), ('Metal',), ('Alternati\
35 ve & Punk',), ('Rock And Roll',), ('Blues',), ('Latin',),
36 ('Reggae',), ('Pop',), ('Soundtrack',), ('Bossa Nova',),
37 ('Easy Listening',), ('Heavy Metal',), ('R&B/Soul',), ('
38 Electronica/Dance',), ('World',), ('Hip Hop/Rap',), ('Sci
39 ence Fiction',), ('TV Shows',), ('Sci Fi & Fantasy',), ('
40 Drama',), ('Comedy',), ('Alternative',), ('Classical',),
41 ('Opera',)]
42 Answer: Rock, Jazz, Metal, Alternative & Punk, Rock And R\
43 oll, Blues, Latin, Reggae, Pop, Soundtrack, Bossa Nova, E
44 asy Listening, Heavy Metal, R&B/Soul, Electronica/Dance,
45 World, Hip Hop/Rap, Science Fiction, TV Shows, Sci Fi & F
46 antasy, Drama, Comedy, Alternative, Classical, Opera
47 > Finished chain.
```

## Zusammenfassung Datenbankabfrage in natürlicher Sprache
Ich hatte ein Beispiel, das ich für die ersten beiden Ausgaben meines [Java-KI-Buches](https://leanpub.com/javaai)[^3] geschrieben hatte (später habe ich dieses Beispiel entfernt, weil der Code zu lang und zu schwer zu verstehen war). Dieses Beispiel habe ich dann in Common Lisp überarbeitet und beide Versionen in mehreren Consulting-Projekten in den späten 1990er und frühen 2000er Jahren verwendet.
In meinem letzten Buch [Practical Python Artificial Intelligence Programming](https://leanpub.com/pythonai)[^4] habe ich ein OpenAI-Beispiel https://github.com/openai/openai-cookbook/blob/main/examples/Backtranslation_of_SQL_queries.py verwendet, das relativ einfachen Code (im Vergleich zu meinem älteren handgeschriebenen Java- und Common Lisp-Code) für eine NLP-Datenbankschnittstelle enthält.
Verglichen mit dem eleganten Support für NLP-Datenbankabfragen in LangChain sind die vorherigen Beispiele nur begrenzt leistungsfähig und erfordern viel mehr Code. Beim Schreiben im März 2023 habe ich das gute Gefühl, dass der Zugriff auf NLP-Datenbanken nun für den Rest meines Berufslebens kein Problem mehr ist!

[^3]https://leanpub.com/javaai
[^4]https://leanpub.com/pythonai
