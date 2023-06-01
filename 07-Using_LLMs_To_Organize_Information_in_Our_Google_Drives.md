# Verwendung von LLMs zur Organisation von Informationen in unseren Google Drives

Mein digitales Leben besteht aus dem Schreiben und Arbeiten als KI-Anwender sowie aus Lernaktivitäten, die ich mit meinem Selbstbild eines "sanftmütigen Wissenschaftlers" rechtfertige. Cloud-Speicher wie GitHub, Google Drive, Microsoft OneDrive und iCloud sind zentral für meine Aktivitäten.
Vor etwa zehn Jahren verbrachte ich zwei Monate damit, ein System in Clojure zu schreiben, das meine eigene, persönliche DropBox werden sollte, ergänzt durch verschiedene NLP-Tools und ein FireFox-Plugin, um Web-Clippings direkt an mein persönliches System zu senden. Um ehrlich zu sein, habe ich mein eigenes Projekt nach ein paar Monaten wieder eingestellt, weil die Zeit, die ich für die Organisation meiner Informationen benötigte, einen größeren Aufwand darstellte als den Nutzen, den ich daraus zog.
In diesem Kapitel werde ich dir Teile eines neuen Systems vorstellen, das ich für meinen persönlichen Gebrauch entwickle und das mir helfen soll, mein Material in Google Drive (und eventuell in anderen Cloud-Diensten) zu organisieren. Sei nicht überrascht, wenn das fertige Projekt ein weiteres Beispiel in einer zukünftigen Auflage dieses Buches ist!
Mit den unten aufgeführten Google-Einrichtungsanweisungen erhältst du ein Pop-up-Fenster mit einer Warnung wie dieser (dies zeigt meine Google Mail-Adresse, du solltest hier deine eigene Google Mail-Adresse sehen, vorausgesetzt, du hast dich kürzlich mit deinem Standard-Webbrowser bei Google Mail angemeldet):

>>> BILD einfügen <<<

Du musst zuerst auf Erweitert und dann auf den Link Gehe zu GoogleAPIExamples (unsicher) in der unteren linken Ecke klicken und dann dieses Beispiel vorübergehend in deinem Gmail-Konto autorisieren.

## Einrichten der Anforderungen.

Du musst ein Credential unter https://console.cloud.google. com/cloud-resource-manager erstellen (kopiert aus der PyDrive-Dokumentation (1), wobei der Anwendungstyp auf "Desktop" geändert werden muss):
- Suche nach "Google Drive API", wähle den Eintrag und klicke auf "Aktivieren".
- Wähle "Credentials" aus dem linken Menü, klicke "Create Credentials", wähle "OAuth client ID".
- Nun müssen der Produktname und der Berechtigungsbildschirm festgelegt werden -> klicke auf "Configure consent screen" und folge den Anweisungen. Sobald du fertig bist:
- Wähle als "Anwendungstyp" eine Desktop-Anwendung.
- Gib einen geeigneten Namen ein.
- Gib Siehttp://localhost:8080for'AuthorizedJavaScriptorigins' ein.
- Gib http://localhost:8080/ für "Authorized redirect URIs" ein.
- Klicke auf "Speichern".
- Klicke auf "JSON herunterladen" auf der rechten Seite der Client-ID, um client_secret_.json herunterzuladen. Kopiere die heruntergeladene JSON-Anmeldedatei in das Beispielverzeichnis google_drive_llm für dieses Kapitel.

(1) https://pythonhosted.org/PyDrive/quickstart.html

## Dienstprogramm, um alle Textdateien aus dem obersten Google Drive-Ordner zu holen

Für dieses Beispiel werden wir unser Testskript bei Google authentifizieren und alle Textdateien der obersten Ebene mit Namen, die auf ".txt" enden, in das lokale Dateisystem im Unterverzeichnis data kopieren. Der Code befindet sich im Verzeichnis google_drive_llm in der Datei fetch_txt_files.py (bearbeitet um die Seitenbreite anzupassen):

