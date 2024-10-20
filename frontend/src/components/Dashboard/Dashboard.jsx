
import React, { useState, useEffect } from 'react';
import TaskList from '../Task/TaskList';
import TaskForm from '../Task/TaskForm';
import DeadlineChart from '../Chart/DeadlineChart';
import { getTasks } from '../../services/api';

function Dashboard() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const response = await getTasks();
    setTasks(response.data);
  };

  return (
    <div>
      <TaskForm onTaskAdded={fetchTasks} />
      <TaskList tasks={tasks} />
      <DeadlineChart tasks={tasks} />
    </div>
  );
}

export default Dashboard;
