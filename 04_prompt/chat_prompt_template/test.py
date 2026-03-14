from langchain_core.prompts import ChatPromptTemplate

chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个{role}"),
        ('human', '1+1=?'),
        ('ai', '1+2=3')
    ]
)

prompt = chatPromptTemplate.format_messages(role='数学家')
print(prompt)



chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你是{role}"),
        ("human","回答我问题：{question}")
    ]
)

prompt_value3 = chat_prompt.format(**{"role": "python开发工程师", "question": "快速排序怎么写"})
print(prompt_value3)

prompt_value2 = chat_prompt.invoke({"role": "python开发工程师", "question": "快速排序怎么写"})
print(prompt_value2)

prompt_value1 = chat_prompt.format_messages(**{"role": "python开发工程师", "question": "快速排序怎么写"})
print(prompt_value1)