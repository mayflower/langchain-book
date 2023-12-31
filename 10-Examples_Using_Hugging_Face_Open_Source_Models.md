# Beispiele mit Hugging Face Open Source-Modellen

Als erstes musst du ein kostenloses Konto auf dem [Hugging Face Hub](https://huggingface.co/docs/huggingface_hub/index)[^1] erstellen, einen API-Schlüssel beschaffen und installieren:

````
1 pipinstall--upgradehuggingface_hub
````

Du musst die folgende Umgebungsvariable für dein Zugangs-Token zum Hugging Face Hub setzen:

````
1 HUGGINGFACEHUB_API_TOKEN
````

Bisher haben wir in diesem Buch den OpenAI LLM Wrapper verwendet:

````
1 from langchain.llms import OpenAI
````

Jetzt werden wir als Alternative die Hugging Face Wrapper Klasse verwenden:

```
1 from langchain import HuggingFaceHub
```

Die LangChain-Bibliothek versteckt die meisten Details der Verwendung beider APIs. Das ist eine wirklich gute Sache. Ich hatte ein paar Diskussionen auf technikorientierten Social Media mit Leuten, die sich daran stören, dass OpenAI nicht Open Source ist. Ich mag zwar die bequeme Nutzung der OpenAI-APIs, gleichzeitig möchte ich immer Alternativen für die von mir verwendete proprietäre Technologie haben.

Der Hugging Face Hub-Endpunkt in LangChain verbindet sich mit dem Hugging Face Hub und führt die Modelle über ihre freien Inferenz-Endpunkte aus.

[^1]: https://huggingface.co/docs/huggingface_hub/index

Wir brauchen einen Hugging Face-Account und -API Key, um diese Endpunkte zu nutzen. Es existieren zwei Hugging Face LLM Wrapper, einer für eine lokale Pipeline und einer für ein Modell, das vom Hugging Face Hub gehostet wird. Beachte, dass diese Wrapper nur für Modelle funktionieren, die die text2text-generation- und text-generation-Tasks unterstützen. Text2Text-generation bezieht sich auf die Funktion, eine Textfolge aus einer anderen Textfolge zu generieren. Zum Beispiel eine Zusammenfassung eines langen Artikels zu erstellen. Text-generation bezieht sich auf die Funktion, eine Textfolge komplett neu zu erstellen.

## LangChain als Wrapper für Hugging Face Prediction Model APIs

Wir beginnen mit einem einfachen Beispiel, das den Support für Prompt-Text in LangChain verwendet. Das folgende Beispiel ist im Skript **simple_example.py** enthalten:

```

```

Durch das Verändern von wenigen Zeilen Code kannst Du viele der Beispiele in diesem Buch mit Hugging Face-APIs statt mit OpenAi-APIs nutzen.

Die LangChain-Dokumentation enthält den Quellcode für einen Wrapper zur Nutzung lokaler Hugging Face-Einbettungen [hier](https://langchain.readthedocs.io/en/latest/_modules/langchain/embeddings/self_hosted_hugging_face.html)[^2].

## Eine eigene LlamaIndex Hugging Face LLM Wrapper Klasse erstellen, die auf deinem Laptop läuft

Wir laden das Hugging Face-Modell **facebook/opt-iml-1.3b** herunter, eine 2,6 Gigabyte große Datei. Dieses Modell wird bei der ersten Anfrage heruntergeladen und dann in **~/.cache/huggingface/hub** zur späteren Verwendung zwischengespeichert.

Dieses Beispiel ist die Abwandlung eines Beispiels für eigene LLMs aus der [LlamaIndex-Dokumentation](https://github.com/jerryjliu/llama_index/blob/main/docs/how_to/customization/custom_llms.md#example-using-a-custom-llm-model)[^3]. Beachte, dass ich in diesem Beispiel ein viel kleineres Modell verwendet und die Größe des Prompts und der Textausgabe reduziert habe.

[^2]: https://langchain.readthedocs.io/en/latest/_modules/langchain/embeddings/self_hosted_hugging_face.html
[^3]: https://github.com/jerryjliu/llama_index/blob/main/docs/how_to/customization/custom_llms.md#example-using-a-custom-llm-model

```

```

Wenn ich das auf einem M1 MacBook Pro nur mit der CPU laufen lasse (ohne GPU oder NeuralEngine-Konfiguration), können wir das Modell schnell von der Festplatte lesen, aber die Verarbeitung der Anfrage dauert eine Weile:

```

```

Auch wenn mein M1 MacBook ziemlich gut läuft, wenn ich TensorFlow und PyTorch für die Verwendung von Apple Silicon GPUs und Neural Engines konfiguriere, entwickle ich meine Modelle normalerweise mit Google Colab.

Lass uns das letzte Beispiel auf Colab wiederholen:


```

```

Mit einer Standard Colab GPU ist die Zeit für Abfrage/Vorhersage viel schneller. Hier ein [Link zu meinem Colab Notebook](https://colab.research.google.com/drive/1Ecg-0iid3AD05zM4HgPXTVHcgkGxyi3q?usp=sharing)[^4], falls du dieses Beispiel lieber auf Colab als auf deinem Laptop laufen lassen möchtest.

[^4]: https://colab.research.google.com/drive/1Ecg-0iid3AD05zM4HgPXTVHcgkGxyi3q?usp=sharing 
