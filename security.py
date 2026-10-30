from rules import BLOCKED_WORDS
from rules import SENSITIVE_WORDS


def analyze(command):

    command = command.lower()

    score = 0

    reasons = []

    for word in BLOCKED_WORDS:

        if word in command:

            score += 70

            reasons.append(
                f"Dangerous keyword detected: {word}"
            )

    for word in SENSITIVE_WORDS:

        if word in command:

            score += 30

            reasons.append(
                f"Sensitive keyword detected: {word}"
            )

    if score >= 70:

        decision = "BLOCK"

    elif score >= 30:

        decision = "REVIEW"

    else:

        decision = "ALLOW"

    return {
        "score": score,
        "decision": decision,
        "reasons": reasons
    }