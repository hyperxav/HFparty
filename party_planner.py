from smolagents import CodeAgent, DuckDuckGoSearchTool, FinalAnswerTool, HfApiModel, Tool, tool, VisitWebpageTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

@tool
def catering_service_tool(query: str) -> str:
    """
    This tool returns the highest-rated catering service in Gotham City.
    
    Args:
        query: A search term for finding catering services.
    """
    # Example list of catering services and their ratings
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }
    
    # Find the highest rated catering service (simulating search query filtering)
    best_service = max(services, key=services.get)
    
    return best_service

class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = """
    This tool suggests creative superhero-themed party ideas based on a category.
    It returns a unique party theme idea."""
    
    inputs = {
        "category": {
            "type": "string",
            "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
        }
    }
    
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets."
        }
        
        return themes.get(category.lower(), "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.")

def create_party_agent():
    """Creates and returns a configured party planning agent with all available tools."""
    return CodeAgent(
        tools=[
            DuckDuckGoSearchTool(), 
            VisitWebpageTool(),
            suggest_menu,
            catering_service_tool,
            SuperheroPartyThemeTool()
        ], 
        model=HfApiModel(model="Qwen/Qwen2.5-Coder-32B-Instruct"),
        max_steps=10,
        verbosity_level=2
    )

def main():
    # Create the agent
    agent = create_party_agent()
    
    print("\nWelcome to Wayne Manor Party Planner!")
    print("-------------------------------------")
    
    # Example queries to demonstrate different tools
    queries = [
        "Give me the best playlist for a party at the Wayne's mansion. The party idea is a 'villain masquerade' theme",
        "What menu would be appropriate for a superhero themed party?",
        "Find the best catering service in Gotham City for a formal event",
        "Suggest a party theme for a 'classic heroes' category"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\nQuery {i}: {query}")
        print("-" * 80)
        result = agent.run(query)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main() 