const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export const apiClient = {
  async post(endpoint, data) {
    try {
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  async get(endpoint) {
    try {
      const response = await fetch(`${API_URL}${endpoint}`);
      
      if (!response.ok) {
        throw new Error(`API Error: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  // Endpoints específicos do BiT
  async orientar(userData) {
    return this.post('/orientar', {
      user_id: userData.id,
      profile: userData.profile,
      level: userData.level,
      region: userData.region,
      language: 'pt',
      lat: userData.latitude,
      lng: userData.longitude,
    });
  },

  async saudeMental(userId, humor, nota) {
    return this.post('/saude', {
      user_id: userId,
      humor: humor,
      weekly_note: nota,
      context: 'daily_checkin',
    });
  },

  async criarUsuario(dados) {
    return this.post('/usuarios', dados);
  },

  async obterUsuario(userId) {
    return this.get(`/usuarios/${userId}`);
  },
};