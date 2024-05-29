# Restaurant Orders

Este projeto é uma aplicação de gerenciamento de um restaurante que inclui a geração dinâmica de cardápios considerando restrições alimentares e a disponibilidade de ingredientes em estoque.


## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

O projeto consiste na implementação de uma aplicação destinada a gerenciar os cardápios de um restaurante. A aplicação permite gerar cardápios dinâmicos que respeitam restrições alimentares e consideram a disponibilidade dos ingredientes em estoque. A funcionalidade é implementada através da integração dos módulos de controle de estoque e de dados do menu.

## Tecnologias Utilizadas

- Python
- FastAPI
- CSV
- Pytest

## Instalação

Para instalar e executar este projeto localmente, siga as instruções abaixo:

1. Clone o repositório:
    ```sh
    git@github.com:matheusrosa1/restaurant-orders.git
    cd restaurant-orders
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Como Usar

1. Certifique-se de que você tem os dados necessários nos arquivos CSV em `data/`:
    - `menu_base_data.csv`: Dados dos pratos do menu.
    - `inventory_base_data.csv`: Dados do estoque de ingredientes.

2. Utilize a classe `MenuBuilder` para gerar o cardápio:
    ```python
    from src.services.menu_builder import MenuBuilder

    menu_builder = MenuBuilder()
    menu = menu_builder.get_main_menu()
    print(menu)
    ```

###Executando a aplicação

Para ver a aplicação rodando com as funcionalidades implementadas, use o comando a seguir:

`python3 -m uvicorn app:app`


## Contribuição

Para contribuir com o projeto, siga os passos abaixo:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Licença [MIT](https://github.com/matheusrosa1/restaurant-orders/?tab=MIT-1-ov-file) 

## Contato

Para mais informações, entre em contato com os mantenedores do projeto:

- GitHub: [matheusrosa1](https://github.com/matheusrosa1/)
- E-mail: matheusrosataxa@gmail.com
