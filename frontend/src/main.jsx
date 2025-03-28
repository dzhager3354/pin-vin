import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Test from './CommonComponents/Test/Test';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <Router> 
          <Routes>
            <Route path="/" element={<Test/>}/>
          </Routes>
      </Router>
  </React.StrictMode>
);