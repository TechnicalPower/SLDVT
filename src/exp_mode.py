import sys
from workflows.basic_workflow.learn import Learn
from utils.data_generate import custom_flow_data_generate


def main():
     word = input("Currently in experimental mode... Could you tell me which word you want to teach for me?")
     custom_flow_data_generate(word)
     basic_learn = Learn()
     basic_learn.start_capture(word)

if __name__ == "__main__":
     main()
