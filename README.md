## Busca leads
### Pacotes e bibliotecas utilizadas
- Pandas
- re
- os
- unidecode

### Projeto

O algoritmo que se segue tem como objetivo buscar leads para prospecção a partir de uma busca no google maps, para buscar as informações foi utilizada uma extensão do próprio google que faz o crawler dessas informações chamado Instant Data Scraper e para baixa-la basta acessar o link:  https://chromewebstore.google.com/detail/instant-datascraper/ofaokhiedipichpaobibbnahnkdoiiah 

Após baixar acesse o google e faça a pesquisa, exemplo “loja de carros no estado de são paulo”  

![Imagem1](https://github.com/LucasGuimaDev/busca-leads/assets/123521555/5b6f4d2a-81fb-43d5-9784-5027272b092f)

 
Desça a página até encontrar a opção “Mais lugares” e clique. 
A página a seguir vai se abrir, então clique em extensões e selecione a extensão do Instant Data Scraper 

![Imagem2](https://github.com/LucasGuimaDev/busca-leads/assets/123521555/46302aeb-d925-4fbf-a396-bddc9446acba)

 
Clique em Locate “Next” button e então clique na opção de mais no final da página, selecione o tempo de delay para a coleta dos dados e então clique em Start crawling 

![Imagem3](https://github.com/LucasGuimaDev/busca-leads/assets/123521555/0813cb39-e3e5-411b-8832-96112426f072)

Então ele vai começar a coleta dos dados 
Após coletar os dados ele mostra a seguinte mensagem, então basta salvar o arquivo em excel 

![Imagem4](https://github.com/LucasGuimaDev/busca-leads/assets/123521555/013234f5-8d60-4219-b07e-491ec552d360)

Após a coleta jogue o arquivo na pasta de arquivos arquivos_xlsx e rode o código para extrair os dados em csv. 
