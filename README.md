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

## Estrutura do Projeto

- **barbearia_project/**: Configurações principais do Django
- **core/**: Aplicativo para páginas básicas (home, sobre, contato)
- **usuarios/**: Aplicativo para gerenciamento de usuários e perfis
- **agendamentos/**: Aplicativo para gerenciamento de agendamentos, barbeiros e serviços
- **static/**: Arquivos estáticos (CSS, JavaScript, imagens)
- **media/**: Arquivos enviados pelos usuários (fotos de perfil)
- **templates/**: Templates HTML

## Personalização

- Modifique os templates em `templates/` para alterar a aparência
- Ajuste os estilos em `static/css/main.css`
- Adicione ou modifique funcionalidades nos aplicativos correspondentes

## Licença

[Licença de Uso Exclusivo](LICENSE)

## Contato

Para suporte ou dúvidas, entre em contato através do email: eduardonunesbueno56@gmail.com
