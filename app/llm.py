from app.schema import reasoning_output as ReasoningOutput
from langchain_core.output_parsers import PydanticOutputParser

from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V3.2",
        task="conversational",
        temperature=0.1,
        max_new_tokens=300
    )
llm = ChatHuggingFace(llm=llm)


parser = PydanticOutputParser(
    pydantic_object=ReasoningOutput
)
#llm = llm.with_structured_output(ReasoningOutput)