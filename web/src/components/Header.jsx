import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../style/Header.css';

export default function Header({ user, onLogout }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    onLogout();
    navigate('/');
  };

  const getInitials = (name) => {
    if (!name) return 'US';
    return name
      .split(' ')
      .filter(word => word.length > 0)
      .map(word => word[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  return (
    <header className="bit-header">
      <div className="header-container">
        <button 
          className="logo"
          onClick={() => navigate('/dashboard')}
        >
          BiT App - Orientação e Inclusão
        </button>

        {user && (
          <div className="header-user">
            <span className="user-name">{user.nome}</span>
            <div className="user-avatar" title={`${user.nome} (${user.area})`}>
              {getInitials(user.nome)}
            </div>
            <button 
              className="logout-btn"
              onClick={handleLogout}
              title="Sair"
            >
              ✕
            </button>
          </div>
        )}
      </div>
    </header>
  );
}
