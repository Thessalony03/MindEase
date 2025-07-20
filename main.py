import os
from google.cloud import language_v1
from flask import jsonify, request, abort
import functions_framework

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bae254daae7ad6aea6caa9df731aaae96ad1df10" #nlp-key.json

@functions_framework.http
def sentiment(request):
    """Dialogflow CX Webhook for Sentiment Analysis"""

    try:
        request_json = request.get_json(force=True)
    except Exception as e:
        abort(400, description=f"Could not parse JSON: {str(e)}")

    text = request_json.get('text', {}).get('text', [""])[0]
    tag = request_json.get('fulfillmentInfo', {}).get('tag')

    if tag == "sentiment_analysis":
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(
            content=text,
            type_=language_v1.Document.Type.PLAIN_TEXT,
        )
        response = client.analyze_sentiment(request={"document": document})
        sentiment = response.document_sentiment
        score = sentiment.score
        magnitude = sentiment.magnitude

        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {"text": {"text": [f"Got it! (Score: {score:.2f}, Magnitude: {magnitude:.2f})"]}}
                ]
            },
            "sessionInfo": {
                "parameters": {
                    "sentiment_score": score,
                    "sentiment_magnitude": magnitude
                }
            }
        })

    else:
        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {"text": {"text": ["❗ Unknown tag for webhook."]}}
                ]
            }
        })
