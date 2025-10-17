from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.duckdb import DuckDBVectorStore
from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
import os
import pandas as pd
from sqlalchemy import create_engine
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine

def load_docs():
    documents = SimpleDirectoryReader("docs").load_data()
    vector_store = DuckDBVectorStore(database_name = "ssa2026.duckdb",table_name = "articles",persist_dir="./", embed_dim=768)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

def llm_query(query: str) -> str:
    engine = create_engine("duckdb:///ssa2026.duckdb")
    sql_database = SQLDatabase(engine, include_tables=["articles"])
    query_engine = NLSQLTableQueryEngine(sql_database)
    response = query_engine.query(query)

    return response.response

# set up embedding
ollama_embedding = OllamaEmbedding(
    model_name="embeddinggemma",
    base_url="http://localhost:11434",
)

def write_markdown_file(filename, content):

  try:
    with open(filename, 'w', encoding='utf-8') as f:  # Use utf-8 encoding for broader character support
      f.write(content)
    print(f"Markdown file '{filename}' created successfully.")
  except Exception as e:
    print(f"Error writing to file '{filename}': {e}")


# set up llm
llm = Ollama(model="gpt-oss", request_timeout=12000.0)

# set up as global models
Settings.llm = llm
Settings.embed_model = ollama_embedding

# load_docs()


# resp =llm_query("""How are researchers using the cloud base data to study changes 
#                 to the earth's surface, the ionosphere, and air moisture content 
#                 using GNSS. Reference multiple studies in long form essay on this topic. 
#                 Focus on the challenges involved with respect to early career professionals. 
#                 Use only the information provided in the database.""")

# resp =llm_query("""List the research techniques using the cloud base data to study changes 
#                 to the earth's surface, the ionosphere, and air moisture content 
#                 using GNSS. Focus on machine learning and artificial intelligence methodologies.
#                 Write this in a long form essay on this topic. Focus on the challenges involved 
#                 with respect to early career professionals.  Use only the information provided in 
#                 the database.""")

# resp =llm_query("""List the research techniques using the cloud base data to study seismic 
#                 events, subsurface geology, and ionospheric changes
#                 using seismic data. Focus on machine learning and artificial intelligence methodologies.
#                 Write this in a long form essay on this topic. Focus on the challenges involved 
#                 with respect to early career professionals. Provide references from articles""")

# resp =llm_query("""List the data preparation techniques using the cloud based data to study seismic 
#                 events, subsurface geology, and ionospheric changes using miniSEED data. Focus on 
#                 machine learning and artificial intelligence methodologies. Write this in a long form 
#                 essay on this topic. Focus on the challenges involved with respect to early career 
#                 professionals. Provide references from articles""")

# resp =llm_query("""List the all the types of studies using cloud based seismic and geodetic data. 
#                 Focus on machine learning and artificial intelligence methodologies. Write a 
#                 long form essay on this topic. Focus on the challenges involved with respect to 
#                 early career professionals. Provide references from articles""")


resp = llm_query("""You are performing a literature review of GNSS, geodesy, GPS, or precise
                 positioning from journal articles. Using only the database,  create an 
                 list of use cases. Include descriptions of the data collected and the analyses performed. 
                 Write a detailed summary of the workflow for each analysis performed in essay form. 
                 Only focus on geodesy use cases. Do not provide a concise synthesis, write 
                 response as an essay. Do not include any reference ids from the database.
                 
                 Format the use cases like the following example:

                 ### the use case 

                 | Paper (excerpt) | Data Collected | Analysis Workflow |
                 |-----------------|----------------|-------------------|
                 | “GNSS Meteorology: Remote sensing of atmospheric water vapor” (Bevis et al., 1992) | Continuous dual‑frequency GNSS carrier‑phase and pseudorange observations from a global network of precision receivers. | 1. **Pre‑processing** – cycle slip detection, carrier‑phase ambiguities resolved by integer or float solutions; 2. **Tropospheric delay separation** – linear combination of L1/L2 to eliminate ionosphere; 3. **ZTD estimation** – least‑squares adjustment; 4. **Conversion to PWV** – applying atmospheric mapping functions and specific humidity equations; 5. **Spatial interpolation** – Kriging or spline to generate continuous PWV fields; 6. **Validation** – comparison with radiosonde and microwave radiometer measurements. |    """)

# resp = llm_query("""You are performing a literature review of tectonic, earthquakes, seismic data,
#                  or seismology from journal articles. Using only the database, create an 
#                  list of use cases. Include descriptions of the data collected and the analyses performed. 
#                  Write a detailed summary of the workflow for each analysis performed in essay form. 
#                  Only focus on seismology use cases. Do not provide a concise synthesis, write 
#                  response as an essay. Do not include any reference ids from the database.
                 
#                  Format the use cases like the following example:

#                  ### the use case 

#                  | Paper (excerpt) | Data Collected | Analysis Workflow |
#                  |-----------------|----------------|-------------------|
#                  | “GNSS Meteorology: Remote sensing of atmospheric water vapor” (Bevis et al., 1992) | Continuous dual‑frequency GNSS carrier‑phase and pseudorange observations from a global network of precision receivers. | 1. **Pre‑processing** – cycle slip detection, carrier‑phase ambiguities resolved by integer or float solutions; 2. **Tropospheric delay separation** – linear combination of L1/L2 to eliminate ionosphere; 3. **ZTD estimation** – least‑squares adjustment; 4. **Conversion to PWV** – applying atmospheric mapping functions and specific humidity equations; 5. **Spatial interpolation** – Kriging or spline to generate continuous PWV fields; 6. **Validation** – comparison with radiosonde and microwave radiometer measurements. |                  
#                  """)

write_markdown_file("workflow_geodesy_gpt-oss_3.md", resp)