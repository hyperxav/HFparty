# HFParty

A simple demonstration of using the `smolagents` library with Hugging Face models to create an AI agent that can search and provide recommendations.

## Features

- Uses the Hugging Face Inference API
- Implements DuckDuckGo search capability
- Can provide party recommendations and answer questions
- Menu suggestion system with Alfred the butler
  - Supports different types of occasions (casual, formal, superhero)
  - Custom menu recommendations

## Setup

1. Clone the repository
```bash
git clone https://github.com/hyperxav/HFparty.git
cd HFparty
```

2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.template .env
```
Then edit the `.env` file and add your Hugging Face API token. You can get your token from [Hugging Face Settings](https://huggingface.co/settings/tokens).

4. Run the agents

For music recommendations:
```bash
python test_agent.py
```

For menu suggestions with Alfred the butler:
```bash
python menu_agent.py
```

## Examples

### Menu Suggestions

The menu agent supports different types of occasions:
- Casual parties: Pizza, snacks, and drinks
- Formal events: 3-course dinner with wine and dessert
- Superhero parties: High-energy and healthy food buffet
- Custom occasions: Personalized menu recommendations

## Requirements

See `requirements.txt` for the full list of dependencies.

## License

MIT License 