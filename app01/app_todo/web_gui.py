import streamlit as st
import time

from modules import functions as fn

now = time.strftime("%a %d.%m.%Y, %H:%M")
task_list = fn.get_tasks()

st.title("My Tasks")
st.subheader(now)
st.text_input(label="Enter a new task:", label_visibility='collapsed', placeholder="Add new task...")
st.write("All my tasks:")

for task in task_list:
    st.checkbox(task)
