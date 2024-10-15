import React, { useReducer, useState } from 'react';
import './TodoApp.css'; 

const todoreducer = (tasks, action) => {
  switch(action.type) {
    case 'ADD_ITEM':
      return [...tasks, { 
        id: Date.now(), 
        title: action.titleInput, 
        name: action.taskInput, 
        dateTime: action.dateTime, 
        completed: false 
      }];
    
    case 'REMOVE_ITEM':
      return tasks.filter(task => task.id !== action.id);
    
    case 'TOGGLE_COMPLETE':
      return tasks.map(task => 
        task.id === action.id ? { ...task, completed: !task.completed } : task
      );

    case 'EDIT_ITEM':
      return tasks.map(task =>
        task.id === action.id 
          ? { ...task, title: action.newTitle, name: action.newName, dateTime: action.newDateTime }
          : task
      );

    default:
      return tasks;
  }
};

const TodoApp = () => {

  const [tasks, dispatch] = useReducer(todoreducer, []);

  const [titleInput, setTitleInput] = useState('');
  const [taskInput, setTaskInput] = useState('');
  const [dateTimeInput, setDateTimeInput] = useState('');
  const [editMode, setEditMode] = useState(null);

  const addTask = (e) => {
    e.preventDefault();

    if (taskInput && dateTimeInput && titleInput) {
      dispatch({
        type: 'ADD_ITEM',
        titleInput: titleInput,
        taskInput: taskInput,
        dateTime: dateTimeInput,
      });
      setTitleInput('');
      setTaskInput('');
      setDateTimeInput('');
    }
  };

  const deleteTask = (id) => {
    dispatch({ type: 'REMOVE_ITEM', id: id });
  };

  const toggleCompleted = (id) => {
    dispatch({ type: 'TOGGLE_COMPLETE', id: id });
  };

  const editTask = (task) => {
    setEditMode(task.id);
    setTitleInput(task.title);
    setTaskInput(task.name);
    setDateTimeInput(task.dateTime);
  };

  const saveEditedTask = (e) => {
    e.preventDefault();

    dispatch({
      type: 'EDIT_ITEM',
      id: editMode,
      newTitle: titleInput,
      newName: taskInput,
      newDateTime: dateTimeInput
    });

    setEditMode(null);
    setTitleInput('');
    setTaskInput('');
    setDateTimeInput('');
  };

  return (
    <div className="todo-app">
      <h1>To-Do App</h1>

      <form className="input-group" onSubmit={editMode ? saveEditedTask : addTask}>
        <input
          type="text"
          value={titleInput}
          onChange={(e) => setTitleInput(e.target.value)}
          placeholder="Title"
          required
        />
        <input
          type="text"
          value={taskInput}
          onChange={(e) => setTaskInput(e.target.value)}
          placeholder="Add something to your list"
          required
        />
        <input
          type="datetime-local"
          value={dateTimeInput}
          onChange={(e) => setDateTimeInput(e.target.value)}
          required
        />
        <button type="submit" className="btn add-task-btn">
          {editMode ? 'Save' : 'Add'}
        </button>
      </form>

      <ul id="taskList">
        {tasks.map(task => (
          <li key={task.id} className={task.completed ? 'completed' : ''}>
            <h3>{task.title}</h3>
            <p>{task.name}</p>
            <span>{new Date(task.dateTime).toLocaleString()}</span>
            <button onClick={() => toggleCompleted(task.id)}>
              {task.completed ? 'Undo' : 'Complete'}
            </button>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
            <button onClick={() => editTask(task)}>Edit</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
