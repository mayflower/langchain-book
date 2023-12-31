# Vorwort

Ich arbeite seit 1982 auf dem Gebiet der künstlichen Intelligenz und ohne Zweifel sind Large Language Models (LLMs) wie GPT-3 und Infrastrukturprojekte wie LangChain die größten technologischen Durchbrüche, die ich erlebt habe. In dieser Publikation werden die Projekte [LangChain](https://github.com/hwchase17/langchain)[^1] und [GPT Index (LlamaIndex)](https://github.com/jerryjliu/gpt_index)[^2] zusammen mit den OpenAI GPT-3 und ChatGPT APIs verwendet, um eine Reihe von interessanten Problemen zu lösen.

Harrison Chase startete das LangChain-Projekt im Oktober 2022 und während ich dieses Buch im Februar 2023 schreibe, hat das GitHub-Repository für [LangChain](https://github.com/hwchase17/langchain)[^1] 171 Mitwirkende. Jerry Liu startete das GPT-Index-Projekt (kürzlich umbenannt in LlamaIndex) Ende 2022 und das GitHub-Repository für [LlamaIndex](https://github.com/jerryjliu/gpt_index)[^2] hat derzeit vierundfünfzig Mitwirkende.

Das GitHub-Repository für die Beispiele in diesem Buch ist https://github.com/mark-watson/langchain-book-examples.git.

Obwohl die Dokumentation und die Online-Beispiele für LangChain und LlamaIndex exzellent sind, bin ich immer noch bestrebt, dieses Buch zu schreiben, um interessante Probleme zu lösen, an denen ich gerne arbeite. Diese sind: Information Retrieval, natürliche Sprachverarbeitung (natural language processing, NLP), Dialogsysteme (dialog agents) und semantisch verknüpfte Datenfelder. Ich hoffe, dass du, liebe Leserin, lieber Leser, von diesen Beispielen begeistert sein wirst und dass zumindest manche von diesen deine zukünftigen Projekte inspirieren werden.

[^1]: https://github.com/hwchase17/langchain
[^2]: https://github.com/jerryjliu/gpt_index

## Über den Autor

Ich habe mehr als 20 Bücher geschrieben, halte über 50 US-Patente und habe bei so interessanten Unternehmen wie Google, Capital One, SAIC, Mind AI und anderen gearbeitet. Auf meiner Webseite https://markwatson.com findest du Links, um die meisten meiner aktuellen Bücher kostenlos zu lesen. Wenn ich meine Karriere kurz zusammenfassen müsste, würde ich sagen, dass ich eine Menge Spaß hatte und meine Arbeit sehr genossen habe. Ich hoffe, dass das, was du hier lernst, dir sowohl Spaß machen, als auch dass es dir bei deiner Arbeit hilfreich sein wird.

Wenn du meine Arbeit unterstützen möchtest, kannst du meine Bücher auf [Leanpub](https://leanpub.com/u/markwatson)[^3] kaufen und meine Git-Repositories, die du nützlich findest, auf [GitHub](https://github.com/mark-watson?tab=repositories&q=&type=public)[^4] bewerten. Du kannst mich auch in den sozialen Medien über [Mastodon](https://mastodon.social/@mark_watson)[^5] und [Twitter](https://twitter.com/mark_l_watson)[^6] finden. Ich stehe auch als Berater zur Verfügung: https://markwatson.com.

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

Ich präsentiere den vollständigen Quellcode sowie zahlreiche Beispiele für jedes im Buch aufgeführte Szenario. Falls du also keinen Zugriff auf bestimmte APIs haben möchtest, ermöglicht dir das Buch dennoch, Schritt für Schritt mitzugehen.

Um OpenAIs GPT-3- und ChatGPT-Modelle zu nutzen, musst du dich für einen API-Schlüssel (kostenlose Version ist ausreichend) unter https://openai.com/api/ anmelden und die Umgebungsvariable **OPENAI_API_KEY** auf deinen Key-Value setzen.

Du benötigst einen API-Schlüssel für Beispiele, die **Googles Knowledge Graph APIs** verwenden.

Referenz: [Google Knowledge Graph APIs](https://cloud.google.com/enterprise-knowledge-graph/docs/search-api)[^7]. 

Die Beispielprogramme, die die Knowledge Graph APIs von Google verwenden, setzen voraus, dass sich die Datei **~/.google_api_key** in deinem Home-Verzeichnis befindet und den Schlüssel von https://console.cloud.google.com/apis enthält.

Für die Beispiele, die die Websuche integrieren, musst du **SerpApi installieren**. Siehe [PyPi-Projektseite](https://pypi.org/project/google-search-results/)[^8]. 

Du kannst dich für ein kostenloses, nicht-kommerzielles Konto für 100 Suchen/Monat mit einer E-Mail-Adresse und Telefonnummer bei https://serpapi.com/users/welcome anmelden.

Für die GMail- und Google Calendar-Beispiele benötigst du außerdem ein [Zapier](https://zapier.com/)-Konto[^9].

Nachdem du dieses Buch durchgelesen hast, kannst du dir die Webseite [LangChainHub](https://github.com/hwchase17/langchain-hub)[^10] ansehen, die Prompts, Chains und Agents enthält, die für die Erstellung von LLM-Anwendungen nützlich sind.

[^7]: https://cloud.google.com/enterprise-knowledge-graph/docs/search-api
[^8]: https://pypi.org/project/google-search-results/
[^9]: https://zapier.com/
[^10]: https://github.com/hwchase17/langchain-hub

## Probleme und Workarounds zur Verwendung der Materialien in diesem Buch

Die Bibliotheken, die ich in diesem Buch verwende, werden häufig aktualisiert und manchmal ändert sich die Dokumentation oder der Link zum Code, wodurch diese in diesem Buch ungültig werden. Ich werde versuchen, alles auf dem neuesten Stand zu halten. Bitte meldet mir defekte Links.

In manchen Fällen wirst du spezielle Versionen oder Bibliotheken für einige der Code-Beispiele verwenden müssen.

Da die Python-Code-Beispiele farbigen Text verwenden, kann es vorkommen, dass beim Kopieren von Code aus diesem E-Book Leerzeichen verloren gehen. Alle Code-Beispiele befinden sich im GitHub-Repository für dieses Buch, daher solltest du das Repository klonen, um mit den Codebeispielen zu experimentieren.