# Questions that the files DO answer
for q in on_topic_questions:
    top_score = store.search(embed(q), k=1)[0][1]  # Get the score of the top match
    print (f"Question: {q}\nTop Match Score: {top_score:.3f}\n")

for q in off_topic_questions:
    top_score = store.search(embed(q), k=1)[0][1]  # Get the score of the top match
    print (f"Question: {q}\nTop Match Score: {top_score:.3f}\n")