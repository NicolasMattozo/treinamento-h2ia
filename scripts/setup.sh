#!/usr/bin/env bash
# ==============================================================================
# Script de configuração do ambiente de desenvolvimento (ufpel-ai-training)
# ==============================================================================
set -e

echo "🚀 Iniciando configuração do ambiente Python..."

# Detecta o gerenciador (prioriza 'uv', faz fallback para 'python3 -m venv')
if command -v uv &> /dev/null; then
    PKG_MGR="uv"
    echo "✨ 'uv' detectado! Utilizando para instalação ultra-rápida."
elif [ -f "$HOME/.local/bin/uv" ]; then
    PKG_MGR="$HOME/.local/bin/uv"
    echo "✨ 'uv' encontrado em ~/.local/bin/uv!"
else
    PKG_MGR="pip"
    echo "ℹ️ 'uv' não encontrado. Utilizando Python venv padrão."
fi

# 1. Criação do Virtual Environment (.venv) se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando ambiente virtual em .venv..."
    if [ "$PKG_MGR" != "pip" ]; then
        $PKG_MGR venv .venv
    else
        python3 -m venv .venv
    fi
else
    echo "✅ Ambiente virtual .venv já existe."
fi

# 2. Instalação das dependências
echo "📥 Instalando dependências a partir do requirements.txt..."
if [ "$PKG_MGR" != "pip" ]; then
    $PKG_MGR pip install -r requirements.txt
else
    .venv/bin/pip install --upgrade pip
    .venv/bin/pip install -r requirements.txt
fi

# 3. Registro do Jupyter Kernel para VS Code e Jupyter Lab
echo "🪐 Registrando kernel do Jupyter ('Python (ufpel-ai)')..."
.venv/bin/python -m ipykernel install --user --name ufpel-ai --display-name "Python (ufpel-ai)"

echo ""
echo "🎉 Ambiente configurado com sucesso!"
echo "💡 Para ativar o ambiente no terminal:"
echo "   source .venv/bin/activate"
echo "💡 No VS Code, selecione o kernel 'Python (ufpel-ai)' ou '.venv' nos notebooks."
