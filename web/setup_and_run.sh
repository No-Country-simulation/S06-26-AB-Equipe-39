#!/bin/bash
set -e

echo "=== Iniciando Setup do Ambiente BiT Front-End ==="

# Verifica se o NVM já está instalado
export NVM_DIR="$HOME/.nvm"
if [ ! -d "$NVM_DIR" ]; then
  echo "NVM não encontrado. Procurando forma de baixar o NVM..."
  
  if command -v curl >/dev/null 2>&1; then
    echo "Baixando com curl..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  elif command -v wget >/dev/null 2>&1; then
    echo "Baixando com wget..."
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  elif command -v python3 >/dev/null 2>&1; then
    echo "Baixando com python3..."
    python3 -c "import urllib.request; urllib.request.urlretrieve('https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh', 'nvm_install.sh')"
    bash nvm_install.sh
    rm nvm_install.sh
  else
    echo "ERRO: Não encontramos curl, wget ou python3 para baixar o NVM."
    echo "Por favor, instale um deles ou instale o NVM manualmente seguindo https://github.com/nvm-sh/nvm"
    exit 1
  fi
fi

# Carrega o NVM na sessão atual do script
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

if command -v nvm >/dev/null 2>&1; then
  echo "Instalando e ativando Node.js versão 20 (LTS)..."
  nvm install 20
  nvm use 20
else
  echo "ERRO: nvm não pôde ser carregado na sessão atual."
  echo "Tente reiniciar seu terminal e rodar novamente."
  exit 1
fi

echo "Verificando versões instaladas:"
node -v
npm -v

echo "Instalando dependências do projeto na pasta web/..."
cd /home/tavares/Documentos/Projects/hackaton/AppBit/web
npm install

echo "=== Setup concluído com sucesso! ==="
echo "Para rodar o servidor de desenvolvimento, execute:"
echo "  nvm use 20 && npm run dev"
