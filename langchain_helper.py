from langchain.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # Import LLMChain
from langchain.chains import SequentialChain


llm = HuggingFaceEndpoint(
    huggingfacehub_api_token="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",
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    model_kwargs={"max_length": 50},  # Specify valid model arguments here
    temperature=0.6
)




def generate_restaurant_name_and_items(cuisine):
    llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")
    prompt_template_name = PromptTemplate(
        input_variables=["Cuisine"],
        template="I want to open a restaurant for {Cuisine} food. Suggest a fancy name for this.",
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")


    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}. Return them as a comma-separated list.",
        )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu")
   

    # Define SequentialChain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["Cuisine"],  # Initial input for the first chain
        output_variables=["restaurant_name", "menu"],  # Final outputs
        return_all=True,  # Include intermediate outputs in the result
    )
    response = chain(cuisine)
    

    return response

if __name__=="__main__":
    print(generate_restaurant_name_and_items("italian"))
