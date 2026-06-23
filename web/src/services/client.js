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
      console.warn(`[API Connection Failed] Using mock data for POST ${endpoint}`, error);
      return this.getMockResponse('POST', endpoint, data);
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
      console.warn(`[API Connection Failed] Using mock data for GET ${endpoint}`, error);
      return this.getMockResponse('GET', endpoint);
    }
  },

  // Endpoints específicos do BiT
  async orientar(userData) {
    return this.post('/orientar', {
      usuario_id: userData.id || 'u_123',
      perfil: userData.area || userData.profile || 'Engenharia de Software',
      nivel: userData.nivel || 'junior',
      regiao: `${userData.cidade || 'Luanda'}, ${userData.pais || 'AO'}`,
      idioma: userData.language || 'pt',
      lat: userData.latitude || -8.8383,
      lng: userData.longitude || 13.2344,
    });
  },

  async saudeMental(userId, humor, nota, contexto = '') {
    return this.post('/saude', {
      usuario_id: userId,
      humor: humor,
      nota_semanal: Number(nota),
      contexto: contexto,
    });
  },

  async criarUsuario(dados) {
    return this.post('/usuarios', dados);
  },

  async obterUsuario(userId) {
    return this.get(`/usuarios/${userId}`);
  },

  // Gerador de respostas mockadas (fallback)
  getMockResponse(method, endpoint, data = {}) {
    if (endpoint === '/usuarios') {
      return {
        id: `u_${Math.random().toString(36).substr(2, 9)}`,
        ...data,
        createdAt: new Date().toISOString()
      };
    }
    
    if (endpoint.startsWith('/usuarios/')) {
      const userId = endpoint.split('/').pop();
      return {
        id: userId,
        nome: 'Alejandro Designer',
        email: 'alejandro@example.com',
        pais: 'Brasil',
        estado: 'São Paulo',
        cidade: 'São Paulo',
        nivel: 'junior',
        area: 'UX/UI Design'
      };
    }

    if (endpoint === '/orientar') {
      const profile = data.perfil || 'Tecnologia';
      // Mock data adjusted to the user's selected area
      const skills = {
        'frontend': ['React avançado', 'Testes com Jest', 'TailwindCSS', 'Acessibilidade Web (WCAG)'],
        'backend': ['Node.js & Express', 'Arquitetura de APIs RESTful', 'PostgreSQL', 'Docker'],
        'ux/ui design': ['Figma avançado', 'Design System', 'Pesquisa com Usuários', 'Prototipagem de alta fidelidade'],
        'default': ['Git avançado', 'Testes automatizados', 'Inglês técnico', 'Lógica de programação']
      };

      const selectedSkills = skills[profile.toLowerCase()] || skills['default'];
      const gapPercent = Math.floor(Math.random() * 40) + 40; // 40% to 80%

      return {
        gap_percentual: gapPercent,
        gap_itens: selectedSkills,
        trilha_sugerida: `Trilha Especializada em ${profile} — Programa de Aceleração BiT`,
        vagas_compativeis: [
          { titulo: `Desenvolvedor ${profile} Júnior`, empresa: 'TechSoluções', match: gapPercent },
          { titulo: `Estagiário de ${profile}`, empresa: 'GlobalIT', match: gapPercent + 5 }
        ],
        confianca: 0.89
      };
    }

    if (endpoint === '/saude') {
      const nota = Number(data.nota_semanal);
      const humor = data.humor || 'cansado';
      
      if (nota < 4) {
        return {
          mensagem: `Notamos que as coisas estão difíceis para você hoje (${humor}). Lembre-se de que você não precisa carregar todo esse peso sozinho.`,
          acao_sugerida: 'Recomendamos buscar apoio emocional. Que tal conversar com o Centro de Valorização da Vida (CVV)? É gratuito e confidencial.',
          derivar_cvv: true,
          nota_atual: nota,
          alerta: 'Alerta de saúde mental ativado — Derivação de emergência habilitada.'
        };
      } else {
        return {
          mensagem: `Obrigado por registrar seu check-in diário. O seu estado é "${humor}". Monitorar as nossas emoções é um passo importante para o autoconhecimento.`,
          acao_sugerida: 'Que tal tirar 10 minutos para respirar fundo ou fazer um alongamento rápido?',
          derivar_cvv: false,
          nota_atual: nota,
          alerta: null
        };
      }
    }

    return { message: 'Mock data generic success' };
  }
};
