from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from langchain_openai import OpenAI

def query_agent(data, query):

    # Parse the CSV file and create a dataframe from its contents.
    df = pd.read_csv(data)

    llm = OpenAI()

    # Create a pandas dataframe agent
    agent = create_pandas_dataframe_agent(llm, df, verbose=True,allow_dangerous_code=True)

    response = agent.run(query)

    return response