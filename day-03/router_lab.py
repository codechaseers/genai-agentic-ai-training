
utterance = input("Enter your query: ")

from json_lab import classify

def answer_faq(utterance):
    return "If your UPI transaction failed, please check the transaction status."
print(answer_faq(utterance))

# mock  api function    
def call_mock_api(intent, entities):
    return {
        "status": "ok",
        "action": "card_hotlisted",
        "ref": "HTL-1029"
    }
# escalate 
def escalate(utterance, result):
    return {
        "reason": "Low confidence",
        "intent": result["intent"],
        "entities": result.get("entities", {}),
        "summary_for_agent": utterance
    }

def route(utterance):

    result = classify(utterance)

    if result["confidence"] < 0.6:
        return escalate(utterance, result)

    if result["intent"] == "out_of_scope":
        return escalate(utterance, result)

    if result["intent"] == "small_talk":
        return "Hello! How can I help you?"

    if result["intent"] in {
        "balance_enquiry",
        "card_hotlist",
        "statement_request"
    }:
        return call_mock_api(
            result["intent"],
            result.get("entities", {})
        )

    if result["intent"] == "upi_issue":
        return answer_faq(utterance)

    return escalate(utterance, result)


# print("sudhanshu")

