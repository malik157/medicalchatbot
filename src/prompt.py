# what is the purpose of prompt.py file?
# Ans - The purpose of the prompt.py file is to define the system prompt that will be used by the language model (LLM) to generate responses based on the retrieved context. The system prompt provides instructions to the LLM on how to answer questions using the retrieved context, and it also sets guidelines for the response format, such as keeping the answer concise and limiting it to three sentences.

# what is prompt engineering?
# Ans - Prompt engineering is the process of designing and crafting prompts to effectively communicate with language models (LLMs) and guide their responses. It involves creating prompts that provide clear instructions, context, and constraints to elicit desired outputs from the LLM. Prompt engineering is crucial for optimizing the performance of LLMs in various applications, such as question-answering, text generation, and conversational agents.

system_prompt = (
    "You are an Medical assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
