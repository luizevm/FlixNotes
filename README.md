# 📘 FlixNotes

FlixNotes é um aplicativo web simples, desenvolvido em **Python + Django**, com o objetivo de permitir que o usuário registre e organize filmes e séries que já assistiu ou deseja assistir.  
O sistema funciona como um bloco de notas pessoal, sem necessidade de login, com foco em simplicidade e organização.

---

## 🎯 Objetivo do Projeto

Facilitar o controle pessoal de mídias assistidas, permitindo registrar informações como:

- Título do filme ou série  
- Tipo (Filme / Série)  
- Plataforma de streaming  
- Gênero  
- Status (Assistido / Quero ver)  
- Avaliação (nota)  
- Comentários opcionais  

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Django 5** (ou versão utilizada no projeto)
- **SQLite** (banco de dados padrão)

---

## 📂 Estrutura Geral do Projeto

- `models.py` → Definição das classes principais (Obra, Plataforma, Gênero etc.)  
- `views.py` → Lógica de apresentação e operações CRUD  
- `urls.py` → Configuração das rotas  
- `templates/` → Estrutura HTML das páginas  
- `admin.py` → Registro dos modelos no Django Admin  

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/flixnotes.git
cd flixnotes
