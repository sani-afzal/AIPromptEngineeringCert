import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
# ChatPromptTemplate creates a sequence of chat messages with roles such as system, human, and ai.
from langchain_core.prompts import PromptTemplate
# PromptTemplate creates a single text prompt.
from langchain_core.output_parsers import StrOutputParser
#from langchain.chains import LLMChain

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("Please configure GROQ_API_KEY in your .env file.")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

faq_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful customer support assistant.

        Company FAQ:
        - Business hours: Monday-Friday, 9 AM-5 PM Pacific.
        - Returns: Items can be returned within 30 days of delivery.
        - Shipping: Standard shipping takes 3-5 business days.

        Answer using only the company information above.
        If the information is missing, say you don't know
        and recommend contacting customer support.
        Keep answers clear and concise."""
    ),
    ("human", "{question}"),
])

faq_chain = faq_prompt | llm | StrOutputParser()


def main():
    question = input("Enter a customer question: ")
    answer = faq_chain.invoke({"question": question})
    print("\nSupport response:", answer)

    # Step 1: Create the first prompt template to retrieve customer query details

    # Step 1: Create the first prompt template to retrieve customer query details
    first_prompt_template = PromptTemplate(
    input_variables=[question],
    template="Extract the key information from the following customer query: {question}"
    )
    formatted_prompt = first_prompt_template.format(question=question)
    print("This is the formatted prompt: ",formatted_prompt)
    answer1 = faq_chain.invoke({"question": formatted_prompt})
    print("answer1 ", answer1)
    extracted_info = str(answer1)
    # Step 2: Create the second prompt template to fetch order details based on extracted information
    second_prompt_template = PromptTemplate(
    input_variables=["extracted_info"],
    template="Using the extracted information: {extracted_info}, retrieve the relevant order details."
    )
    formatted_prompt2 = second_prompt_template.format(extracted_info=extracted_info)
    print("This is the formatted prompt2: ",formatted_prompt2)
    answer2 = faq_chain.invoke({"question": formatted_prompt2})
    print("answer2", answer2)
    order_details = str(answer2)

    # Step 3: Create the third prompt template to generate a detailed response for the customer
    third_prompt_template = PromptTemplate(
     input_variables=["order_details"],
     template="Based on the following order details: {order_details}, generate a detailed response to address the customer query."
    )
    formatted_prompt3 = third_prompt_template.format(order_details=order_details)
    print("This is the formatted prompt3: ",formatted_prompt3)
    answer3 = faq_chain.invoke({"question": formatted_prompt3})
    print("answer3", answer3)

    # Step 4: Define the chains
   # first_chain = LLMChain(llm=llm, prompt=first_prompt_template)
    first_chain = first_prompt_template | llm
    #second_chain = LLMChain(llm=llm, prompt=second_prompt_template)
    second_chain = second_prompt_template | llm
    #third_chain = LLMChain(llm=llm, prompt=third_prompt_template)
    third_chain = third_prompt_template | llm

    # Input to start the prompt chain (example customer query)
    #initial_input = "Can you help me with the status of my order #12345 placed last week?"

    initial_input = question

    # Run the first chain to extract key information from the query
    extracted_info = first_chain.invoke(initial_input)
    print("Extracted Info:", extracted_info)

    # Run the second chain to retrieve order details based on the extracted information
    order_details = second_chain.invoke(extracted_info)
    print("Order Details:", order_details)

    # Run the third chain to generate a detailed response based on the order details
    customer_response = third_chain.invoke(order_details)
    print("Customer Response:", customer_response)

if __name__ == "__main__":
    main()

#def main() -> None:
#    print("Hello from groq-support!")
# i placed my order on ulta but i want to return one of the product. 
# its mac lipstick shade red101. please help me. Order number is 1234

