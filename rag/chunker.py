def chunk_text(text: str, chunk_size:int  = 400, chunk_overlap: int = 60) -> list[str]:
    """Split on Paragraphs and then pack into chunk size pieces with overlapping"""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()] 
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current = "\n\n" + para
        else:
            chunks.append(current.strip())
            #carry the latest overlap character into next chunk
            current = current[-chunk_overlap:] + "\n\n" + para
    
    if current.strip():
        chunks.append(current.strip())
    return chunks