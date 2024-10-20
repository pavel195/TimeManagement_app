import React from "react";
import {AppBar, Toolbar,Typography,Container} from '@mui/material';

{/* Основной каркас для страниц приложения */}
function Layout({ children }) {
    return (
      <>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6">Time Management App</Typography>
          </Toolbar>
        </AppBar>
        <Container style={{ marginTop: '2rem' }}>
          {children}
        </Container>
      </>
    );
  }

  export default Layout;
