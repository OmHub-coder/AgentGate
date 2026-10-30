import streamlit as st

from security import analyze

from ai import explain

st.title("🛡 AgentGate")

st.subheader(
    "Security Checkpoint For AI Agents"
)

command = st.text_area(
    "Enter Agent Action"
)

if st.button("Analyze"):

    result = analyze(command)

    st.write(
        "Risk Level:",
        result["level"]
    )

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