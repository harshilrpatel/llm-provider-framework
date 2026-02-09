"""
Test all models to come up with a question and evaluate the response from all the models and rank them. 
"""

import json
from typing import Dict, List
from dotenv import load_dotenv
from ProviderFactory import create_provider
import random

#Load environment variable
load_dotenv(override=True)

def ask_question(llm_provider, messages:List[Dict[str, str]])->str:
    """ 
    Return response from LLM Provider 

    Args:
        llm_provider : LLMProvider to use 
        messages: List of message dictionaries
    
    Return:
        Generated response from LLMProvider
    """
    #Initialize Provider
    provider = create_provider(llm_provider)

    #Ask the Provider to generate response to our question
    response = provider.generate_response(messages)

    return response



def main():

    #Create a prompt for LLMs to generate a question to test their own intelligence. 

    messages = [{
        "role" : "user",
        "content" : "Please come up with a challenging, nuanced question that I can ask number of LLMs to evaluate their intelligence. Answer only with the question, no explanation."
    }]

    #Models
    models = ["Gemini", "OpenAI", "Claude"]

    #Randomly pick any model
    model = random.choice(models)
    print(f"Just so humans are aware, random model picked was : {model}. \n")

    #Invoke ask_question to get generate the question to test each models using a random model picked earlier.
    question = ask_question(model, messages)

    #Print the question 
    print(f"Question for evalution is : \n {question}")

    #Ask each models to respond to the question
    answers_by_each_models = []
    for model in models:
        answers_by_each_models.append(ask_question(model, [{
            "role":"user",
            "content": question
        }]))

    #What did all models responded with
    for model, answer in zip(models, answers_by_each_models):
        print(f"\n\nResponse from {model} is : {answer}")

    #Lets pick a random model to evaluate the responses from all the LLM models
    evaluator = random.choice(models)

    print(f"Just so humans are aware, random model picked was : {evaluator}. \n")

    #Make a prompt to judge the responses
    
    judge = f"""
    You are judging a competition between {len(models)} competitors.
    Each model has been given this question:

    {question}

    Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
    Respond with JSON, and only JSON, with the following format:
    {{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

    Here are the responses from each competitor in form of a list following format:
    ["Response from competitor 1", "Response from competitor 2", ...]

    {answers_by_each_models}

    Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks.
    """

    #Generate Judge Messages
    judge_messages = [{"role":"user", "content": judge}]

    #Ask random model evaludate the responses
    results = ask_question(evaluator, judge_messages)

    #Display results
    results_dict = json.loads(results)
    ranks = results_dict["results"]
    print("\n")
    for index, result in enumerate(ranks):
        competitor = models[int(result)-1]
        print(f"Rank {index+1}: {competitor}")

if __name__ == "__main__":
    main()
    
