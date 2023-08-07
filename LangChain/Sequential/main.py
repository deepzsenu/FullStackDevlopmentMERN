import streamlit as st
from secret import API_KEY
import os
import openai
from langchain.llms import OpenAI
from langchain.chains import SequentialChain, LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate

st.markdown("""
<h1 style = "color:red;text_align: center;">This is a Simple Sequential Chain Demo<h1>          
""",
    unsafe_allow_html=True,)

user_question = st.text_input(
    "Enter a Question",
    value="What is the capital of delhi?"
)

llm  = OpenAI(openai_api_key=API_KEY, temperature=0.3)

if st.button("Tell me about it ", key="primary"):
    # Chain 1
    template = "{Question}\n\n"
    prompt_template1 = PromptTemplate(template = template, input_variables=["Question"])
    st.subheader("Chain1", "")
    question_chain = LLMChain(prompt=prompt_template1, llm=llm)
    st.info(question_chain.run(user_question))

    # Chain 2

    template = """
        Here is a statement
        {Statement}
        Make Bullet point Assumptions based on the above statement that are correct """
    prompt_template2 = PromptTemplate(template = template, input_variables=["Statement"])
    assumption_chain = LLMChain(prompt=prompt_template2, llm=llm)
    st.subheader("Chain2")
    assumption_chain_sequential =  SimpleSequentialChain(
        chains=[question_chain, assumption_chain],
        verbose=True
    )
    st.info(assumption_chain_sequential.run(user_question))

    # chain3

    template = """
        Here is a bullet point Assertion
        {Assertion}
        Based on the assertion mark True or false if it is True explain why if not explain why"""

    assertion_prompt = PromptTemplate(template=template, input_variables=["Assertion"])
    Assertion_chai = LLMChain(prompt=assertion_prompt, llm=llm)
    Assertion_chai_Seq = SimpleSequentialChain(
        chains=[question_chain, assumption_chain, Assertion_chai],
        verbose=True
    )
    st.subheader("Chain3")
    st.info(Assertion_chai_Seq.run(user_question))

    # Final chain
    st.header("Final Chain")
    template = """
        In light of the above facts how would you answer the question{}, user_questions
        """
    template = "{Answer}/n/n"
    final_prompt = PromptTemplate(template=template, input_variables=["Answer"])
    final_chain = LLMChain(prompt=final_prompt,llm=llm)
    final_chain_seq = SimpleSequentialChain(
        chains = [question_chain, assumption_chain,Assertion_chai , final_chain],
        verbose=True
    )

    st.info(final_chain_seq.run(user_question))

    st.subheader("Thanks for using the application")