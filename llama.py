from langchain_groq import ChatGroq
#pip install -qU langchain-groq
question = "I am lost"
llm = ChatGroq(
    temperature = 0,
    groq_api_key = "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",
    model_name = "llama-3.1-70b-versatile"
)
response = llm.invoke("Are you gay: {}".format(question))
print(response.content)