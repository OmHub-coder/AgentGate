import streamlit as st

import json

from security import analyze

from ai import explain

from logger import save_log

with st.sidebar:

    st.title("🛡 AgentGate")

    st.success("System Online")

    st.markdown("---")

    st.subheader("Recent Activity")

    try:

        with open(
            "logs.json",
            "r"
        ) as file:

            logs = json.load(file)

        for log in reversed(
            logs[-5:]
        ):

            st.write(
                f"""
                {log["decision"]}
                |
                {log["action"]}
                """
            )

    except:

        st.write(
            "No activity yet"
        )

st.title("🛡 AgentGate")

st.subheader(
    "Security Checkpoint For AI Agents"
)

command = st.text_area(
    "Enter Agent Action"
)

if st.button("Analyze"):

    result = analyze(command)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Risk Score",
            result["score"]
    )

    with col2:

        st.metric(
            "Threat Level",
            result["level"]
    )

    st.progress(
        min(result["score"], 100)
)

    save_log({
    "action": command,
    "score": result["score"],
    "level": result["level"],
    "decision": result["decision"]
})

    

    if result["decision"] == "ALLOW":

        st.success("✅ ALLOW")

    elif result["decision"] == "REVIEW":

        st.warning("⚠ REVIEW")

    else:

        st.error("🚫 BLOCK")

    st.subheader(
        "Threat Analysis"
    )

    for reason in result["reasons"]:

        st.write(
            f"• {reason}"
        )

    st.markdown("---")

    st.subheader(
        "🤖 AI Security Analysis"
    )

    with st.spinner(
        "Analyzing Security Risk..."
    ):

        analysis = explain(command)

    st.write(analysis)