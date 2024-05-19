import google.cloud.dialogflowcx_v3 as dialogflow
import uuid


def detect_intent_text(project_id, location_id, agent_id, session_id, text):
    """Detects intent from text input and returns the response."""
    session_client = dialogflow.SessionsClient()
    session_path = session_client.session_path(
        project_id, location_id, agent_id, session_id
    )

    text_input = dialogflow.TextInput(text=text)
    query_input = dialogflow.QueryInput(text=text_input, language_code="en")

    request = dialogflow.DetectIntentRequest(
        session=session_path,
        query_input=query_input
    )

    response = session_client.detect_intent(request=request)

    print(f"user says: {response.query_result.text}")
    print(f"agent says: {response.query_result.response_messages[0].text.text[0]}")


def gen_session_id():
    return uuid.uuid4().hex


def run_agent_with_func_tools():
    # Example usage
    project_id = "api-project-604594715070"
    location_id = "global"
    agent_id = "565978b6-f65a-4031-980a-441032ca038e"

    session_id = gen_session_id()

    messages = [
        "Hi! I want to buy a laptop.",
        "I want to ask for the temperature of a city like New York.",
        "New York",
        "Can tell me the New York city Temperature?"
    ]

    for text in messages:
        detect_intent_text(project_id, location_id, agent_id, session_id, text)


if __name__ == '__main__':
    run_agent_with_func_tools()

