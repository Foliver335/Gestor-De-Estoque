<div>
  <h2>Gestor de Estoque: Sistema Inteligente de Controle de Materiais</h2>
  <p>Um sistema desktop robusto e intuitivo desenvolvido em Python, utilizando Tkinter para uma interface gráfica amigável e PostgreSQL para um gerenciamento de dados eficiente. Adotamos a arquitetura MVC (Model-View-Controller) para garantir um código organizado, escalável e de fácil manutenção.</p>

  <h3>Estrutura de Diretórios</h3>
   <div>
        <pre>
material_control/
├── app.py                 # Ponto de entrada da aplicação
├── controller/
│   └── material_controller.py  # Lógica de controle entre View e Model
├── model/
│   ├── db_connection.py        # Conexão com PostgreSQL
│   └── material_model.py       # Operações de banco (CRUD)
└── view/
    ├── main_view.py           # Janela principal (menu)
    ├── register_view.py       # Tela de cadastro de materiais
    ├── entry_view.py          # Tela de registro de entrada (código de barras)
    └── exit_view.py           # Tela de registro de saída (código de barras)
        </pre>
    </div>
  <p>A organização do projeto foi pensada para facilitar o desenvolvimento e a compreensão da sua arquitetura:</p>
  <ul>
    <li><code>app.py</code>: 🚪 Ponto de entrada principal da aplicação.</li>
    <li><code>controller/</code>: 🧠 Camada responsável pela lógica de controle, intermediando a comunicação entre a View e o Model.
      <ul>
        <li><code>material_controller.py</code>: Controla o fluxo de dados e as ações relacionadas aos materiais.</li>
      </ul>
    </li>
    <li><code>model/</code>: 💾 Camada que lida com a persistência dos dados e a interação com o banco de dados.
      <ul>
        <li><code>db_connection.py</code>: Estabelece e gerencia a conexão com o banco de dados PostgreSQL.</li>
        <li><code>material_model.py</code>: Implementa as operações de Criação, Leitura, Atualização e Exclusão (CRUD) dos dados dos materiais.</li>
      </ul>
    </li>
    <li><code>view/</code>: 🎨 Camada responsável pela interface gráfica com o usuário.
      <ul>
        <li><code>main_view.py</code>: Janela principal da aplicação, oferecendo o menu de opções.</li>
        <li><code>register_view.py</code>: Formulário para o cadastro de novos materiais no sistema.</li>
        <li><code>entry_view.py</code>: Interface para registrar a entrada de materiais utilizando leitura de código de barras.</li>
        <li><code>exit_view.py</code>: Interface para registrar a saída de materiais, também com suporte a código de barras.</li>
      </ul>
    </li>
  </ul>

  <h3>🚀 Requisitos para Execução</h3>
  <p>Antes de iniciar, certifique-se de que os seguintes requisitos estejam atendidos em seu ambiente:</p>
  <ul>
    <li><strong>Python</strong>: Versão 3.8 ou superior instalada.</li>
    <li><strong>psycopg2</strong>: Biblioteca Python para comunicação com PostgreSQL. Instale com: <code>pip install psycopg2</code></li>
    <li><strong>PostgreSQL</strong>: Servidor versão 9.6 ou superior em execução local.</li>
  </ul>

  <h3>⚙️ Configuração do Banco de Dados</h3>
  <p>Siga os passos abaixo para configurar o banco de dados PostgreSQL que o sistema utilizará:</p>
  <ol>
    <li><strong>Crie o Banco de Dados:</strong> Utilize o comando SQL abaixo no seu cliente PostgreSQL:
      <pre><code>CREATE DATABASE materiais;</code></pre>
    </li>
    <li><strong>Configure as Credenciais:</strong> Edite o arquivo <code>model/db_connection.py</code> e ajuste as informações de conexão de acordo com sua configuração do PostgreSQL:
      <pre><code class="language-python">psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="materiais",  # Nome do banco de dados criado
    user="postgres",       # Seu usuário PostgreSQL
    password="root"        # Sua senha do PostgreSQL
)</code></pre>
    </li>
    <li><strong>Criação Automática de Tabela:</strong> Caso a tabela de materiais ainda não exista no banco de dados, o sistema se encarregará de criá-la automaticamente na primeira execução.</li>
  </ol>

  <h3>▶️ Como Executar o Sistema</h3>
  <p>Siga estas instruções para colocar o Gestor de Estoque em funcionamento:</p>
  <ol>
    <li><strong>Clone o Repositório:</strong> Utilize o Git via SSh para baixar o código do projeto para sua máquina:
      <pre><code>git clone &lt;git@github.com:Foliver335/Gestor-De-Estoque.git&gt;</code></pre>
    </li>
    <li><strong>Acesse a Pasta do Projeto:</strong> Navegue até o diretório onde o repositório foi clonado:
      <pre><code>cd material_control</code></pre>
    </li>
    <li><strong>Instale as Dependências:</strong> Certifique-se de ter todas as bibliotecas necessárias instaladas:
      <pre><code>pip install psycopg2</code></pre>
    </li>
    <li><strong>Execute a Aplicação:</strong> Inicie o sistema com o seguinte comando:
      <pre><code>python app.py</code></pre>
    </li>
  </ol>
  <p>Após a execução, a janela principal do Gestor de Estoque será exibida, apresentando as seguintes opções:</p>
  <ul>
    <li><strong>Cadastrar Material:</strong> Permite inserir informações detalhadas sobre um novo material, como código, nome, quantidade, unidade de medida, descrição e data de validade.</li>
    <li><strong>Registrar Entrada:</strong> Interface otimizada para registrar a entrada de materiais no estoque, utilizando a leitura (ou digitação) do código de barras e a especificação da quantidade.</li>
    <li><strong>Registrar Saída:</strong> Similar ao registro de entrada, esta opção permite dar baixa nos materiais do estoque, informando o código de barras e a quantidade a ser removida.</li>
  </ul>

  <h3>⚙️ Fluxo de Uso Detalhado</h3>
  <h4>Cadastrar Material</h4>
  <ol>
    <li>Preencha todos os campos do formulário com as informações do novo material.</li>
    <li>Clique no botão "Cadastrar" para salvar as informações no banco de dados.</li>
    <li>Uma mensagem de confirmação será exibida, e a janela de cadastro será fechada.</li>
  </ol>

  <h4>Registrar Entrada</h4>
  <ol>
    <li>Ao abrir a tela de registro de entrada, o campo de código de barras estará automaticamente selecionado (com foco).</li>
    <li>Passe o leitor de código de barras no produto (ou digite o código manualmente e pressione a tecla Enter).</li>
    <li>Informe a quantidade de itens que estão entrando no estoque.</li>
    <li>Clique no botão "Registrar Entrada" para confirmar a operação.</li>
    <li>Uma mensagem de confirmação será mostrada ao usuário.</li>
  </ol>

  <h4>Registrar Saída</h4>
  <p>O processo de registro de saída é bastante similar ao de entrada:</p>
  <ol>
    <li>O campo de código de barras estará pronto para leitura ou digitação.</li>
    <li>Informe a quantidade de itens que estão saindo do estoque.</li>
    <li>Antes de processar a saída, o sistema verifica se a quantidade solicitada está disponível em estoque.</li>
    <li>Clique no botão "Registrar Saída" para finalizar a operação.</li>
    <li>Uma mensagem de confirmação (ou de alerta, caso a quantidade seja insuficiente) será exibida.</li>
  </ol>

  <h3>🔮 Personalizações e Melhorias Futuras</h3>
  <p>Estamos sempre trabalhando para aprimorar o Gestor de Estoque. Algumas das futuras implementações planejadas incluem:</p>
  <ul>
    <li>🔒 Tela de login com sistema de controle de acesso e diferentes perfis de usuários.</li>
    <li>📊 Geração de relatórios personalizáveis em formatos PDF e Excel para análise de estoque e movimentações.</li>
    <li>📤📥 Funcionalidades de exportação e importação de dados em massa, facilitando a gestão de grandes volumes de informações.</li>
  </ul>

  <h3>🤝 Contribuidores e Manutenção</h3>
  <p>Desenvolvido com paixão por Felipe Fause.</p>
  <p>Sinta-se à vontade para contribuir com sugestões, relatórios de bugs ou pull requests!</p>
</div>
