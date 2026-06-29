from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Write a tweet about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Write a linkedin post about {topic}",
    input_variables=['topic']
)


parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})



result = parallel_chain.invoke({'topic' : 'AI'})

# print(result)

print(result['linkedin'])

print(result['tweet'])