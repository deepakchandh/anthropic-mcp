# from tools.paper_search import search_papers
# from tools.paper_extract import extract_info
#
# if __name__ == "__main__":
#     topic = "Geometry"
#     ids = search_papers(topic)
#     print("\n--- Sample Paper Info ---")
#     search_papers("Llm")
#     if ids:
#         paper_info = extract_info(ids[0])
#         print(paper_info)


import json
from tools.paper_search import search_papers
from tools.paper_extract import extract_info

# Tool function mapping
TOOL_MAP = {
    "search_papers": search_papers,
    "extract_info": extract_info
}

def handle_tool_call(tool_name: str, arguments: dict):
    """
    Dispatch tool call to the correct function.
    """
    if tool_name not in TOOL_MAP:
        raise ValueError(f"Tool '{tool_name}' not recognized.")

    func = TOOL_MAP[tool_name]
    return func(**arguments)

def chatbot_loop():
    """
    Basic chatbot loop to simulate input and tool usage.
    """
    print("Welcome to the Arxiv Assistant!")
    print("Available tools: search_papers, extract_info")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            break

        try:
            parsed = json.loads(user_input)  # Expecting {"tool": "name", "args": { ... }}
            tool_name = parsed["tool"]
            arguments = parsed.get("args", {})
            output = handle_tool_call(tool_name, arguments)
            print("Assistant:", output)
        except Exception as e:
            print(f"Error: {e}")
            print("Format: {\"tool\": \"search_papers\", \"args\": {\"topic\": \"AI\", \"max_results\": 3}}")

if __name__ == "__main__":
    chatbot_loop()

