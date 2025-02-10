from mira_sdk import MiraClient
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# flow = Flow(source="flow.yaml")
# try:
# 	client.flow.deploy(flow)
# except FlowError as e:
# 	print(f"Error occured: {str(e)}")

# input_dict={"topic": "NGO", "style": "Mother Teresa"}
# response=client.flow.test(flow, input_dict)
# print(response)

from mira_sdk import MiraClient, CompoundFlow

compound_flow = CompoundFlow(source="compound_flow.yaml")
try:
    client.flow.deploy(compound_flow)
except FlowError as e:
    print(f"Error occured: {str(e)}")

test_input = { # Prepare test inputs
    "Area_of_interest": "Education",
    "person_idolised": "APJ Abdul Kalam"
}

try:
    response = client.flow.test(compound_flow, test_input) # Test entire pipeline
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))

client.dataset.create("sohamthorat/nsshours", "Optional description")

client.dataset.add_source("sohamthorat/nsshours", url="https://www.planstreet.com/what-are-social-services-and-what-they-do")

client.dataset.add_source("sohamthorat/nsshours", url="https://nss.gov.in/nss-detail-page")

client.dataset.add_source("sohamthorat/nsshours", url="https://www.bajajfinserv.in/national-service-scheme")