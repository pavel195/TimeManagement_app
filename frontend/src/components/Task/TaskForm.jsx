
import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import { createTask } from '../../services/api';

function TaskForm({ onTaskAdded }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [dueDate, setDueDate] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createTask({ title, description, due_date: dueDate });
    setTitle('');
    setDescription('');
    setDueDate('');
    onTaskAdded();
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Название задачи"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <TextField
        label="Описание"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <TextField
        label="Дедлайн"
        type="date"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
        required
        fullWidth
        margin="normal"
        InputLabelProps={{
          shrink: true,
        }}
      />
      <Button type="submit" variant="contained" color="primary">
        Добавить задачу
      </Button>
    </form>
  );
}

export default TaskForm;
