// frontend/src/components/Task/TaskForm.jsx

import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';
import { createTask } from '../../services/api';

function TaskForm({ onTaskAdded }) {
  // Состояния для полей формы
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [dueDate, setDueDate] = useState('');

  // Обработчик отправки формы
  const handleSubmit = async (e) => {
    e.preventDefault(); // Предотвращаем стандартное поведение формы

    // Формируем объект задачи
    const newTask = {
      title,
      description,
      due_date: dueDate
    };

    try {
      // Отправляем POST-запрос на создание задачи
      await createTask(newTask);

      // Очищаем поля формы
      setTitle('');
      setDescription('');
      setDueDate('');

      // Вызываем функцию обновления списка задач
      onTaskAdded();
    } catch (error) {
      console.error("Ошибка при создании задачи:", error);
      alert("Не удалось создать задачу. Пожалуйста, попробуйте снова.");
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mb: 4 }}>
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
        multiline
        rows={4}
        margin="normal"
      />
      <TextField
        label="Дедлайн"
        type="datetime-local"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
        required
        fullWidth
        margin="normal"
        InputLabelProps={{
          shrink: true, // Чтобы ярлык не перекрывал дату
        }}
      />
      <Button type="submit" variant="contained" color="primary">
        Добавить задачу
      </Button>
    </Box>
  );
}

export default TaskForm;
