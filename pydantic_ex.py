import instructor
import os
from openai import OpenAI
from pydantic import BaseModel, Field
from loguru import logger

api_key = os.environ["OPEN_API_KEY"]

class books(BaseModel):
    title: str = Field(..., description="""title of the book in title case""")
    summary: str = Field(..., description="""a brief but informative summary of the entire book
                         describing the context and theme in about 300 tokens""")
    author: str = Field(..., description="""name of the author in last name, first name format
                        like Dickens, Charles""")
    year_published: int = Field(..., description="""year this boook was published""")

client = instructor.from_openai(OpenAI(api_key=api_key))

if __name__ == "__main__":
    completion = client.chat.completions.create_iterable(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "Give me ten of the best non-fiction books of all time"
            }
        ],
        response_model=books
    )

    for i, book in enumerate(completion):
        logger.info(f"Book No. {i}")
        logger.info(book)
