
import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

function DeadlineChart({ tasks }) {
  const data = tasks.map((task) => {
    const daysLeft = Math.ceil(
      (new Date(task.due_date) - new Date()) / (1000 * 60 * 60 * 24)
    );
    return {
      name: task.title,
      daysLeft: daysLeft >= 0 ? daysLeft : 0,
    };
  });

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey="name" />
        <YAxis label={{ value: 'Дней до дедлайна', angle: -90, position: 'insideLeft' }} />
        <Tooltip />
        <Bar dataKey="daysLeft" fill="#1976d2" />
      </BarChart>
    </ResponsiveContainer>
  );
}

export default DeadlineChart;
