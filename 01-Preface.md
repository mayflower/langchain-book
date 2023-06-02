# Vorwort

Ich arbeite seit 1982 auf dem Gebiet der künstlichen Intelligenz und ohne Zweifel sind Large Language Models (LLMs) wie GPT-3 und Infrastrukturprojekte wie LangChain die größten technologischen Durchbrüche, die ich erlebt habe. In dieser Publikation werden die Projekte LangChain[^1] und GPT Index (LlamaIndex)[^2] zusammen mit den OpenAI GPT-3 und ChatGPT APIs verwendet, um eine Reihe von interessanten Problemen zu lösen.

Harrison Chase startete das LangChain-Projekt im Oktober 2022 und während ich dieses Buch im Februar 2023 schreibe, hat das GitHub-Repository für LangChain[^1] 171 Mitwirkende. Jerry Liu startete das GPT-Index-Projekt (kürzlich umbenannt in LlamaIndex) Ende 2022 und das GitHub-Repository für LlamaIndex[^2] hat derzeit vierundfünfzig Mitwirkende.

Das GitHub-Repository für die Beispiele in diesem Buch ist https://github.com/mark-watson/langchain-book-examples.git.

Obwohl die Dokumentation und die Online-Beispiele für LangChain und LlamaIndex exzellent sind, bin ich immer noch bestrebt, dieses Buch zu schreiben, um interessante Probleme zu lösen, an denen ich gerne arbeite. Diese sind: Information Retrieval, natürliche Sprachverarbeitung (natural language processing, NLP), Dialogsysteme (dialog agents) und semantisch verknüpfte Datenfelder. Ich hoffe, dass du, liebe Leserin, lieber Leser, von diesen Beispielen begeistert sein wirst und dass zumindest manche von diesen deine zukünftigen Projekte inspirieren werden.

[^1]: https://github.com/hwchase17/langchain
[^2]: https://github.com/jerryjliu/gpt_index

## Über den Autor

Ich habe mehr als 20 Bücher geschrieben, halte über 50 US-Patente und habe bei so interessanten Unternehmen wie Google, Capital One, SAIC, Mind AI und anderen gearbeitet. Auf meiner Webseite https://markwatson.com findest du Links, um die meisten meiner aktuellen Bücher kostenlos zu lesen. Wenn ich meine Karriere kurz zusammenfassen müsste, würde ich sagen, dass ich eine Menge Spaß hatte und meine Arbeit sehr genossen habe. Ich hoffe, dass das, was du hier lernst, dir sowohl Spaß machen, als auch dass es dir bei deiner Arbeit hilfreich sein wird.

Wenn du meine Arbeit unterstützen möchtest, kannst du meine Bücher auf Leanpub[^3] kaufen und meine Git-Repositories, die du nützlich findest, auf GitHub[^4] bewerten. Du kannst mich auch in den sozialen Medien über Mastodon[^5] und Twitter[^6] finden. Ich stehe auch als Berater zur Verfügung: https://markwatson.com.

[^3]: https://leanpub.com/u/markwatson
[^4]: https://github.com/mark-watson?tab=repositories&q=&type=public
[^5]: https://mastodon.social/@mark_watson
[^6]: https://twitter.com/mark_l_watson

## Buchumschlag

Ich lebe in Sedona, Arizona. Das Foto auf dem Buchdeckel habe ich im Januar 2023 von der Straße aus aufgenommen, in der ich wohne.

## Danksagung

>BILD FEHLT

![Mark und Carol Watson](marcandcarolwatson.jpg)

Dieses Bild zeigt mich und meine Frau Carol, die mir bei der Buchproduktion und -bearbeitung hilft.

Ich möchte mich auch bei den folgenden Lesern bedanken, die Fehler oder Rechtschreibfehler in diesem Buch gemeldet haben: Armando Flores  und Peter Solimine.

## Voraussetzungen für das Ausführen und Ändern der Beispiele im Buch

Ich präsentiere den vollständigen Quellcode sowie zahlreiche Beispiele für jedes im Buch aufgeführte Szenario. Falls du also keine Zugriffsrechte auf bestimmte APIs haben möchtest, ermöglicht dir das Buch dennoch, Schritt für Schritt mitzugehen.

Um OpenAIs GPT-3- und ChatGPT-Modelle zu nutzen, musst du sich für einen API-Schlüssel (kostenlose Version ist ausreichend) unter https://openai.com/api/ anmelden und die Umgebungsvariable **OPENAI_API_KEY** auf deinen Key-Value setzen.

Du benötigst einen API-Schlüssel für Beispiele, die **Googles Knowledge Graph APIs** verwenden.

Referenz: Google Knowledge Graph APIs[^7]. 

Die Beispielprogramme, die die Knowledge Graph APIs von Google verwenden, setzen voraus, dass du die Datei **~/.google_api_key** in deinem Home-Verzeichnis hast, die den Schlüssel von https://console.cloud.google.com/apis enthält.

Für die Beispiele, die die Websuche integrieren, musst du auch **SerpApi installieren**:


>REVIEW: in Version 2023-05-10 nicht mehr enthalten
```
1    pip install google-search-results
```

Siehe PyPi-Projektseite[^8]. Du kannst dich für ein kostenloses, nicht-kommerzielles Konto für 100 Suchen/Monat mit einer E-Mail-Adresse und Telefonnummer unter https://serpapi.com/users/welcome anmelden.

Für die GMail und Google Calendar Beispiele benötigst du außerdem ein Zapier-Konto[^9].

Nachdem du dieses Buch durchgelesen hast, kannst du dir die Webseite LangChainHub[^10] ansehen, die Prompts, Chains und Agents enthält, die für die Erstellung von LLM-Anwendungen nützlich sind.

[^7]: https://cloud.google.com/enterprise-knowledge-graph/docs/search-api
[^8]: https://pypi.org/project/google-search-results/
[^9]: https://zapier.com/
[^10]: https://github.com/hwchase17/langchain-hub

>REVIEW fehlende Übersetzung
## Issues and Workarounds for Using the Material in this Book

The libraries that I use in this book are frequently updated and sometimes the documentation or code links change, invalidating links in this book. I will try to keep everything up to date. Please report broken links to me.

In some cases you will need to use specific versions or libraries for some of the code examples.

Because the Python code listings use colorized text you may find that copying code from this eBook may drop space characters. All of the code listings are in the GitHub repository for this book so you should clone the repository to experiment with the example code.
