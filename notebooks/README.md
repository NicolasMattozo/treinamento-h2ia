# 📓 Cadernos de Laboratório (Jupyter Notebooks)

Este diretório contém os notebooks e relatórios interativos desenvolvidos durante as atividades e pesquisas do treinamento em IA.

---

## ⚡ Como Executar

### 1. Localmente (no VS Code)
1. Certifique-se de que o ambiente virtual está configurado (`.venv`).
2. Abra o arquivo `.ipynb` no VS Code.
3. No canto superior direito do notebook, clique em **Select Kernel** (Selecionar Kernel) e escolha:
   - **Python Environments...** -> **`.venv (ufpel-ai)`** (ou `Python (ufpel-ai)`).
4. Execute as células normalmente usando `Shift + Enter`.

### 2. No Google Colab
Cada notebook possui um badge no topo:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NicolasMattozo/ufpel-ia-training)

Clicando no badge (diretamente no GitHub), o notebook é carregado instantaneamente no Google Colab.

#### Dicas para Google Colab:
- Para instalar dependências adicionais no Colab se necessário:
  ```python
  !pip install -r https://raw.githubusercontent.com/NicolasMattozo/ufpel-ia-training/main/requirements.txt
  ```
- Para habilitar GPU no Colab (caso vá treinar modelos profundos):
  - Menu: **Ambiente de execução (Runtime)** -> **Alterar tipo de ambiente de execução (Change runtime type)** -> Selecionar **T4 GPU**.
- Para salvar alterações feitas no Colab de volta para o GitHub:
  - Menu: **Arquivo (File)** -> **Salvar uma cópia no GitHub (Save a copy in GitHub)**.

---

## 📑 Notebooks Disponíveis

| Notebook | Descrição | Abrir no Colab |
| :--- | :--- | :---: |
| [Relatório_Buscas_sem_informação.ipynb](Relat%C3%B3rio_Buscas_sem_informa%C3%A7%C3%A3o.ipynb) | Estudo comparativo de buscas cegas (BFS, DFS, IDDFS) no 8-puzzle | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NicolasMattozo/ufpel-ia-training/blob/main/notebooks/Relat%C3%B3rio_Buscas_sem_informa%C3%A7%C3%A3o.ipynb) |
| [Relatório_Busca_com_Informação.ipynb](Relat%C3%B3rio_Busca_com_Informa%C3%A7%C3%A3o.ipynb) | Estudo e análise de busca heurística informada (A*) no 8-puzzle | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NicolasMattozo/ufpel-ia-training/blob/main/notebooks/Relat%C3%B3rio_Busca_com_Informa%C3%A7%C3%A3o.ipynb) |
