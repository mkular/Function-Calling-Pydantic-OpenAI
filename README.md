# Function-Calling-Pydantic-OpenAI
Getting structured output from OpenAI using pydantic function calling

In order to program/code upon data obtained from LLMs, it needs to be in a structured format. Pydantic offers an easy solution to this by incorporating function calling.
This example shows that when OpenAI GPT-4o is asked: "Give me ten of the best non-fiction books of all time", it answers in the following format:
```python
title: str = Field(..., description="""title of the book in title case""")
summary: str = Field(..., description="""a brief but informative summary of the entire book
                         describing the context and theme in about 300 tokens""")
author: str = Field(..., description="""name of the author in last name, first name format
                        like Dickens, Charles""")
year_published: int = Field(..., description="""year this boook was published""")
```
After installing the requirements via:
<pre>pip install -r requirements.txt</pre>

Export the OPEN_API_KEY via:
<pre>export OPEN_API_KEY="your actual openai api key"</pre>

Run the program as:
<pre>python pydantic_ex.py</pre>

Notice that in the output structure of the result is in-line with the format given:

```
024-10-05 01:05:11.720 | INFO     | __main__:<module>:32 - Book No. 0
2024-10-05 01:05:11.721 | INFO     | __main__:<module>:33 - title='The Immortal Life of Henrietta Lacks' summary="This compelling book by Rebecca Skloot delves into the life of Henrietta Lacks, a poor African-American woman whose cancer cells were taken without her knowledge in 1951. These cells, known as HeLa, became one of the most important tools in medicine, contributing to numerous scientific breakthroughs. Skloot explores issues of medical ethics, racism, and the impact of scientific research on human lives. She intertwines the scientific aspects with a narrative of Lacks' family, uncovering the injustices they faced and the legacy of Henrietta's immortal cells." author='Skloot, Rebecca' year_published=2010
2024-10-05 01:05:12.867 | INFO     | __main__:<module>:32 - Book No. 1
2024-10-05 01:05:12.867 | INFO     | __main__:<module>:33 - title='Sapiens: A Brief History of Humankind' summary="Yuval Noah Hariri's 'Sapiens' explores the history of humankind from the Stone Age to the present, focusing on how Homo sapiens came to dominate the world. Harari examines the roles of biology, history, and culture in shaping human societies, highlighting the cognitive, agricultural, and scientific revolutions. He challenges traditional beliefs and suggests how future technological advancements might shape humanity. The book offers a panoramic view of human history, making complex ideas accessible and thought-provoking." author='Harari, Yuval Noah' year_published=2011
2024-10-05 01:05:13.931 | INFO     | __main__:<module>:32 - Book No. 2
2024-10-05 01:05:13.932 | INFO     | __main__:<module>:33 - title='Educated' summary="Tara Westover's memoir 'Educated' recounts her journey from growing up in a strict and abusive household in rural Idaho, with no formal education, to earning a Ph.D. from Cambridge University. The book details her struggle for self-invention and highlights the power of education to transform a life. Westover's story is one of resilience and determination, shedding light on the impact of family dynamics, mental illness, and self-discovery." author='Westover, Tara' year_published=2018
2024-10-05 01:05:14.901 | INFO     | __main__:<module>:32 - Book No. 3
2024-10-05 01:05:14.902 | INFO     | __main__:<module>:33 - title='The Diary of a Young Girl' summary="Anne Frank's 'The Diary of a Young Girl' is a poignant and powerful account of her life in hiding during the Nazi occupation of the Netherlands. Written between 1942 and 1944, this diary provides a glimpse into the thoughts and experiences of a young Jewish girl as she, her family, and others lived in secret. Her reflections on humanity, nature, and hope stand as a testament to the resilience of the human spirit amidst the horrors of war." author='Frank, Anne' year_published=1947
2024-10-05 01:05:16.127 | INFO     | __main__:<module>:32 - Book No. 4
2024-10-05 01:05:16.127 | INFO     | __main__:<module>:33 - title='In Cold Blood' summary="Truman Capote's 'In Cold Blood' is a groundbreaking work of true crime, telling the story of the 1959 murder of the Clutter family in Holcomb, Kansas. Capote meticulously reconstructs the events surrounding the crime, offering insights into the minds of the perpetrators and the impact on the community. Through exhaustive research, Capote creates a narrative that reads like fiction while raising questions about justice, psychology, and the nature of evil." author='Capote, Truman' year_published=1965
2024-10-05 01:05:17.097 | INFO     | __main__:<module>:32 - Book No. 5
2024-10-05 01:05:17.097 | INFO     | __main__:<module>:33 - title='The Wright Brothers' summary="David McCullough's 'The Wright Brothers' presents the lives of Orville and Wilbur Wright, who changed history with their invention of the first successful powered airplane. Based on thorough research, including the Wright brothers' personal diaries and letters, McCullough chronicles their determination, innovation, and the challenges they overcame. The book captures the spirit of invention and the profound impact of their achievements on the world." author='McCullough, David' year_published=2015
2024-10-05 01:05:19.260 | INFO     | __main__:<module>:32 - Book No. 6
2024-10-05 01:05:19.260 | INFO     | __main__:<module>:33 - title='The Selfish Gene' summary="Richard Dawkins' 'The Selfish Gene' revolutionized the understanding of evolutionary biology by introducing the concept of genes as the primary unit of selection. Published in 1976, the book explores the idea that genes 'compete' for survival, driving evolution through natural selection. Dawkins' clear and engaging writing presents complex genetic ideas, influencing both scientific thought and popular understanding of evolution. It sparks debates on altruism, cooperation, and cultural evolution." author='Dawkins, Richard' year_published=1976
2024-10-05 01:05:20.338 | INFO     | __main__:<module>:32 - Book No. 7
2024-10-05 01:05:20.338 | INFO     | __main__:<module>:33 - title='The Power Broker' summary="Robert Caro's 'The Power Broker: Robert Moses and the Fall of New York' is a comprehensive biography of Robert Moses, the influential urban planner behind much of New York City's mid-20th century development. Caro investigates how Moses wielded power to shape the city and its suburbs, often at great social cost. Through exhaustive research, Caro unveils the complexities of urban planning, politics, and the ways individuals can manipulate systems to achieve their vision, for better or worse." author='Caro, Robert' year_published=1974
2024-10-05 01:05:21.227 | INFO     | __main__:<module>:32 - Book No. 8
2024-10-05 01:05:21.228 | INFO     | __main__:<module>:33 - title='The Origin of Species' summary="Charles Darwin's seminal work, 'The Origin of Species,' published in 1859, introduced the theory of evolution by natural selection, a groundbreaking concept that transformed biological science. Darwin meticulously details the process by which species evolve over time through environmental pressures. His observations and arguments laid the foundation for modern evolutionary biology and sparked discussions that continue in scientific and philosophical realms today." author='Darwin, Charles' year_published=1859
2024-10-05 01:05:22.236 | INFO     | __main__:<module>:32 - Book No. 9
2024-10-05 01:05:22.236 | INFO     | __main__:<module>:33 - title='Guns, Germs, and Steel' summary="Jared Diamond's 'Guns, Germs, and Steel: The Fates of Human Societies' investigates the factors that led to the unequal distribution of wealth and power across civilizations. Diamond argues that environmental factors, rather than inherent differences among people, shaped the modern world. By examining agriculture, geography, and technology, he provides insights into human development and challenges the notion of racial superiority. The book is a comprehensive exploration of why history unfolded differently across continents." author='Diamond, Jared' year_published=1997
```
