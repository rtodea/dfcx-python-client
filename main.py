import google.cloud.dialogflowcx_v3 as dialogflow
import uuid


def detect_intent_text(project_id, location_id, agent_id, session_id, text):
    """Detects intent from text input and returns the response."""
    session_client = dialogflow.SessionsClient()
    session_path = session_client.session_path(
        project_id, location_id, agent_id, session_id
    )

    text_input = dialogflow.TextInput(text=text)
    query_input = dialogflow.QueryInput(text=text_input)

    request = dialogflow.DetectIntentRequest(
        session=session_path,
        query_input=query_input
    )

    response = session_client.detect_intent(request=request)

    print(f"Query text: {response.query_result.text}")
    print(f"Detected intent: {response.query_result.intent.display_name}")
    for param in response.query_result.parameters:
        print(f"{param.display_name}: {param.value}")
    print(f"Response: {response.query_result.response_messages[0].text.text[0]}")


def gen_session_id():
    return uuid.uuid4().hex


def run_agent_with_func_tools():
    # Example usage
    project_id = "your-project-id"
    location_id = "global"
    agent_id = "your-agent-id"

    session_id = gen_session_id()

    messages = [
        "Hello, I'd like to book a flight"
    ]

    for text in messages:
        detect_intent_text(project_id, location_id, agent_id, session_id, text)


if __name__ == '__main__':
    run_agent_with_func_tools()

