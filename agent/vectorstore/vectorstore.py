from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document

class VectorStore:

    def __init__(self, agent):
        self.embedding: Embeddings = agent.llm.embedding
        self.vector_store = InMemoryVectorStore(self.embedding)
        self.__post__init__()

    def __post__init__(self):
        self._initialize_vectorstore()

    def _initialize_vectorstore(self):
        pass
        # self.embedding.embed_query()

    def wrap_text(
        self,
        text: str,
        metadata: dict
    ) -> Document:
        
        return Document(
            page_content=text, 
            metadata=metadata
        )
    
    def cache_document(
            
    ):
        pass