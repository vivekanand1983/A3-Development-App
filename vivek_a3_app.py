
import streamlit as st

# Title
st.title("A3 Development Assistant")

# Step-by-step guided A3 input
steps = [
    "6 o'clock Position: Theme / Long-term Direction",
    "9 o'clock Position: Annual Objective",
    "12 o'clock Position: A3 Topic",
    "Background",
    "Current Condition",
    "Goal",
    "Root Cause Analysis",
    "Recommendations",
    "Implementation Plan (4W1H)",
    "Follow-up & PDCA"
]

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0

# Navigation
def next_step():
    if st.session_state.step < len(steps) - 1:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

# Display current step
st.header(steps[st.session_state.step])
user_input = st.text_area("Enter your input below:", key=steps[st.session_state.step])

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        prev_step()
with col2:
    if st.button("Next"):
        next_step()
