from smolagents import CodeAgent, tool, HfApiModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

def main():
    # Alfred, the butler, preparing the menu for the party
    agent = CodeAgent(
        tools=[suggest_menu], 
        model=HfApiModel(model="Qwen/Qwen2.5-Coder-32B-Instruct")  # Using the same model as before
    )

    # Preparing the menu for the party
    result = agent.run("Prepare a formal menu for the party.")
    print("\nAlfred's Menu Suggestion:")
    print("------------------------")
    print(result)

if __name__ == "__main__":
    main() 