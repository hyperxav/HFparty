from party_planner import create_party_agent
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    print("Creating party planning agent...")
    agent = create_party_agent()
    
    print("\nPushing agent to Hugging Face Hub...")
    try:
        agent.push_to_hub('hyperxav/party-agent')
        print("✨ Successfully pushed agent to hyperxav/party-agent!")
        print("You can now access it at: https://huggingface.co/spaces/hyperxav/party-agent")
    except Exception as e:
        print(f"❌ Error pushing to Hugging Face Hub: {str(e)}")

if __name__ == "__main__":
    main() 