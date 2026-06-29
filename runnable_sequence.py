from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke: \n {text}",
    input_variables=['text']
)


chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

#chain = prompt1 | model | parser | prompt2 | model | parser    (Can use the LCEL syntax as well)

print(chain.invoke({'topic' : 'AI'}))