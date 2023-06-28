1 from langchain.text_splitter import CharacterTextSplitter
2 from langchain.vectorstores import Chroma
3 from langchain.embeddings import OpenAIEmbeddings
4 from langchain.document_loaders import DirectoryLoader
5 from langchain import OpenAI, VectorDBQA
6
7 embeddings = OpenAIEmbeddings() 8
9 loader=DirectoryLoader('../data/', glob="**/*.txt")
10 documents = loader.load()
11 text_splitter = CharacterTextSplitter(chunk_size=2500, ch\
12 unk_overlap=0)
13
14 texts = text_splitter.split_documents(documents)
15
16 docsearch = Chroma.from_documents(texts, embeddings)
17
18 qa = VectorDBQA.from_chain_type(llm=OpenAI(),
19                                 chain_type="stuff",
20                                 vectorstore=docsearch)
21
22 def query(q):
23     print(f"Query: {q}")
24     print(f"Answer: {qa.run(q)}")
25
26 query("What kinds of equipment are in a chemistry laborat\
27 ory?")
28 query("What is Austrian School of Economics?")
29 query("Why do people engage in sports?")
30 query("What is the effect of bodychemistry on exercise?")