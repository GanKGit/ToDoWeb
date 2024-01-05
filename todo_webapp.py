import file_io
import streamlit as st

todos_list=file_io.readToDoFile()


def add_todo():
    new_item = st.session_state['new_item']
    todos_list.append(new_item)
    file_io.writeToDoFile(todos_list)
    st.session_state['new_item'] = ""


st.title("Todo Organiser")
st.write("Manage your todos...")
for index, todo in enumerate(todos_list):
    check_box=st.checkbox(todo, key=todo + str(index))
    if check_box:
        todos_list.pop(index)
        file_io.writeToDoFile(todos_list)
        del st.session_state[todo + str(index)]
        st.rerun()

st.text_input("Enter a todo", on_change=add_todo, key='new_item')

