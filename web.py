import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

# set an index and item with enumerate
for index, todo in enumerate(todos):
    #set the checkbox with name and key of the each item
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #remove the item from the list
        todos.pop(index)
        #rewrite the todos
        functions.write_todos(todos)
        #delete the key from the session state dictionary
        del st.session_state[todo]
        # rerun the session
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')


# st.session_state