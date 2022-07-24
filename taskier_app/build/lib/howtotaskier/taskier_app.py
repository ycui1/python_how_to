import streamlit as st
from taskier import Task, TaskierDBOption, set_db_option, TaskStatus, TaskierError
from taskier_app_helper import TaskierMenuOption, TaskierFilterKey


session = st.session_state

sidebar = st.sidebar
status_options = TaskStatus.formatted_options()
menu_key = "selected_menu_option"
working_task_key = "working_task"
sorting_params_key = "sorting_params"
sorting_orders = ["Ascending", "Descending"]
sorting_keys = {"Title": "title", "Description": "desc", "Urgency": "urgency", "Status": "status", "Note": "completion_note"}


def update_session_tracking(key, value):
    session[key] = value


def init_session():
    if menu_key not in session:
        update_session_tracking(menu_key, TaskierMenuOption.SHOW_TASKS.value)
        update_session_tracking(working_task_key, None)
        update_session_tracking(sorting_params_key, {x.value: None for x in TaskierFilterKey})


def show_tasks():
    filter_params = session[sorting_params_key]
    if filter_params[TaskierFilterKey.SORTING_KEY.value] is not None:
        reading_params = get_reading_params(filter_params)
        tasks = Task.load_tasks(**reading_params)
        sorting_key = sorting_keys[filter_params[TaskierFilterKey.SORTING_KEY.value]]
        should_reverse = filter_params[TaskierFilterKey.SORTING_ORDER.value] == sorting_orders[1]
        tasks.sort(key=lambda x: getattr(x, sorting_key), reverse=should_reverse)
    else:
        tasks = Task.load_tasks()
    
    for task in tasks:
        col1, col2 = st.columns([3, 1])
        col1.write(str(task))
        col2.button("View Detail", key=task.task_id, on_click=wants_task_detail, args=(task,))
        st.write(f"Status: {task.status.name.title()}")
        st.markdown("___")


def get_reading_params(filter_params):
    reading_params = dict.fromkeys(["statuses", "urgencies", "content"])
    if selected_statuses := filter_params[TaskierFilterKey.SELECTED_STATUSES.value]:
        reading_params["statuses"] = [status_options.index(x) for x in selected_statuses]
    if selected_urgencies := filter_params[TaskierFilterKey.SELECTED_URGENCIES.value]:
        reading_params["urgencies"] = selected_urgencies
    if selected_content := filter_params[TaskierFilterKey.SELECTED_CONTENT.value]:
        reading_params["content"] = selected_content
    return reading_params


def wants_task_detail(task: Task):
    update_session_tracking(working_task_key, task)
    update_session_tracking(menu_key, TaskierMenuOption.SHOW_TASK_DETAIL.value)


def show_task_detail():
    task = session[working_task_key]
    form = st.form("existing_task_form", clear_on_submit=False)

    form.title("Task Detail")

    task.title = form.text_input("The title", value=task.title, key="existing_task_title")

    task.desc = form.text_input("The description", value=task.desc, key="existing_task_desc")

    task.urgency = form.slider("The urgency level", min_value=1, max_value=5, value=task.urgency)

    status = form.selectbox("The status", index=task.status, options=status_options, key="existing_task_status")
    task.status = TaskStatus(status_options.index(status))

    task.completion_note = form.text_input("The completion note", value=task.completion_note, key="existing_task_note")

    submitted = form.form_submit_button("Update Task")
    if submitted:
        try:
            task.update_in_db()
        except TaskierError:
            form.error("Couldn't update the task as it's maybe deleted already.")
        else:
            session[working_task_key] = task
            form.success("Your Task Was Updated!")


def show_new_task_entry():
    with st.form("new_task_form", clear_on_submit=True):
        st.title("New Task")

        title = st.text_input("The title", key="new_task_title")

        desc = st.text_input("The description", key="new_task_desc")

        urgency = st.slider("The urgency level", min_value=1, max_value=5)

        submitted = st.form_submit_button("Save Task")
        if submitted:
            task = Task.task_from_form_entry(title, desc, urgency)
            task.save_to_db()
            st.success("Your Task Was Saved!")


def setup_filters():
    filter_params = session[sorting_params_key]
    with sidebar.expander("Sort and Filter", expanded=True):
        filter_params[TaskierFilterKey.SORTING_KEY.value] = st.selectbox("Sorted by", sorting_keys)
        filter_params[TaskierFilterKey.SORTING_ORDER.value] = st.radio("Sorting order", sorting_orders)
        filter_params[TaskierFilterKey.SELECTED_STATUSES.value] = st.multiselect("Show tasks with status (defaults to all)", options=status_options)
        filter_params[TaskierFilterKey.SELECTED_URGENCIES.value] = st.multiselect("Show tasks with urgency level (defaults to all)", options=range(1, 6))
        filter_params[TaskierFilterKey.SELECTED_CONTENT.value] = st.text_input("Show tasks with the content (defaults to all)")


def setup_deletion():
    task = session[working_task_key]
    text_title = sidebar.text_input("Enter task title to delete", key="existing_delete")
    submitted = sidebar.button("Delete Task")
    if submitted:
        if text_title == task.title:
            task.delete_from_db()
            sidebar.success("Your task has been deleted.")
        else:
            sidebar.error("You must enter the exact text for the title to delete.")


def setup_sidebar():
    sidebar.button("Show Tasks", on_click=update_session_tracking, args=(menu_key, TaskierMenuOption.SHOW_TASKS.value))

    sidebar.button("New Task", on_click=update_session_tracking, args=(menu_key, TaskierMenuOption.NEW_TASK.value))

    selected_db = sidebar.radio("Choose Database Option", [x.value for x in TaskierDBOption])
    set_db_option(selected_db)

    sidebar.button("Load Data to Database", on_click=Task.load_seed_data)

    sidebar.markdown("___")

    if session[menu_key] == TaskierMenuOption.SHOW_TASKS.value:
        setup_filters()
    elif session[menu_key] == TaskierMenuOption.SHOW_TASK_DETAIL.value:
        setup_deletion()


if __name__ == "__main__":
    init_session()
    setup_sidebar()
    if session[menu_key] == TaskierMenuOption.SHOW_TASKS.value:
        show_tasks()
    elif session[menu_key] == TaskierMenuOption.NEW_TASK.value:
        show_new_task_entry()
    elif session[menu_key] == TaskierMenuOption.SHOW_TASK_DETAIL.value:
        show_task_detail()
    else:
        st.write("No matching menu")
