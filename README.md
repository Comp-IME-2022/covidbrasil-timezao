# Evolução do covid 19 no Brasil

## Como usar

O programa roda utilizando a biblioteca [streamlit](https://www.streamlit.io/) do python.

Como os dados são atualizados diaramente, é necessário baixar o arquivo `csv` no [site](https://covid.saude.gov.br/) do Ministério da Saúde,
ao baixar o arquivo atualizado, é necessário coloca-lo em uma pasta chamada `data` na raiz do diretório.
Então, precisamos mudar o nome do arquivo em `params.yaml` para o nome do arquivo baixado do site.
Por fim, na raiz do diretório realizamos o seguinte comando:

```
streamlit run run.py
```

Se tudo ocorrer como esperado, o terminal mostrará a url onde a aplicação está rodando.
