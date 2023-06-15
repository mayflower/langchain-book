# Rezepte verfassen mit Large Language Models

Wenn du die ChatGPT-Webanwendung bittest, ein Rezept aus einer Zutatenliste des Users und mit einer Beschreibung zu verfassen, gelingt ihr die Erstellung von Rezepten recht gut. Für das Beispiel in diesem Kapitel nehme ich einen anderen Ansatz:

* die Rezept- und Zutatendateien von meiner Webanwendung http://cookingspace.com zur Erstellung von Text nutzen, basierend auf einer Benutzeranfrage für ein Rezept
* behandle das als Problem der Textvorhersage
* formatiere die Antwort für die Anzeige

Dieser Ansatz hat den Vorteil (für mich!), dass die erstellten Rezepte den Rezepten ähneln, die ich gerne koche, da die Kontextdaten von meinen eigenen Rezeptdateien abgeleitet werden.

## Rezeptdaten vorbereiten

Ich benutze die JSON Rezept-Dateien von meiner Webanwendung http://cookingspace.com. Das folgende Python-Skript konvertiert meine JSON-Daten zu Textbeschreibungen, eine per Datei:

```

```

Hier ist eine Auflistung einer der kürzeren generierten Rezeptdateien (d.h., Text-Rezeptdaten, die aus rohen JSON-Rezeptdaten von meiner Webseite CookingSpace.com konvertiert wurden):

```

```

Ich habe 41 einzelne Rezeptdateien erstellt, die für den Rest dieses Kapitels verwendet werden.

Wenn wir im nächsten Abschnitt ein LLM zum Erstellen eines Rezepts verwenden, sind die Anweisungen nummerierte Schritte und die Formatierung ist anders als bei meinen ursprünglichen Rezeptdateien.

## Ein Vorhersagemodell mit dem OpenAI text-davinci-002 Modell

Hier verwenden wir die **DirectoryLoader** -Klasse, die wir in früheren Beispielen genutzt haben, um einen Embedding Index zu laden und dann zu erstellen.

Hier das Code-Beispiel für das Skript **recipe_generator.py**:

```

```

Das hat zwei Rezepte erzeugt. Hier das Ergebnis für die erste Anfrage:

```


```

Wenn du dir die von mir indizierten Textrezeptdateien anschaust, siehst du, dass das Vorhersagemodell Informationen aus mehreren Trainingsdatenrezepten zusammenführt und gleichzeitig neue Originaltexte für Anleitungen erstellt, die lose auf den von mir geschriebenen Anleitungen und Informationen aus dem OpenAI text-davinci-002-Modell basieren.  

Hier das Ergebnis der zweiten Anfrage:

```


```

## Zusammenfassung der Erstellung von Kochrezepten

Kochen ist eine meiner Lieblingsbeschäftigungen (neben dem Wandern, Kajakfahren und Spielen einer Vielzahl von Musikinstrumenten). Die Webanwendung [CookingSpace.com](http://cookingspace.com/)[^1] habe ich ursprünglich geschrieben, um ein persönliches Bedürfnis zu erfüllen: Aus medizinischen Gründen musste ich meine Vitamin K-Zufuhr genau überwachen und regulieren. Ich verwendete die USDA Nutrition Database der US Regierung, um die Menge von Vitaminen und Nährstoffen in den von mir genutzten Rezepten zu schätzen.

Als ich mit generativen Modellen experimentieren wollte, um Rezepte auf Basis meiner persönlichen Rezeptdaten zu erstellen, war das Experiment einfach aufzusetzen und durchzuführen, weil ich Rezeptdaten aus meinem vorherigen Projekt und Tools wie OpenAI-APIs und LangChain zur Verfügung hatte. Es ist ein durchgängiges Thema in diesem Buch, dass es heutzutage relativ einfach ist, persönliche Projekte auf der Grundlage unserer Daten und Interessen zu erstellen.

[^1] http://cookingspace.com/
