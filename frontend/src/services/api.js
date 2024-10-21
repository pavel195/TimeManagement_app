// frontend/src/services/api.js

import axios from 'axios';

// Базовый URL вашего API
const API_URL = 'http://localhost:8000';

// Функция для получения списка задач
export const getTasks = (skip = 0, limit = 100) => {
  return axios.get(`${API_URL}/tasks/`, {
    params: {
      skip,
      limit
    }
  });
};

// Функция для создания новой задачи
export const createTask = (task) => {
  return axios.post(`${API_URL}/tasks/`, task);
};

// Функция для получения задачи по ID
export const getTaskById = (taskId) => {
  return axios.get(`${API_URL}/tasks/${taskId}`);
};

// Функция для обновления задачи
export const updateTask = (taskId, updatedTask) => {
  return axios.put(`${API_URL}/tasks/${taskId}`, updatedTask);
};

// Функция для удаления задачи
export const deleteTask = (taskId) => {
  return axios.delete(`${API_URL}/tasks/${taskId}`);
};
