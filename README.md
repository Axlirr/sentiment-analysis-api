# Sentiment Analysis API

A modern sentiment analysis API that can analyze text emotions in real-time using state-of-the-art transformer models. This project provides both a REST API and a web interface for easy interaction.

## Features

- Real-time sentiment analysis of text
- Support for multiple languages
- Pre-trained transformer model using BERT
- Simple REST API
- Clean web interface
- Docker support for easy deployment

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Axlirr/sentiment-analysis-api.git
cd sentiment-analysis-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## API Usage

Send POST requests to `/api/analyze` with JSON data:

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this project!"}'
```

Response format:
```json
{
  "text": "I love this project!",
  "sentiment": "positive",
  "confidence": 0.95,
  "emotions": {
    "joy": 0.8,
    "sadness": 0.05,
    "anger": 0.02,
    "fear": 0.03,
    "neutral": 0.1
  }
}
```

## Technical Details

- Backend: Python with FastAPI
- ML Model: Hugging Face Transformers (BERT-based)
- Frontend: HTML/CSS/JavaScript with Bootstrap
- Containerization: Docker

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- FastAPI
- Uvicorn
- See requirements.txt for full list

## License

MIT License - feel free to use this project for any purpose.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.