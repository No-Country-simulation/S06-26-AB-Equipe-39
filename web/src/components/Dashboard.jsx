import React, { useState, useEffect } from 'react';
import { apiClient } from '../services/client';
import '../style/Dashboard.css';

export default function Dashboard({ user }) {
  const [activeTab, setActiveTab] = useState('orientacao');

  // Estado da Orientação
  const [orientacaoData, setOrientacaoData] = useState(null);
  const [loadingOrientacao, setLoadingOrientacao] = useState(false);
  const [errorOrientacao, setErrorOrientacao] = useState(null);

  // Estado da Saúde Mental
  const [humor, setHumor] = useState('');
  const [nota, setNota] = useState(5);
  const [contexto, setContexto] = useState('');
  const [saudeResult, setSaudeResult] = useState(null);
  const [submittingSaude, setSubmittingSaude] = useState(false);
  const [errorSaude, setErrorSaude] = useState(null);

  // Emojis de Humor
  const humores = [
    { label: 'Feliz', emoji: '😃', value: 'feliz' },
    { label: 'Cansado', emoji: '🥱', value: 'cansado' },
    { label: 'Triste', emoji: '😢', value: 'triste' },
    { label: 'Ansioso', emoji: '😰', value: 'ansioso' },
    { label: 'Sobrecarregado', emoji: '🤯', value: 'sobrecarregado' },
  ];

  // Executa orientação automaticamente ao carregar
  useEffect(() => {
    handleCalcularOrientacao();
  }, []);

  const handleCalcularOrientacao = async () => {
    setLoadingOrientacao(true);
    setErrorOrientacao(null);
    try {
      // Obter geolocalização se disponível no navegador
      let latitude = -8.8383;
      let longitude = 13.2344;
      
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
          },
          (err) => console.log('Usando localização padrão', err),
          { timeout: 5000 }
        );
      }

      const res = await apiClient.orientar({
        ...user,
        latitude,
        longitude
      });
      setOrientacaoData(res);
    } catch (err) {
      setErrorOrientacao('Não foi possível obter os dados de orientação.');
    } finally {
      setLoadingOrientacao(false);
    }
  };

  const handleSaudeSubmit = async (e) => {
    e.preventDefault();
    if (!humor) {
      alert('Por favor, selecione um emoji de humor.');
      return;
    }
    
    setSubmittingSaude(true);
    setErrorSaude(null);
    setSaudeResult(null);
    try {
      const res = await apiClient.saudeMental(user.id || 'u_123', humor, nota, contexto);
      setSaudeResult(res);
    } catch (err) {
      setErrorSaude('Não foi possível enviar o check-in de saúde.');
    } finally {
      setSubmittingSaude(false);
    }
  };

  return (
    <main className="dashboard-main">
      <div className="dashboard-container">
        
        {/* Boas-vindas */}
        <section className="welcome-banner">
          <h1>Olá, {user.nome}!</h1>
          <p className="welcome-sub">
            Área: <span className="badge-tech">{user.area}</span> • Nível: <span className="badge-level">{user.nivel}</span>
          </p>
        </section>

        {/* Tabs de Navegação */}
        <div className="tab-navigation">
          <button 
            className={`tab-btn ${activeTab === 'orientacao' ? 'active' : ''}`}
            onClick={() => setActiveTab('orientacao')}
          >
            🧭 Orientação Profissional
          </button>
          <button 
            className={`tab-btn ${activeTab === 'saude' ? 'active' : ''}`}
            onClick={() => setActiveTab('saude')}
          >
            🌱 Saúde Mental
          </button>
        </div>

        {/* Conteúdo das Tabs */}
        <div className="tab-content">
          
          {/* ABA 1: ORIENTAÇÃO */}
          {activeTab === 'orientacao' && (
            <div className="tab-pane">
              <div className="pane-header">
                <h2>Alinhamento Profissional e Vagas</h2>
                <p>Veja seu gap de competências e oportunidades recomendadas.</p>
                <button 
                  className="btn btn-secondary btn-sm"
                  onClick={handleCalcularOrientacao}
                  disabled={loadingOrientacao}
                >
                  {loadingOrientacao ? 'Analisando...' : 'Recalcular Perfil'}
                </button>
              </div>

              {loadingOrientacao && (
                <div className="loading-state">
                  <div className="spinner"></div>
                  <p>O Agente BiT está cruzando seu perfil com as vagas do mercado...</p>
                </div>
              )}

              {errorOrientacao && (
                <div className="error-card">
                  <p>⚠️ {errorOrientacao}</p>
                </div>
              )}

              {!loadingOrientacao && orientacaoData && (
                <div className="orientacao-grid">
                  
                  {/* Card de Progresso / Match */}
                  <div className="card card-progress">
                    <h3>Compatibilidade com o Mercado</h3>
                    <div className="progress-radial-wrapper">
                      <div className="progress-ring">
                        <span className="progress-val">{orientacaoData.gap_percentual}%</span>
                      </div>
                    </div>
                    <p className="progress-desc">
                      Você possui {orientacaoData.gap_percentual}% das habilidades buscadas em vagas de {user.area}.
                    </p>
                  </div>

                  {/* Card de Competências em Aberto (Gap) */}
                  <div className="card card-gap">
                    <h3>Recomendações de Estudo</h3>
                    <p className="section-sub">Aprimore estas habilidades para fechar o gap:</p>
                    <ul className="gap-list">
                      {orientacaoData.gap_itens.map((item, idx) => (
                        <li key={idx} className="gap-item">
                          <span className="bullet">⚡</span> {item}
                        </li>
                      ))}
                    </ul>
                    <div className="trilha-sugerida">
                      <strong>Trilha sugerida pelo Agente:</strong>
                      <p>✨ {orientacaoData.trilha_sugerida}</p>
                    </div>
                  </div>

                  {/* Card de Vagas Recomendadas */}
                  <div className="card card-jobs">
                    <h3>Vagas Compatíveis</h3>
                    <div className="jobs-list">
                      {orientacaoData.vagas_compativeis && orientacaoData.vagas_compativeis.length > 0 ? (
                        orientacaoData.vagas_compativeis.map((vaga, idx) => (
                          <div key={idx} className="job-card">
                            <div className="job-info">
                              <span className="job-title">{vaga.titulo}</span>
                              <span className="job-company">{vaga.empresa}</span>
                            </div>
                            <span className="job-match">{vaga.match}% match</span>
                          </div>
                        ))
                      ) : (
                        <p>Nenhuma vaga compatível encontrada no momento.</p>
                      )}
                    </div>
                  </div>

                </div>
              )}
            </div>
          )}

          {/* ABA 2: SAÚDE MENTAL */}
          {activeTab === 'saude' && (
            <div className="tab-pane">
              <div className="pane-header">
                <h2>Check-in Diário de Bem-estar</h2>
                <p>Como você está se sentindo hoje? Compartilhar ajuda a aliviar a pressão.</p>
              </div>

              <div className="saude-layout">
                {/* Formulário de Envio */}
                <form onSubmit={handleSaudeSubmit} className="saude-form">
                  
                  {/* Seleção de Emojis */}
                  <div className="form-group">
                    <label>Como você se sente hoje?</label>
                    <div className="emoji-selector">
                      {humores.map((h) => (
                        <button
                          key={h.value}
                          type="button"
                          className={`emoji-btn ${humor === h.value ? 'selected' : ''}`}
                          onClick={() => setHumor(h.value)}
                        >
                          <span className="emoji-pic">{h.emoji}</span>
                          <span className="emoji-lbl">{h.label}</span>
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Nota Semanal */}
                  <div className="form-group">
                    <div className="label-with-value">
                      <label htmlFor="nota-semanal">Nota de bem-estar (0 a 10)</label>
                      <span className="slider-value">{nota}</span>
                    </div>
                    <input
                      type="range"
                      id="nota-semanal"
                      min="0"
                      max="10"
                      value={nota}
                      onChange={(e) => setNota(Number(e.target.value))}
                      className="slider"
                    />
                    <div className="slider-labels">
                      <span>Crítico 😢</span>
                      <span>Regular 😐</span>
                      <span>Excelente 😊</span>
                    </div>
                  </div>

                  {/* Contexto Livre */}
                  <div className="form-group">
                    <label htmlFor="contexto">Opcional: O que está acontecendo esta semana?</label>
                    <textarea
                      id="contexto"
                      rows="3"
                      value={contexto}
                      onChange={(e) => setContexto(e.target.value)}
                      placeholder="Ex: ansioso por causa de testes ou aguardando resposta de entrevistas..."
                    />
                  </div>

                  <button 
                    type="submit" 
                    className="btn btn-primary"
                    disabled={submittingSaude}
                  >
                    {submittingSaude ? 'Enviando...' : 'Registrar Check-in'}
                  </button>

                  {errorSaude && (
                    <div className="error-card mt-3">
                      <p>⚠️ {errorSaude}</p>
                    </div>
                  )}
                </form>

                {/* Exibição da Resposta / Mensagem de Acolhimento */}
                {saudeResult && (
                  <div className="saude-result-container">
                    
                    {/* Mensagem Acolhedora do Agente */}
                    <div className="card card-response-agent animate-fade-in">
                      <h3>Mensagem de Apoio</h3>
                      <p className="agent-msg">"{saudeResult.mensagem}"</p>
                      <div className="suggested-action">
                        <strong>Atividade recomendada:</strong>
                        <p>{saudeResult.acao_sugerida}</p>
                      </div>
                    </div>

                    {/* Alerta Crítico (CVV) quando nota < 4 ou derivar_cvv for true */}
                    {saudeResult.derivar_cvv && (
                      <div className="card cvv-card animate-pulse">
                        <div className="cvv-header">
                          <span className="cvv-alert-icon">❤️</span>
                          <h3>Você não está sozinho!</h3>
                        </div>
                        <p>
                          Conversar ajuda. Se você está passando por um momento difícil, 
                          considere entrar em contato com o <strong>Centro de Valorização da Vida (CVV)</strong>.
                        </p>
                        <div className="cvv-contacts">
                          <a href="tel:188" className="cvv-btn tel-btn">📞 Ligar 188</a>
                          <a href="https://www.cvv.org.br" target="_blank" rel="noopener noreferrer" className="cvv-btn link-btn">🌐 Visitar cvv.org.br</a>
                        </div>
                        <span className="cvv-footnote">Atendimento 24h, gratuito, sigiloso e acolhedor.</span>
                      </div>
                    )}

                  </div>
                )}
              </div>
            </div>
          )}

        </div>
      </div>
    </main>
  );
}
