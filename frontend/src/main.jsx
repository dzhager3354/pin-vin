import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// import Test from './CommonComponents/Test/Test';
import Gate from './Pages/Gate/Gate';
import ManagerPhoneNumbers from './Pages/ManagerPages/ManagerPhoneNumbers/ManagerPhoneNumbers';
import CallsByPhoneNumber from './Pages/ManagerPages/CallsByPhoneNumber/CallsByPhoneNumber';
import SuperviserStats from './Pages/SuperviserPages/SuperviserStats/SuperviserStats';
import CallDetails from './Pages/ManagerPages/CallDetails/CallDetails';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <Router> 
          <Routes>
            {/* <Route path="/test" element={<Test/>}/> */}
            <Route path="/" element={<Gate/>}/>
            <Route path="/manager-phone-numbers" element={<ManagerPhoneNumbers/>}/>
            <Route path="/calls-by-phonenumber/:id" element={<CallsByPhoneNumber/>} />
            <Route path="/superviser-stats" element={<SuperviserStats/>} />
            <Route path="/call-details/:callId/:currentId" element={<CallDetails/>} />
            {/* <Route path="/superviser/:id" element={</>}/> */}
            {/* <Route path="/manager/:id" element={</>}/> */}
          </Routes>
      </Router>
  </React.StrictMode>
);