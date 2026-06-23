import React, { useState, useEffect } from 'react';
import { HashRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Header from './components/Header';
import OnboardingFlow from './components/OnboardingFlow';
import Dashboard from './components/Dashboard';
import './style/global.css';

export default function App() {
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem('bit_user');
    return saved ? JSON.parse(saved) : null;
  });

  const handleOnboardingComplete = (userData) => {
    // Adiciona um id único para o usuário
    const fullUser = {
      ...userData,
      id: `u_${Date.now()}`
    };
    localStorage.setItem('bit_user', JSON.stringify(fullUser));
    setUser(fullUser);
  };

  const handleLogout = () => {
    localStorage.removeItem('bit_user');
    setUser(null);
  };

  return (
    <Router>
      <Header user={user} onLogout={handleLogout} />
      <Routes>
        <Route 
          path="/" 
          element={
            user ? (
              <Navigate to="/dashboard" replace />
            ) : (
              <OnboardingFlow onComplete={handleOnboardingComplete} />
            )
          } 
        />
        <Route 
          path="/dashboard" 
          element={
            user ? (
              <Dashboard user={user} />
            ) : (
              <Navigate to="/" replace />
            )
          } 
        />
        {/* Fallback de rotas */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}
