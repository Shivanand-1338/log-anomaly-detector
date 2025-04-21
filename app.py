import streamlit as st
import time

st.set_page_config(page_title="Log Viewer", layout="wide")
st.title("📄 Real-Time Log Viewer")

log_file = "logs.txt"

# Auto-refresh every 5 seconds
refresh_interval = 5
st.caption(f"⏳ Refreshes every {refresh_interval} seconds")

# Button to trigger manual refresh
if st.button("🔄 Refresh now"):
    st.experimental_rerun()

# Display the logs
try:
    with open(log_file, "r") as f:
        logs = f.readlines()
        logs = logs[-100:]  # show only last 100 lines

        for line in logs:
            if any(level in line for level in ["ERROR", "CRITICAL", "FATAL", "ALERT"]):
                st.error(line.strip())
            else:
                st.text(line.strip())
except FileNotFoundError:
    st.warning(f"No log file found at: `{log_file}`")

# Auto-refresh
time.sleep(refresh_interval)
st.experimental_rerun()
