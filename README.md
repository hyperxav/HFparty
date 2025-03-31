# HFParty

A comprehensive party planning system using the `smolagents` library with Hugging Face models to create an AI agent that can handle various aspects of party planning at Wayne Manor.

## Features

- Uses the Hugging Face Inference API
- Comprehensive party planning tools:
  - Music recommendations with DuckDuckGo search
  - Menu suggestion system with Alfred the butler
  - Superhero party theme generator
  - Gotham City catering service finder
  - Web page content analysis
- Multiple party themes supported:
  - Classic heroes
  - Villain masquerade
  - Futuristic Gotham
  - Custom themes
- Menu types for different occasions:
  - Casual parties
  - Formal events
  - Superhero gatherings
  - Custom menus

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

4. Run the party planner
```bash
python party_planner.py
```

## Examples

### Party Themes

The party planner supports various superhero themes:
- Classic Heroes: Justice League Gala with themed cocktails
- Villain Masquerade: Gotham Rogues' Ball
- Futuristic Gotham: Neo-Gotham Night with cyberpunk style

### Menu Suggestions

Different menu types available:
- Casual parties: Pizza, snacks, and drinks
- Formal events: 3-course dinner with wine and dessert
- Superhero parties: High-energy and healthy food buffet
- Custom occasions: Personalized menu recommendations

### Catering Services

Integrated with Gotham City's top catering services:
- Gotham Catering Co.
- Wayne Manor Catering
- Gotham City Events

## Requirements

See `requirements.txt` for the full list of dependencies.

## License

MIT License 