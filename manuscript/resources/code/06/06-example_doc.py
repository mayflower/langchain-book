"Example from documentation"

from llama_index import GPTSimpleVectorIndex, Document
from llama_index import download_loader

RDFReader = download_loader("RDFReader")
doc = RDFReader().load_data("sample.nt")
index = GPTSimpleVectorIndex(doc)

 result = index.query("list all countries in a quoted Python array, then explain why")

 print(result.response)