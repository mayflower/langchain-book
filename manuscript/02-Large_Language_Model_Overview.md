# Übersicht über Large Language Models 

[Large Language Models](https://blogs.nvidia.com/blog/2022/10/10/llms-ai-horizon/)[^1] (LLM) sind eine Untermenge der künstlichen Intelligenz, die Deep Learning und neuronale Netzwerke zur Verarbeitung natürlicher Sprache einsetzt. [Transformers](https://www.linkedin.com/pulse/chatgpt-tip-iceberg-paul-golding)[^2] stellen eine spezielle Art von neuronaler Netzwerkarchitektur dar, die mithilfe von selbstbeobachtenden Mechanismen Kontext in sequenziellen Daten erlernen können. Sie wurden im Jahr 2017 von einem Team bei Google Brain eingeführt und haben seitdem Beliebtheit bei der Erforschung von LLM erlangt. Einige Beispiele von [transformerbasierten](https://factored.ai/transformer-based-language-models/)[^3] LLMs sind [BERT, GPT-3, T5 und Megatron-LM](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))[^4].

Die Hauptpunkte, die wir in diesem Buch behandeln wollen, sind:

-	LLMs sind Deep Learning Algorithmen die auf Basis massiver Datenmengen natürliche Sprache verstehen und generieren können.
-	LLMs nutzen Techniken wie Selbstaufmerksamkeit, Maskierung und Feinabstimmung, um komplexe Muster und Zusammenhänge in der Sprache zu erlernen. LLMs auf Grundlage von Transformern können die natürliche Sprache verstehen und generieren. Diese Modelle nutzen neuronale Netzwerkarchitekturen, die sequenzielle Daten wie Text mithilfe von Aufmerksamkeitsmechanismen verarbeiten können. Aufmerksamkeitsmechanismen erlauben dem Modell, die wichtigen Teile von Ein- und Ausgabe in den Fokus zu nehmen und gleichzeitig die unwichtigen zu ignorieren.
-	LLMs können verschiedene Aufgaben der natürlichen Sprachverarbeitung (Natural Language Processing - NLP) und natürlichen Spracherzeugung (Natural Language Generation – NLG) wie Zusammenfassung, Übersetzung, Vorhersage, Klassifikation und Fragenbeantwortung ausführen.
-	Auch wenn LLMs ursprünglich für Anwendungen des NLP entwickelt wurden, haben sie doch auch ihr Potential in anderen Bereichen wie computerbasiertes Sehen und Bioinformatik gezeigt, indem sie ihr verallgemeinerbares Wissen und ihre Fähigkeit zum Transferlernen nutzbar gemacht haben.

[BERT-Modelle](https://en.wikipedia.org/wiki/BERT_(Language_model))[^5] waren unter den ersten Transformer-Modellen, die breite Nutzung gefunden haben. BERT wurde von Google AI Language im Jahr 2018 entwickelt. BERT-Modelle stellen eine Gruppe maskierter Sprachmodelle dar, die Transformer-Architektur benutzen, um bidirektionale Repräsentationen natürlicher Sprache zu erlernen. BERT-Modelle können die Bedeutung mehrdeutiger Worte verstehen, indem sie den umgebenden Text als Kontext benutzen. Der *Zaubertrick* besteht darin, dass die Trainingsdaten praktisch kostenlos mitgeliefert werden. Man ersetzt ein fehlendes Wort-Token und trainiert das Modell darauf, die fehlenden Wörter vorherzusagen. Dieser Vorgang wird mit riesigen Mengen an Trainingsdaten aus dem Internet, Büchern und anderen Quellen wiederholt.

Hier sind einige "Papers with Code"-Links für BERT (Links sind für Code, Paper-Links in den Code-Repositories):

- https://github.com/allenai/scibert
- https://github.com/google-research/bert

[^1]: https://blogs.nvidia.com/blog/2022/10/10/llms-ai-horizon/
[^2]: https://www.linkedin.com/pulse/chatgpt-tip-iceberg-paul-golding
[^3]: https://factored.ai/transformer-based-language-models/
[^4]: https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)
[^5]: https://en.wikipedia.org/wiki/BERT_(Language_model)

## Big Tech Businesses vs. Small Startups bei der Verwendung von Large Language Models

Sowohl Microsoft als auch Google haben Interessen auf beiden Seiten: Einerseits möchten sie Cloud-LLM-Dienste an Entwickler und kleine Start-up-Unternehmen verkaufen. Andererseits streben sie danach, ihre Dienste wie Office 365, Google Docs, Sheets usw. zu etablieren und die Nutzer an diese zu binden.

Microsoft hat im Rahmen seiner laufenden Partnerschaft mit OpenAI, dem Unternehmen hinter ChatGPT, KI-Technologie in E-Mails, Diashows und Tabellenkalkulationen am Arbeitsplatz integriert. Der Azure OpenAI-Dienst von Microsoft bietet ein leistungsstarkes Werkzeug, um diese Ergebnisse zu ermöglichen, wenn er in Verbindung mit ihrem Data Lake von mehr als zwei Milliarden Metadaten und Transaktionselementen genutzt wird.

Während ich dies schreibe, hat Google gerade eine öffentliche Warteliste für seinen Bard AI/Chat-Suchdienst geöffnet. Seit Jahren verwende ich verschiedene Google-APIs in meinem eigenen Code. Dabei habe ich keine Favoriten im Wettstreit der Tech-Giganten, sondern bin vor allem daran interessiert, dass ich das, was sie entwickeln, in meinen eigenen Projekten verwenden kann.

Hugging Face, das KI-Produkte entwickelt und die von anderen Unternehmen entwickelten Produkte hostet, arbeitet an Open-Source-Konkurrenten zu ChatGPT und wird dafür ebenfalls [AWS](https://iblnews.org/aws-partners-with-hugging-face-an-ai-startup-rival-to-chatgpt-working-on-open-source-models/)[^6] nutzen. Cohere AI, Anthropic, Hugging Face und Stability AI sind einige der Startups, die OpenAI und Hugging Face APIs für ihre Entwicklungen nutzen. Während ich dieses Kapitel schreibe, sehe ich Hugging Face als eine großartige Quelle für spezialisierte Modelle. Ich finde es toll, dass die Modelle von Hugging Face sowohl über ihre APIs als auch selbst gehostet auf unseren eigenen Servern und manchmal sogar auf den eigenen Laptops ausgeführt werden können. Hugging Face ist eine fantastische Resource, und auch wenn ich ihre Modelle in diesem Buch viel seltener verwende als OpenAI APIs, solltest du die Hosting- und Open-Source-Flexibilität von Hugging Face in Anspruch nehmen. In diesem Buch verwende ich OpenAI APIs, weil ich möchte, dass du dich schnell orientieren und deine eigenen Projekte erstellen kannst.

Lieber Leser, ich habe dieses Buch nicht für Entwickler geschrieben, die in etablierten KI-Firmen arbeiten (obwohl ich hoffe, dass diese Leute das vorliegende Material nützlich finden!). Dieses Buch wurde für kleine Entwickler geschrieben, die ihr eigenes Interesse daran haben, Werkzeuge zu schreiben, die ihnen Zeit einsparen. Hoffentlich wird es Entwicklern helfen, in die von ihnen entworfenen und geschriebenen Programme Funktionen einzubauen, die es mit den Lösungen der großen Technologieunternehmen aufnehmen können.

[^6]: https://iblnews.org/aws-partners-with-hugging-face-an-ai-startup-rival-to-chatgpt-working-on-open-source-models/