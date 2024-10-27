from flask import Flask, request, jsonify
from flask_cors import CORS
from webscrape import scrape, extract_body, clean_content, batch_maker
from ai_parser import ai_parse

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from React frontend

@app.route('/scrape', methods=['POST'])
def scrape_website():
    data = request.json
    website_url = data.get('url')
    prompt = data.get('prompt')

    # Scrape website
    raw_html = scrape(website_url)
    body = extract_body(raw_html)
    cleaned_text = clean_content(body)

    # Split into batches and parse with AI
    chunks = batch_maker(cleaned_text, 6000)  # 6000 token limit per chunk
    result = ai_parse(chunks, prompt)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5000)