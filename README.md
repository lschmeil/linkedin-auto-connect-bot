🤖 LinkedIn Auto Connect Bot

Este projeto é um bot automatizado em Python utilizando Selenium que acessa o LinkedIn, realiza buscas por perfis profissionais e envia convites de conexão com uma mensagem personalizada e dinâmica.
A automação simula ações humanas de forma segura, reduzindo o tempo gasto para expandir sua rede profissional.

🚀 Funcionalidades

Login automático via cookies (sem necessidade de digitar e-mail/senha).

Busca de perfis pela palavra-chave definida (ex.: desenvolvedor).

Execução de scroll infinito para carregar novos resultados.

Coleta automática de links de perfis (/in/).

Abertura individual de cada perfil encontrado.

Detecção e clique automático no botão Conectar.

Adição de nota personalizada, preenchida com o nome real da pessoa.

Escolha aleatória entre mensagens pré-definidas.

Registro dos convites enviados em enviados.json para evitar repetição.

Limite configurável de convites por execução.

📂 Estrutura do Projeto

bot.py → Script principal de automação.

cookies.json → Cookies exportados do LinkedIn (necessários para login).

enviados.json → Arquivo gerado automaticamente contendo nomes já contatados.

requirements.txt → Lista de dependências do projeto.

⚙️ Instalação

Clone este repositório:

git clone https://github.com/seuusuario/linkedin-bot.git
cd linkedin-bot


Instale as dependências:

pip install -r requirements.txt


Adicione seus cookies do LinkedIn no arquivo cookies.json.

▶️ Como Usar

Execute o script principal:

python bot.py


O bot irá:

Carregar seus cookies.

Entrar no LinkedIn automaticamente.

Buscar perfis relacionados à palavra-chave.

Enviar convites personalizados.

Registrar nomes já contactados em enviados.json.

📝 Mensagens Personalizadas

O bot escolhe automaticamente uma mensagem aleatória e insere o nome do perfil:

"Oi {nome}, tudo bem? Sou Lucas, dev júnior de 17 anos. Quero muito me conectar com você para trocar experiências!"
"Olá {nome}! Sou Lucas, dev júnior de 17 anos. Estou começando na área e seria ótimo ter você na minha rede."
"Hey {nome}, tenho 17 anos e estou iniciando como dev júnior. Seria incrível poder aprender com você!"
"Prazer {nome}! Sou Lucas, dev júnior de 17 anos. Vamos nos conectar e compartilhar conhecimento?"

⚠️ Avisos Importantes

O LinkedIn pode aplicar limites diários para convites → evite exageros.

A automação é para fins educacionais — utilize com responsabilidade.

O limite de convites por execução pode ser configurado em:

limite_convites = 20

🧑‍💻 Autor

Lucas Schmeil — Desenvolvedor Júnior
Automação criada para estudo, produtividade e networking profissional.
