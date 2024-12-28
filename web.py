import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    # print(todo)
    todos.append(todo)
    functions.write_todos(todos, 'w')

st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("This app to increase your productivity!")

# st.checkbox("Buy grocery.")
# st.checkbox("Throw the trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        functions.write_todos(todos, 'w')
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo", placeholder="Add new Todo...", on_change=add_todo, key="new_todo")

# print("Hello")

# st.session_state