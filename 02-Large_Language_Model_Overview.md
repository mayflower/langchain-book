# Übersicht über Large Language Models 

Large Language Models[^1] (LLM) sind eine Untermenge der künstlichen Intelligenz, die Deep Learning und neuronale Netzwerke zur Verarbeitung natürlicher Sprache einsetzt. Transformers[^2] stellen eine spezielle Art von neuronaler Netzwerkarchitektur dar, die mithilfe von selbstbeobachtenden Mechanismen Kontext in sequenziellen Daten erlernen können. Sie wurden im Jahr 2017 von einem Team bei Google Brain eingeführt und haben seitdem Beliebtheit bei der Erforschung von LLM erlangt. Einige Beispiele von transformerbasierten[^3] LLMs sind BERT, GPT-3, T5 und Megatron-LM[^4].

Die Hauptpunkte, die wir in diesem Buch behandeln wollen, sind:

-	LLMs sind Deep Learning Algorithmen die auf Basis massiver Datenmengen natürliche Sprache verstehen und generieren können.
-	LLMs nutzen Techniken wie Selbstaufmerksamkeit, Maskierung und Feinabstimmung, um komplexe Muster und Zusammenhänge in der Sprache zu erlernen. LLMs auf Grundlage von Transformern können die natürliche Sprache verstehen und generieren. Diese Modelle nutzen neuronale Netzwerkarchitekturen, die sequenzielle Daten wie Text mithilfe von Aufmerksamkeitsmechanismen verarbeiten können. Aufmerksamkeitsmechanismen erlauben dem Modell, die wichtigen Teile von Ein- und Ausgabe in den Fokus zu nehmen und gleichzeitig die unwichtigen zu ignorieren.
-	LLMs können verschiedene Aufgaben der natürlichen Sprachverarbeitung (Natural Language Processing - NLP) und natürlichen Spracherzeugung (Natural Language Generation – NLG) wie Zusammenfassung, Übersetzung, Vorhersage, Klassifikation und Fragenbeantwortung ausführen.
-	Auch wenn LLMs ursprünglich für Anwendungen des NLP entwickelt wurden, haben sie doch auch ihr Potential in anderen Bereichen wie computerbasiertes Sehen und Bioinformatik gezeigt, indem sie ihr verallgemeinerbares Wissen und ihre Fähigkeit zum Transferlernen nutzbar gemacht haben.

BERT-Modelle[^5] waren unter den ersten Transformer-Modellen, die breite Nutzung gefunden haben. BERT wurde von Google AI Language im Jahr 2018 entwickelt. BERT-Modelle stellen eine Gruppe maskierter Sprachmodelle dar, die Transformer-Architektur benutzen, um bidirektionale Repräsentationen natürlicher Sprache zu erlernen. BERT-Modelle können die Bedeutung mehrdeutiger Worte verstehen, indem sie den umgebenden Text als Kontext benutzen. Der *Zaubertrick* besteht darin, dass die Trainingsdaten praktisch kostenlos mitgeliefert werden. Man ersetzt ein fehlendes Wort-Token und trainiert das Modell darauf, die fehlenden Wörter vorherzusagen. Dieser Vorgang wird mit riesigen Mengen an Trainingsdaten aus dem Internet, Büchern und anderen Quellen wiederholt.

Hier sind einige "Papers with Code"-Links für BERT (Links sind für Code, Paper-Links in den Code-Repositories):

- https://github.com/allenai/scibert
- https://github.com/google-research/bert

[^1]: https://blogs.nvidia.com/blog/2022/10/10/llms-ai-horizon/
[^2]: https://www.linkedin.com/pulse/chatgpt-tip-iceberg-paul-golding
[^3]: https://factored.ai/transformer-based-language-models/
[^4]: https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)
[^5]: https://en.wikipedia.org/wiki/BERT_(Language_model)

## Big Tech Businesses vs. Small Startups nutzen Large Language Models

Sowohl Microsoft als auch Google bespielen beide Seiten: Sie wollen Cloud-LLM-Dienste sowohl an Entwickler und kleine Startup-Unternehmen verkaufen als auch einen Lock-in für ihre Dienste wie Office 365, Google Docs und Sheets usw. erreichen.
Microsoft hat im Rahmen seiner laufenden Partnerschaft mit OpenAI, dem Unternehmen hinter ChatGPT, KI-Technologie in E-Mails, Diashows und Tabellenkalkulationen am Arbeitsplatz integriert. 

> *REVIEW: Microsofts Azure OpenAI Service bietet ein leistungsfähiges Werkzeug, um diese Ergebnisse zu ermöglichen, wenn es mit seinem Data Lake von mehr als zwei Milliarden Metadaten und Transaktionselementen genutzt wird.*

Während ich dies schreibe, hat Google gerade eine öffentliche Warteliste für seinen Bard AI/Chat-Suchdienst geöffnet. Ich verwende seit Jahren verschiedene Google-APIs in meinem eigenen Code. Ich habe keine Favoriten im Wettstreit der Tech-Giganten, sondern bin vor allem daran interessiert, das ich das was sie entwickeln in meinen eigenen Projekten verwenden kann.

Hugging Face, das KI-Produkte entwickelt und die von anderen Unternehmen entwickelten Produkte hostet, arbeitet an Open-Source-Konkurrenten zu ChatGPT und wird dafür ebenfalls AWS (6) nutzen. Cohere AI, Anthropic, Hugging Face und Stability AI sind einige der Startups, die OpenAI und Hugging Face APIs für ihre Entwicklungen nutzen. Während ich dieses Kapitel schreibe, sehe ich Hugging Face als eine großartige Quelle für spezialisierte Modelle. Ich finde es toll, dass die Modelle von Hugging Face sowohl über ihre APIs als auch selbst gehostet auf unseren eigenen Servern und manchmal sogar auf den eigenen Laptops ausgeführt werden können. Hugging Face ist eine fantastische Resource, und auch wenn ich ihre Modelle in diesem Buch viel seltener verwende als OpenAI APIs, sollten Sie die Hosting- und Open-Source-Flexibilität von Hugging Face in Anspruch nehmen. In diesem Buch verwende ich OpenAI APIs, weil ich möchte, dass Sie sich schnell orientieren und Ihre eigenen Projekte erstellen können.

Lieber Leser, ich habe dieses Buch nicht für Entwickler geschrieben, die in etablierten KI-Firmen arbeiten (obwohl ich hoffe, dass diese Leute das vorliegende Material nützlich finden!). Ich habe dieses Buch für kleine Entwickler geschrieben, die ihr eigenes Interesse daran haben, Werkzeuge zu schreiben, die ihnen Zeit einsparen. Ich habe dieses Buch auch in der Hoffnung geschrieben, dass es Entwicklern helfen wird, in die von ihnen entworfenen und geschriebenen Programme Funktionen einzubauen, die es mit den Lösungen der großen Technologieunternehmen aufnehmen können.

(6) https://iblnews.org/aws-partners-with-hugging-face-an-ai-startup-rival-to-chatgpt-working-on-open-source-models/
