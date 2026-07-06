import argparse
from agent.llm import LLMProvider
def main():
    parser = argparse.ArgumentParser(prog="agent", description="AI Knowledge Agent")
    subparsers = parser.add_subparsers(dest="command", required=True)
    ask_parser = subparsers.add_parser("ask", help="Ask the agent a question")
    ask_parser.add_argument("question", type=str, help="The question to ask")
    args = parser.parse_args()
    if args.command == "ask":
        provider = LLMProvider()
        print("Thinking...")
        try:
            answer = provider.ask(args.question)
            print(answer)
        except RuntimeError as error:
            print(f"Sorry, I couldn't get an answer: {error}")
if __name__ == "__main__":
    main()
