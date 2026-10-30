import ollama


def explain(action):

    prompt = f"""
You are AgentGate AI.

The rules engine has already classified this action.

Action:
{action}

Your task is NOT to change the classification.

Only explain:

1. Why this action may be considered safe or risky.
2. Any possible concerns.
3. Recommendation.

Keep response under 60 words.

Do not invent threats.
Do not call low-risk actions critical.
Stay consistent with the rules-engine output.
"""

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]