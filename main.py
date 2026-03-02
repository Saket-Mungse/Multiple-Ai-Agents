# main.py

from pipeline import run_pipeline

def show_menu():
    print("\nSelect Agent:")
    print("1 - Career")
    print("2 - Diet")
    print("3 - Summary")
    print("4 - Coding")
    print("5 - Prompt Generation")


def main():
    show_menu()

    choice = input("Enter choice number: ")

    agent_map = {
        "1": "career",
        "2": "diet",
        "3": "summary",
        "4": "coding",
        "5": "prompt"
    }

    agent_type = agent_map.get(choice)

    if not agent_type:
        print("Invalid choice")
        return

    question = input("Ask your question: ")

    result = run_pipeline(agent_type, question)

    print("\nResponse:\n")
    print(result)


if __name__ == "__main__":
    main()