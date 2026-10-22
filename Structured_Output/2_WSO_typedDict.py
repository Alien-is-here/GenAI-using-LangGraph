from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional , Literal
from loadenv import dot_loadenv

dot_loadenv()

model = ChatOpenAI("")

class Review(TypedDict):
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    summary : Annotated[str, "A breif Summary of the review"]
    sentiment : Annotated[Literal["Positive" , "Negative" , "Neutral"], "Return Sentiment of the review (negative , positive , neutral)"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" write text """)

print(result)