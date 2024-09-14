<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Python Amazon Scraper</title>
</head>
<body>
    <h1>Python Amazon Scraper com Selenium e MongoDB</h1>
    <p>
        Este é um projeto em Python que utiliza a biblioteca Selenium para automatizar a busca de informações de produtos 
        na Amazon por meio do navegador Firefox. Os dados coletados são processados e armazenados em um banco de dados 
        NoSQL MongoDB, com saída em formato JSON.
    </p>
    <h2>Funcionalidades</h2>
    <ul>
        <li>Pesquisa automatizada de produtos na Amazon com Selenium.</li>
        <li>Coleta de informações como título, preço, link e imagem dos produtos.</li>
        <li>Armazenamento dos dados coletados em um banco de dados MongoDB.</li>
        <li>Geração de arquivo JSON com os dados obtidos.</li>
    </ul>
    <h2>Requisitos</h2>
    <p>Certifique-se de que você tenha os seguintes pacotes e ferramentas instalados:</p>
    <ul>
        <li><strong>Python 3.x</strong></li>
        <li><strong>Selenium</strong> (<code>pip install selenium</code>)</li>
        <li><strong>Firefox</strong> e <strong>Geckodriver</strong> (Para Firefox, o driver pode ser baixado 
        <a href="https://github.com/mozilla/geckodriver/releases" target="_blank">aqui</a>)</li>
        <li><strong>MongoDB</strong> (Instale e configure o MongoDB no seu ambiente)</li>
        <li><strong>PyMongo</strong> (<code>pip install pymongo</code>)</li>
    </ul>
    <h2>Instalação</h2>
    <ol>
        <li>Clone este repositório:
            <pre><code>git clone https://github.com/seu-usuario/amazon-scraper.git</code></pre>
        </li>
        <li>Instale as dependências necessárias:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Configure o MongoDB:
            <ul>
                <li>Certifique-se de que o MongoDB está rodando localmente ou em um servidor remoto.</li>
                <li>Atualize o script Python com a URI de conexão do MongoDB, se necessário.</li>
            </ul>
        </li>
        <li>Baixe o <strong>Geckodriver</strong> e adicione-o ao seu PATH ou especifique o caminho no script.</li>
    </ol>
    <h2>Uso</h2>
    <ol>
        <li>Execute o programa para iniciar a automação de busca:
            <pre><code>python amazon_scraper.py</code></pre>
        </li>
        <li>O script irá abrir o navegador Firefox, procurar os produtos na Amazon conforme os parâmetros configurados no código e compilar as informações coletadas em um arquivo JSON.</li>
        <li>Os dados serão armazenados no MongoDB, em uma coleção chamada <code>amazon_products</code>.</li>
    </ol>
    <h2>Estrutura de Saída</h2>
    <p>Os dados coletados serão armazenados no MongoDB e também estarão disponíveis no seguinte formato JSON:</p>
    <pre><code>{
    "produto": "Nome do Produto",
    "preco": "R$ 100,00",
    "avaliacao": "4.5 de 5 estrelas",
    "url": "https://www.amazon.com/produto-exemplo"
}</code></pre>
    <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir uma <em>issue</em> ou <em>pull request</em> se desejar melhorar este projeto.</p>
    <h2>Licença</h2>
    <p>Este projeto é licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.</p>
</body>
</html>
