from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Prompt engineering the model to follow the given task
template = """
    You are to take the following content and parse it to return some data: {content}
    Make sure to follow these conditions:
    1. Extract only information that directly matches the prompt you will be given.
    2. Do not include extra commentary, text, comments, or explanations. Simply respond with a table containing the desired content if possible.
    3. If there isn't any information that matches the description/prompt, simply output an empty string ('') as a response.
    4. Only include data that is explicitly requested do not provide any additional information if not asked for. 
"""

model = OllamaLLM(model="llama3")

def ai_parse(chunks, prompt):
    system_prompt = ChatPromptTemplate.from_template(template)
    lchain = prompt | model # From LangChain module. 
    result = []
    for chunk in enumerate(chunks):
        response = lchain.invoke({"content": chunk, "parse_description": system_prompt})
        result.append(response)
    return "\n".join(result)