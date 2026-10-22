from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional , Literal
from loadenv import dot_loadenv
from pydantic import BaseModel , EmailStr ,Field
dot_loadenv()

model = ChatOpenAI("")

class Review(BaseModel):
        key_themes: list[str] = Field(description="Write down all the key themes discussed in the review")
        pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
        cons: Optional[list[str]] = Field(default = None, description="Write down all the cons inside a list")
        summary: str = Field("A breif Summary of the review")
        sentiment: Literal["Positive" , "Negative" , "Neutral"] = Field(description="Return Sentiment of the review (negative , positive , neutral)")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" write text """)

print(result)