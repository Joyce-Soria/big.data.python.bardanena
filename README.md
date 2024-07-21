# Bar da Nena

Este projeto é um estudo de caso de Big Data e Power BI aplicado ao "Bar da Nena". O objetivo é demonstrar como coletar, processar, analisar e visualizar grandes volumes de dados em tempo real usando ferramentas e tecnologias como Python.

## Motivação e Origem dos Dados

Este projeto foi desenvolvido com dados fictícios pelo fato da região onde moro ser rural e não possuir comércios próximos. As partes envolvidas nesta atividade são fictícias, e os dados gerados para este estudo de caso visam simular um cenário realista de um bar em uma área urbana.

## Estrutura do Projeto

1. **Coleta de Dados**
    - Geração de dados fictícios de vendas, clientes e localização do bar.
2. **Processamento de Dados**
    - Utilização de bibliotecas como Pandas e NumPy para processar e limpar os dados.
3. **Análise de Dados**
    - Análise de vendas por mês, previsão de clientes para o próximo mês e análise de dados de clientes.
4. **Visualização de Dados**
    - Utilização de Plotly para criar gráficos interativos.
    - Criação de uma interface interativa com Streamlit.

## Como Executar

1. Crie um ambiente virtual e instale as dependências:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scriptsctivate`
    pip install -r requirements.txt
    ```

2. Gere os dados fictícios:

    ```bash
    python src/generate_data.py
    ```

3. Execute a análise de dados:

    ```bash
    python src/analysis.py
    ```

4. Inicie a aplicação Streamlit:

    ```bash
    streamlit run src/app.py
    ```

## Dependências

- pandas
- numpy
- plotly
- streamlit
- scikit-learn
- faker
