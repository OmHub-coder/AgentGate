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
    st.code("""
delete all files

email password database

access bank credentials

create pdf report

backup user data

shutdown server
""")

    try:

        with open(
            "logs.json",
            "r"
        ) as file:

            logs = json.load(file)

        total_logs = len(logs)

        blocked_count = sum(
            1 for log in logs
            if log["decision"] == "BLOCK"
        )

        review_count = sum(
            1 for log in logs
            if log["decision"] == "REVIEW"
        )

        allow_count = sum(
            1 for log in logs
            if log["decision"] == "ALLOW"
        )

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

a, b, c, d = st.columns(4)

with a:
    st.metric(
        "Total Actions",
        total_logs
    )

with b:
    st.metric(
        "Blocked",
        blocked_count
    )

with c:
    st.metric(
        "Review",
        review_count
    )

with d:
    st.metric(
        "Allowed",
        allow_count
    )

st.markdown("---")
command = st.text_area(
    "Enter Agent Action"
)

if st.button("Analyze"):

    result = analyze(command)

    col1, col2, col3 = st.columns(3)

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

    with col3:

        st.metric(
            "Category",
            result["category"]
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

    st.markdown("---")

    st.subheader(
        "📋 Executive Summary"
    )

    st.info(
        f"""
    Decision: {result['decision']}

    Threat Level: {result['level']}

    Category: {result['category']}
    """
    )