
import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';

function TaskList({ tasks }) {
  return (
    <List>
      {tasks.map((task) => (
        <ListItem key={task.id}>
          <ListItemText
            primary={task.title}
            secondary={`Дедлайн: ${new Date(task.due_date).toLocaleDateString()}`}
          />
        </ListItem>
      ))}
    </List>
  );
}

export default TaskList;
