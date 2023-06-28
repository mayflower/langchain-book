# Verwendung von Zapier-Integrationen mit GMail und Google Kalender

Zapier ist ein spezieller Dienst, mit dem man Integrationen mit Hunderten von Cloud-Services erstellen kann. Hier werden wir einige Demos für das Schreiben von automatischen Integrationen mit GMail und Google Calendar schreiben.

Die Verwendung des Zapier-Dienstes ist einfach. Du musst die Dienste, mit denen du interagieren möchtest, auf der Zapier-Entwickler-Webseite registrieren und kannst dann mithilfe von Aufforderungen in natürlicher Sprache ausdrücken, wie du mit den Diensten interagieren möchtest.

## Entwicklungsumgebung einrichten

Du benötigst einen Entwicklerschlüssel für die [Zapier Natural Language Actions API](https://nla.zapier.com/get-started/)[^1]. Gehe zu dieser verlinkten Webseite und suche nach "Dev App" in der Spalte "Provider Name". Wenn kein Schlüssel vorhanden ist, musst du eine Aktion einrichten, um einen Schlüssel zu erstellen. Klicke auf "Set up Actions" (Aktionen einrichten) und folge den Anweisungen. Dein Schlüssel wird in der Spalte "Persönlicher API-Schlüssel" für die "Dev App" angezeigt. Klicke darauf, um deinen Schlüssel zu sehen und zu kopieren. Du kannst hier die [Dokumentation lesen](https://nla.zapier.com/api/v1/dynamic/docs)[^2].

Als ich mein Zapier-Konto eingerichtet habe, habe ich drei Zapier Natural Language Actions eingerichtet:
 
- Gmail: Find Email
- Gmail: Send Email
- Google Kalender: Find Event

Wenn du dasselbe tust, siehst du die von Zapier registrierten Aktionen:

>>>BILD einfügen<<<

[^1]: https://nla.zapier.com/get-started/
[^2]: https://nla.zapier.com/api/v1/dynamic/docs

## Versenden einer GMail zum Test

Im folgenden Beispiel ersetze **TEST_EMAIL_ADDRESS** durch eine E-Mail-Adresse, die du zu Testzwecken verwenden kannst.

```
1 from langchain.llms import OpenAI
2 from langchain.agents import initialize_agent
3 from langchain.agents.agent_toolkits import ZapierToolkit
4 from langchain.utilities.zapier import ZapierNLAWrapper
5
6 llm = OpenAI(temperature=0)
7 zapier = ZapierNLAWrapper()
8 toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
9 agent = initialize_agent(toolkit.get_tools(), llm, agent=\
10 "zero-shot-react-description", verbose=True)
11
12 agent.run("Send an Email to TEST_EMAIL_ADDRESS via gmail \
13 that is a pitch for hiring Mark Watson as a consultant fo
14 r deep learning and large language models")
```

Hier ist die Beispielausgabe:

```
1 $ pythonsend_gmail.py
2
3
4 > Entering new AgentExecutor chain...
5 I need to use the Gmail: Send Email tool
6 Action:Gmail:SendEmail
7 ActionInput:SendanemailtoTEST_EMAIL_ADDRESSwithth\
8 esubject"Pitch for Hiring MarkWatsonasaConsultantf
9 orDeepLearningandLargeLanguageModels"andthebody
10 "DearMarkWatson,Iamwritingtoyoutopitchtheidea
11 ofhiringyouasaconsultantfordeeplearningandlarge
12 language models. I believe you have the expertise and ex
13 periencetohelpusachieveourgoals.Pleaseletmeknow
14 if you are interested in discussing further. Thank you f
15 oryourtime."
16 Cc:notenoughinformationprovidedintheinstruction,m\
17 issingCc
18 Observation:{"labelIds":"SENT"}
19 Thought:Inowknowthefinalanswer
20 FinalAnswer:AnemailhasbeensenttoTEST_EMAIL_ADDRES\
21 Swiththesubject"PitchforHiringMarkWatsonasaCon
22 sultantforDeepLearningandLargeLanguageModels"and
23 thebody"DearMarkWatson,Iamwritingtoyoutopitch
24 theideaofhiringyouasaconsultantfordeeplearning
25 andlargelanguagemodels.Ibelieveyouhavetheexperti
26 seandexperiencetohelpusachieveourgoals.Pleasele
27 tmeknowifyouareinterestedindiscussingfurther.Th
28 ankyouforyourtime."
29
30 >Finishedchain.
```

## Beispiel für die Integration von Google Calendar

Angenommen, du hast die Zapier Natural Language Action "Google Calendar: Find Event" konfiguriert. Dann funktioniert derselbe Code, den wir im letzten Abschnitt zum Senden einer E-Mail verwendet haben, auch für die Überprüfung von Kalendereinträgen. Man muss nur die Aufforderung in natürlicher Sprache ändern:

```
1 fromlangchain.llmsimportOpenAI
2 fromlangchain.agentsimportinitialize_agent
3 fromlangchain.agents.agent_toolkitsimportZapierToolkit
4 fromlangchain.utilities.zapierimportZapierNLAWrapper
5
6 llm=OpenAI(temperature=0)
7 zapier=ZapierNLAWrapper()
8 toolkit=ZapierToolkit.from_zapier_nla_wrapper(zapier)
9 agent=initialize_agent(toolkit.get_tools(),llm,
10 agent="zero-shot-react-descripti\
11 on",verbose=True)
12
13 agent.run("GetmyGoogleCalendarentriesfortomorrow")
```

Die Ausgabe sieht folgendermaßen aus:

```
1 $pythonget_google_calendar.py 2
3 >EnteringnewAgentExecutorchain...
4 I need to find events in my Google Calendar
5 Action:GoogleCalendar:FindEvent
6 ActionInput:FindeventsinmyGoogleCalendartomorrow
7 Observation:{"location":"GregtocallMarkon(928)XXX\
8 -ZZZZ","kind":"calendar#event","end__dateTime":"2023-
9 03-23T10:00:00-07:00","status":"confirmed","end__dateT
10 ime_pretty":"Mar23,202310:00AM","htmlLink":"https:/
11 /zpr.io/WWWWWWWW"}
12 Thought:Inowknowthefinalanswer
13 FinalAnswer:IhaveaneventinmyGoogleCalendartomor\
14 rowat10:00AM.
15
16 >Finishedchain
```

Ich habe diese Ausgabe bearbeitet, um einige private Informationen zu entfernen.
