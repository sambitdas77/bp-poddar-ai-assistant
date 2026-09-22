
def build_prompt(question: str, docs):
    """
    Creates the final prompt sent to Gemini.
    """

    if docs:
        context = "\n\n".join([
            f"""
Source File : {doc.metadata.get("source_file", "Unknown")}
Page : {doc.metadata.get("page", 0) + 1}

Content:
{doc.page_content}
"""
            for doc in docs
        ])
    else:
        context = "No relevant context found."

    prompt = f"""
You are BP Poddar AI Assistant.

Personality:
- Friendly.
- Helpful.
- Speak like a senior BP Poddar student.
- Format answers nicely using Markdown.

Rules:

1. If the answer exists inside the provided context, answer ONLY using that context.
2. Explain topics in a structured manner with headings and bullet points.
3. Mention the source page if relevant.
4. If the context does not contain the answer, reply:
   "The uploaded BP Poddar documents do not contain this information."

Context:
{context}

Question:
{question}
"""

    return prompt