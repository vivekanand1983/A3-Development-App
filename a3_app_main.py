
import streamlit as st
from a3_utils import generate_response

st.set_page_config(page_title="Vivek A3 Assistant", layout="wide")
st.title("🧠 Vivek A3 Assistant")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.inputs = {}

steps = [
    ("6 o'clock position: Theme", "Enter the long-term theme (e.g., Digital Transformation)"),
    ("9 o'clock position: Annual Goal", "Enter the goal for this year (e.g., Build process-driven model)"),
    ("12 o'clock position: A3 Title", "Enter the focused A3 topic (e.g., Build roadmap for digitally-enabled ops)"),
    ("Background", "Let me generate the Background section based on your entries above."),
    ("Current Condition", "Would you like to proceed to the Current Condition section?"),
    ("Goal", "Now let’s define the measurable goals."),
    ("Analysis", "Let’s identify root causes behind the current issues."),
    ("Recommendations", "List down your proposed countermeasures or solutions."),
    ("Implementation Plan", "Outline your plan – Who will do What, When, and How."),
    ("Follow-up", "How will you ensure ongoing PDCA and learning?")
]

# Step-wise interaction
step_title, prompt = steps[st.session_state.step]
st.subheader(step_title)

if st.session_state.step < 3:
    user_input = st.text_area(prompt, height=100)
else:
    user_input = st.text_area(prompt, height=200)

if st.button("Next Step"):
    if user_input.strip() != "":
        st.session_state.inputs[step_title] = user_input
        st.session_state.step += 1

if st.session_state.step > 0:
    if st.button("Previous Step"):
        st.session_state.step -= 1

# Display collected inputs for review
with st.expander("📋 Review All Inputs"):
    for k, v in st.session_state.inputs.items():
        st.markdown(f"**{k}**")
        st.markdown(v)