```
1 from pydrive.auth import GoogleAuth
2 from pydrive.drive import GoogleDrive
3 from pathlib import Path
4
5 # good GD search docs:
6 # https://developers.google.com/drive/api/guides/search-files
7
8
9 # Authenticate with Google
10 gauth = GoogleAuth()
11 gauth.LocalWebserverAuth()
12 drive = GoogleDrive(gauth)
13
14 def get_txt_files(dir_id='root'):
15    " get all plain text files with .txt extension in top\
16 level Google Drive directory "
17
18    file_list = drive.ListFile({'q': f"'{dir_id}' in pare\
19 nts and trashed = false"}).GetList()
20    for file1 in file_list:
21        print('title: %s, id: %s' % (file1['title'], file\
22 1['id']))
23    return [[file1['title'], file1['id'], file1.GetConten\
24 tString()]
25            for file1 in file_list
26                if file1['title'].endswith(".txt")]27
27
28 def create_test_file():
29    " not currently used, but useful for testing. "
30
31    # Create GoogleDriveFile instance with title 'Hello.t\
32 xt':
33    file1 = drive.CreateFile({'title': 'Hello.txt'})
34    file1.SetContentString('Hello World!')
35    file1.Upload()
36
37 def test():
38    fl = get_txt_files()
39    for f in fl:
40        print(f)
41        file1 = open("data/" + f[0],"w")
42        file1.write(f[2])
43        file1.close()
44
45 if __name__ == '__main__':
46    test()
```

Zum Testen habe ich nur eine Textdatei mit der Dateierweiterung ".txt" auf meinem Google Drive, so dass meine Ausgabe nach der Ausführung dieses Skripts wie die folgende Auflistung aussieht. Ich habe die Ausgabe bearbeitet, um meine Datei-IDs zu ändern und nur ein paar Zeilen des Debug-Ausdrucks der Dateititel zu drucken.

```
1 $ python fetch_txt_files.py
2 Your browser has been opened to visit:
3
4 https://accounts.google.com/o/oauth2/auth?client_id=5\
5 29311921932-xsmj3hhiplr0dhqjln13fo4rrtvoslo8.apps.googleu
6 sercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3B6180
7 %2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive
8 &access_type=offline&response_type=code
9
10 Authentication successful.
11
12 title: testdata, id: 1TZ9bnL5XYQvKACJw8VoKWdVJ8jeCszJ
13 title: sports.txt, id: 18RN4ojvURWt5yoKNtDdAJbh4fvmRpzwb
14 title: Anaconda blog article, id: 1kpLaYQA4Ao8ZbdFaXU209h\
15 g-z0tv1xA7YOQ4L8y8NbU
16 title: backups_2023, id: 1-k_r1HTfuZRWN7vwWWsYqfssl0C96J2x
17 title: Work notes, id: 1fDyHyZtKI-0oRNabA_P41LltYjGoek21
18 title:SedonaWritingGroupContactList,id:1zK-5v9OQUf\
19 y8Sw33nTCl9vnL822hL1w
20 ...
21 ['sports.txt', '18RN4ojvURWt5yoKNtDdAJbh4fvmRpzwb', 'Spor\
22 t is generally recognised as activities based in physical
23 athleticism or physical dexterity.[3] Sports are usually
24 governed by rules to ensure fair competition and consist
25 ent adjudication of the winner.\n\n"Sport" comes from the
26 Old French desport meaning "leisure", with the oldest de
27 finition in English from around 1300 being "anything huma
28 ns find amusing or entertaining".[4]\n\nOther bodies advo
29 cate widening the definition of sport to include all phys
30 ical activity and exercise. For instance, the Council of
31 Europe include all forms of physical exercise, including
32 those completed just for fun.\n\n']
```

## Vektorindizes für Dateien in speziellen Google Drive-Ordnern erstellen

Das Beispiel-Skript im letzten Abschnitt sollte Kopien der Textdateien in Deinem obersten Google Documents Ordner mit der Endung ".txt" erzeugt haben. Jetzt verwenden wir den gleichen LlamaIndex Testcode wie in einem früheren Kapitel. Hier is das Testskript **index_and_QA.py**: 

```

```

Für meine Testdatei sieht der Output so aus:

```

```

Es ist interessant zu sehen, wie das Ergebnis der Abfrage in eine schöne Form umgeschrieben wird, verglichen mit dem Rohtext in der Datei **sports.txt** in meinem Google Drive:

```

```

## Zusammenfassung Google Drive Beispiele

Wenn Du Google Drive bereits zum Speichern Deiner Arbeitsnotizen und anderer Dokuemnte verwendest, 
dann magst Du vielleicht das einfache Beispiel in diesem Kapitel erweitern, um Dein eigenes Abfragesystem für Dokumente zu erstellen.
Zusätzlich zu Google Drive nutze ich auch Microsoft 365 und OneDrive für meine Arbeit und persönlichen Projekte.
Ich habe noch keine eigenen Konnektoren für OneDrive geschrieben, aber das ist auf meiner persönlichen To do-Liste, unter Verwendung der Microsoft Library https://github.com/OneDrive/onedrive-sdk-python.
