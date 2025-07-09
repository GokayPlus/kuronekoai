import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

# === Ayarlar ===
DATA_DIR = "data/zincir_feed"
os.makedirs(DATA_DIR, exist_ok=True)

llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature": 0.7})

def get_related_topics(topic: str, max_topics=5):
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
        "{topic}" Produce subheadings related to the title. Each should be informative and independently researchable.
            Just list in points:
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(topic=topic)
    return [line.strip("- ") for line in result.strip().split("\n") if line.strip()]

def get_google_links(query, num_results=3):
    return list(search(query, num_results=num_results))

def fetch_clean_text(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        [s.decompose() for s in soup(['script', 'style', 'header', 'footer', 'nav'])]
        text = soup.get_text()
        text = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])
        return text
    except:
        return ""

def save_text(topic, content):
    with open(f"{DATA_DIR}/{topic[:50].replace('/', '_')}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def embed_all():
    embeddings = HuggingFaceEmbeddings()
    texts = []
    for filename in os.listdir(DATA_DIR):
        with open(f"{DATA_DIR}/{filename}", encoding="utf-8") as f:
            text = f.read()
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
            chunks = splitter.split_text(text)
            for chunk in chunks:
                texts.append(Document(page_content=chunk, metadata={"source": filename}))
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("faiss_index/zincir_feed")

if __name__ == "__main__":
    ana_konu = input("What is the main fact buddy?")
    alt_konular = get_related_topics(ana_konu)
    print("\n[+] Subheadings:", alt_konular)

    for konu in [ana_konu] + alt_konular:
        print(f"\n[+] {konu} searching about this fact...")
        links = get_google_links(konu)
        full_text = ""
        for link in links:
            print(f"  - {link}")
            text = fetch_clean_text(link)
            full_text += text + "\n"
        save_text(konu, full_text)

    print("\n[+] Embedding...")
    embed_all()
    print("[✓] All the content has been processed and embedded in FAISS.")
