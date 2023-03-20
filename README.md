# Teste de Desenvolvimento Django

## Introdução

O objetivo deste teste de programação é avaliar suas habilidades e conhecimento em Python, e mais especificamente no framework web Django.

## Cenário

O time da IGS está crescendo todos os meses, e agora precisamos ter uma aplicação para gerenciar a informação dos colaboradores, como o nome, endereço de e-mail, e departamento. Como é o caso em todas as aplicações escritas na IGS, ela deverá ter uma API para permitir integrações.

## Requisitos

O aplicativo "IGS Employee Manager" deverá conter:

- Um painel no site administrativo do Django, para gerenciar dados de colaboradores e de departamentos
- Uma API Django com métodos para:
  - Listar, adicionar e remover colaboradores
  - Listar, adicionar e remover departamentos
- Um website público em Django ( fora do painel de administração, e sem necessidade de autenticação ) com uma única página contendo um tabela simples listando todos os colaboradores e seus departamentos. A página não precisa utilizar a API criada no item acima e pode ser implementado como uma view.

## Critérios de Aceite

- O código-fonte do projeto deve ser entregue como um repositório no site github.bom, com instruções em um arquivo README.md sobre sua execução;
- Devem existir modelos independentes (porém relacionados) para as entidades de colaboradores, e de departamentos;
- Todos os nomes de variáveis, métodos, objetos, classes e propriedades devem ser escritos em inglês;
- Todos os campos devem seguir tipos de dados coerentes e conter as validações relevantes;
- As boas práticas de codificação do Django e de Python devem ser seguidas;

## Pontos bônus!

Sinta-se livre para adicionar recursos ao projeto se você tiver o tempo e conhecimento para fazê-lo - como aumentar a testabilidade, leitura, gestão de ambiente de desenvolvimento e execução, ou documentação de API. Fique à vontade também para adicionar no arquivo README ou no próprio código comentários sobre suas decisões e abordagens técnicas ao desafio.

## Rotas da API

|  Rota Base |  Rota Complementar |  Descrição |
|---|---|---|
| http://127.0.0.1:8000/  | admin/  |  Acessar o painel no site administrativo do Django, |
|  http://127.0.0.1:8000/ | employee/  | Listar todos os colaboradores ou adicionar novo colaborador  |
| http://127.0.0.1:8000/  | employee/\<int:id>/  | Deletar um colaborador específico ou ver informações sobre um colaborador específico  |
|  http://127.0.0.1:8000/ |  employee/list-all/ | Website público em Django com uma única página contendo um tabela simples listando todos os colaboradores e seus departamentos |
| http://127.0.0.1:8000/  | department/  |  Listar todos os departamentos ou adicionar novo departamento |
|  http://127.0.0.1:8000/ | department/\<str:department>  | Deletar um departamento específico ou ver informações sobre um departamento específico |



## Exemplo da API

### Requisição

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

### Resposta

```
[
  {
    "name": "Jose da Silva",
    "email": "jose.silva@igs-software.com.br",
    "department": "Tester"
  },
  {
    "name": "Jose dos Santos",
    "email": "jose.santos@igs-software.com.br",
    "department": "Developer"
  },
  {
    "name": "Jose Lima",
    "email": "jose.lima@igs-software.com.br",
    "department": "RH"
  }
]
```
