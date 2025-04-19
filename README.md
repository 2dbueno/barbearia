# Sistema de Barbearia - Documentação

## Visão Geral

Este é um sistema web responsivo para gerenciamento de barbearia, desenvolvido com Django, SQLite, HTML, CSS e JavaScript. O sistema permite que clientes se cadastrem, visualizem e agendem horários, enquanto administradores podem gerenciar clientes, barbeiros, serviços e agendamentos.

## Funcionalidades

### Funcionalidades para Clientes
- Cadastro e login de usuários
- Visualização e atualização de perfil
- Agendamento de horários com seleção de barbeiro e serviço
- Cancelamento de agendamentos
- Visualização de histórico de agendamentos

### Funcionalidades para Administradores
- Visualização de todos os agendamentos
- Visualização de agendamentos por dia, semana e mês
- Gerenciamento de clientes
- Agendamento para clientes via CPF
- Cancelamento de agendamentos
- Gerenciamento de barbeiros e serviços

## Tecnologias Utilizadas

- **Backend**: Django 5.2 (Python 3.10)
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5
- **Ícones**: Font Awesome
- **Mapa**: Leaflet.js

## Requisitos de Sistema

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)

## Instalação

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/barbearia.git
cd barbearia
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Configure o banco de dados:
```
python manage.py migrate
```

5. Crie um superusuário (administrador):
```
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

7. Acesse o sistema em seu navegador:
```
http://127.0.0.1:8000/
```

## Estrutura do Projeto

- **barbearia_project/**: Configurações principais do Django
- **core/**: Aplicativo para páginas básicas (home, sobre, contato)
- **usuarios/**: Aplicativo para gerenciamento de usuários e perfis
- **agendamentos/**: Aplicativo para gerenciamento de agendamentos, barbeiros e serviços
- **static/**: Arquivos estáticos (CSS, JavaScript, imagens)
- **media/**: Arquivos enviados pelos usuários (fotos de perfil)
- **templates/**: Templates HTML

## Configuração para Produção

Para implantar o sistema em um ambiente de produção, siga estas etapas adicionais:

1. Configure variáveis de ambiente para segurança:
```
export SECRET_KEY='sua_chave_secreta'
export DEBUG=False
export ALLOWED_HOSTS='seu_dominio.com,www.seu_dominio.com'
```

2. Configure um servidor web como Nginx ou Apache

3. Use Gunicorn ou uWSGI como servidor WSGI:
```
pip install gunicorn
gunicorn barbearia_project.wsgi:application
```

4. Configure um banco de dados mais robusto como PostgreSQL ou MySQL

5. Configure armazenamento de arquivos estáticos e de mídia

## Personalização

- Modifique os templates em `templates/` para alterar a aparência
- Ajuste os estilos em `static/css/main.css`
- Adicione ou modifique funcionalidades nos aplicativos correspondentes

## Licença

Este projeto está licenciado sob a licença MIT.

## Contato

Para suporte ou dúvidas, entre em contato através do email: contato@exemplo.com
