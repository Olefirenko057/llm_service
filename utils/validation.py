import json

# Validates the format and structure of incoming messages from ActiveMQ.
def validate_message(message):
    try:
        data = json.loads(message)
        if "filePath" not in data or "lessonId" not in data:
            return None
        return data
    except json.JSONDecodeError:
        return None