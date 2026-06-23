import React, { useState } from 'react';
import '../style/OnboardingFlow.css';

export default function OnboardingFlow({ onComplete }) {
  const [step, setStep] = useState(0);
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    dataNascimento: '',
    sexo: '',
    pais: '',
    estado: '',
    cidade: '',
    whatsapp: '',
    formacao: '',
    nivel: '',
    area: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const steps = [
    {
      title: 'Dados pessoais',
      subtitle: 'Vamos nos conhecer',
      fields: ['nome', 'email', 'dataNascimento', 'sexo'],
    },
    {
      title: 'Localização',
      subtitle: 'Onde você está',
      fields: ['pais', 'estado', 'cidade'],
    },
    {
      title: 'Contato',
      subtitle: 'Nos conectando',
      fields: ['whatsapp'],
    },
    {
      title: 'Formação',
      subtitle: 'Sua trajetória educacional',
      fields: ['formacao'],
    },
    {
      title: 'Profissional',
      subtitle: 'Seu nível e área de interesse',
      fields: ['nivel', 'area'],
    },
  ];

  const currentStep = steps[step];
  const progress = ((step + 1) / steps.length) * 100;

  // Simple validation check before proceeding
  const isStepValid = () => {
    return currentStep.fields.every(field => {
      const val = formData[field];
      if (typeof val === 'string') {
        return val.trim() !== '';
      }
      return val !== undefined && val !== null;
    });
  };

  const handleNext = (e) => {
    e.preventDefault();
    if (!isStepValid()) {
      alert('Por favor, preencha todos os campos obrigatórios deste passo.');
      return;
    }
    
    if (step < steps.length - 1) {
      setStep(step + 1);
    } else {
      onComplete(formData);
    }
  };

  const handleBack = (e) => {
    e.preventDefault();
    if (step > 0) {
      setStep(step - 1);
    }
  };

  return (
    <div className="onboarding-wrapper">
      <div className="onboarding-container">
        
        {/* Progresso */}
        <div className="progress-section">
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: `${progress}%` }}></div>
          </div>
          <span className="progress-text">Passo {step + 1} de {steps.length}</span>
        </div>

        {/* Conteúdo */}
        <div className="onboarding-content">
          <div className="step-header">
            <h2>{currentStep.title}</h2>
            <p>{currentStep.subtitle}</p>
          </div>

          <form className="step-form" onSubmit={handleNext}>
            {currentStep.fields.map(fieldName => (
              <div key={fieldName} className="form-group">
                <label htmlFor={fieldName}>
                  {getFieldLabel(fieldName)}
                </label>
                {fieldName === 'sexo' ? (
                  <select
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={handleChange}
                    required
                  >
                    <option value="">Selecione...</option>
                    <option value="masculino">Masculino</option>
                    <option value="feminino">Feminino</option>
                    <option value="outro">Outro</option>
                  </select>
                ) : fieldName === 'nivel' ? (
                  <select
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={handleChange}
                    required
                  >
                    <option value="">Selecione...</option>
                    <option value="junior">Júnior</option>
                    <option value="pleno">Pleno</option>
                    <option value="senior">Sênior</option>
                    <option value="estudante">Estudante</option>
                  </select>
                ) : fieldName === 'area' ? (
                  <select
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={handleChange}
                    required
                  >
                    <option value="">Selecione...</option>
                    <option value="frontend">Desenvolvimento Frontend</option>
                    <option value="backend">Desenvolvimento Backend</option>
                    <option value="ux/ui design">UX/UI Design</option>
                  </select>
                ) : (
                  <input
                    type={getInputType(fieldName)}
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={handleChange}
                    placeholder={getFieldPlaceholder(fieldName)}
                    required
                  />
                )}
              </div>
            ))}

            {/* Botões */}
            <div className="form-actions">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleBack}
                disabled={step === 0}
              >
                Voltar
              </button>
              <button
                type="submit"
                className="btn btn-primary"
              >
                {step === steps.length - 1 ? 'Finalizar' : 'Próximo'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

function getFieldLabel(field) {
  const labels = {
    nome: 'Nome completo',
    email: 'E-mail',
    dataNascimento: 'Data de nascimento',
    sexo: 'Sexo',
    pais: 'País',
    estado: 'Estado',
    cidade: 'Cidade',
    whatsapp: 'WhatsApp',
    formacao: 'Nível de formação acadêmica',
    nivel: 'Nível profissional',
    area: 'Área de tecnologia',
  };
  return labels[field] || field;
}

function getInputType(field) {
  if (field === 'email') return 'email';
  if (field === 'dataNascimento') return 'date';
  if (field === 'whatsapp') return 'tel';
  return 'text';
}

function getFieldPlaceholder(field) {
  const placeholders = {
    nome: 'Seu nome completo',
    email: 'seu@email.com',
    dataNascimento: 'DD/MM/YYYY',
    pais: 'ex: Brasil',
    estado: 'ex: São Paulo',
    cidade: 'ex: São Paulo',
    whatsapp: 'ex: +55 (11) 99999-9999',
    formacao: 'ex: Ensino Superior em TI',
  };
  return placeholders[field] || '';
}
