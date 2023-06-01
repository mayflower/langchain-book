# Vorwort

Ich arbeite seit 1982 auf dem Gebiet der künstlichen Intelligenz und ohne Zweifel sind Large Language Models (LLMs) wie GPT-3 und Infrastrukturprojekte wie LangChain die größten technologischen Durchbrüche, die ich erlebt habe. In dieser Publikation werden die Projekte LangChain (1) und GPT Index (LlamaIndex)(2) zusammen mit den OpenAI GPT-3 und ChatGPT APIs verwendet, um eine Reihe von interessanten Problemen zu lösen.
Harrison Chase startete das LangChain-Projekt im Oktober 2022 und während ich dieses Buch im Februar 2023 schreibe, hat das GitHub-Repository für LangChain https://github.com/hwchase17/langchain einhunderteinundsiebzig Mitwirkende. Jerry Liu startete das GPT-Index-Projekt (kürzlich umbenannt in LlamaIndex) Ende 2022 und das GitHub-Repository für LlamaIndex https://github.com/jerryjliu/gpt_index hat derzeit vierundfünfzig Mitwirkende.
Das GitHub-Repository für die Beispiele in diesem Buch ist https://github.com/mark-watson/langchain-book-examples.git.
Obwohl die Dokumentation und die Online-Beispiele für LangChain und LlamaIndex exzellent sind, bin ich immer noch bestrebt, dieses Buch zu schreiben, um interessante Probleme zu lösen, an denen ich gerne arbeite. Diese sind: Information Retrieval, natürliche Sprachverarbeitung (natural language processing, NLP), Dialog-Agenten (dialog agents) und semantische web/linked Datenfelder. Ich hoffe, dass Sie, liebe Leserin, lieber Leser, von diesen Beispielen begeistert sein werden und dass zumindest einige von ihnen Ihre zukünftigen Projekte inspirieren werden.

(1) https://github.com/hwchase17/langchain
(2) https://github.com/jerryjliu/gpt_index

## Über den Autor

Ich habe über 20 Bücher geschrieben, ich halte über 50 US-Patente und ich habe bei so interessanten Unternehmen wie Google, Capital One, SAIC, Mind AI und anderen gearbeitet. Auf meiner Website https://markwatson.com finden Sie Links, um die meisten meiner aktuellen Bücher kostenlos zu lesen. Wenn ich meine Karriere kurz zusammenfassen müsste, würde ich sagen, dass ich eine Menge Spaß hatte und meine Arbeit sehr genossen habe. Ich hoffe, dass das, was Sie hier lernen, Ihnen sowohl Spaß machen als auch Ihnen bei Ihrer Arbeit helfen wird.
Wenn Sie meine Arbeit unterstützen möchten, können Sie meine Bücher auf Leanpub (3) kaufen und meine Git-Repositories, die Sie nützlich finden, auf GitHub (4) bewerten. Sie können mich auch in den sozialen Medien über Mastodon (5) und Twitter (6) finden. Ich stehe auch als Berater zur Verfügung: https: //markwatson.com.

(3) https://leanpub.com/u/markwatson
(4) https://github.com/mark-watson?tab=repositories&q=&type=public
(5) https://mastodon.social/@mark_watson
(6) https://twitter.com/mark_l_watson

## Buchumschlag

Ich lebe in Sedona, Arizona. Das Foto auf dem Buchdeckel habe ich im Januar 2023 von der Straße aus aufgenommen, in der ich wohne.

## Danksagung

Dieses Bild zeigt mich und meine Frau Carol, die mir bei der Buchproduktion und -bearbeitung hilft.
Ich möchte mich auch bei den folgenden Lesern bedanken, die Fehler oder Rechtschreibfehler in diesem Buch gemeldet haben: bis jetzt keine.

## Voraussetzungen für das Ausführen und Ändern der Beispiele im Buch

Ich zeige den vollständigen Quellcode und eine ganze Reihe von Beispielen für jedes Beispiel im Buch. Wenn Sie also keinen Zugang zu einigen der folgenden APIs erhalten möchten, können Sie trotzdem im Buch mitlesen.
Um OpenAIs GPT-3- und ChatGPT-Modelle zu nutzen, müssen Sie sich für einen API-Schlüssel (kostenlose Version ist ausreichend) unter https://openai.com/api/ anmelden und die Umgebungsvariable **OPENAI_API_KEY** auf Ihren Key-Value setzen.
Sie benötigen einen API-Schlüssel für Beispiele, die Googles Knowledge Graph APIs verwenden.
Referenz Google Knowledge Graph APIs (7). Die Beispielprogramme, die die Knowledge Graph APIs von Google verwenden, setzen voraus, dass Sie die Datei ~/.google_api_key in Ihrem Home-Verzeichnis haben, die den Schlüssel von https://console.cloud.google.com/apis enthält.
Für die Beispiele, die die Websuche integrieren, müssen Sie auch SerpApi installieren:

```
1    pip install google-search-results
```

Siehe PyPi-Projektseite (8). Sie können sich für ein kostenloses, nicht-kommerzielles Konto für 100 Suchen/Monat mit einer E-Mail-Adresse und Telefonnummer unter https://serpapi.com/users/welcome anmelden.
Für die GMail und Google Calendar Beispiele benötigen Sie außerdem ein Zapier-Konto (9).
Nachdem Sie dieses Buch durchgelesen haben, können Sie sich die Website LangChainHub (10) ansehen, die Prompts, Chains und Agents enthält, die für die Erstellung von LLM-Anwendungen nützlich sind.


(7) https://cloud.google.com/enterprise-knowledge-graph/docs/search-api
(8) https://pypi.org/project/google-search-results/
(9) zapier.com
(10) https://github.com/hwchase17/langchain-hub
