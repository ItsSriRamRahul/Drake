import subprocess
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os 
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI


class AIAgent:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4")

    def run_code(self,lang,filename,inputs=None):
        
        cmdline=subprocess.run([lang,filename],text=True,capture_output=True,input=inputs)
        if cmdline.returncode != 0:
            return cmdline.stderr
        else:
            return cmdline.stdout
    def gen_code(self,query,):
        chunks = []
        for chunk in self.model.stream(query):
            chunks.append(chunk)
            print(chunk.content, end="", flush=True)
    def rectify(self):
        None
agent=AIAgent()
agent.gen_code("what is difference between saturn and neptune?")
