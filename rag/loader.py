from pathlib import Path

def load_notes(folder:str) -> list[dict]:
    """Read every .md and .txt file in a folder into memory"""
    docs = []
    for path in Path(folder).rglob("*"):
        if path.suffix in (".md", ".txt"):
            text = path.read_text(encoding="utf-8") # default for now
            docs.append({
                "text": text,
                "source": str(path), # metadata aka where it came from
            }) 
    return docs