import streamlit as st

from security import analyze

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
    result["level"])
    

    if result["decision"] == "ALLOW":
        st.success("✅ ALLOW")

    elif result["decision"] == "REVIEW":
        st.warning("⚠ REVIEW")

    else:
        st.error("🚫 BLOCK")

    st.write(
        result["reasons"]
    )