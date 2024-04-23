# Criando um Projeto com Interface Gráfica Utilizando a Linguagem Python

Este é um projeto desenvolvido como parte do curso "Criando um Projeto com Interface Gráfica Utilizando a Linguagem Python" da Escola Virtual Bradesco. O objetivo deste projeto é aplicar os conceitos aprendidos no curso para criar uma interface gráfica utilizando a linguagem Python.

## Descrição do Projeto

O projeto consiste na criação de uma aplicação com interface gráfica que oferece funcionalidades básicas, como:

- Exibição de elementos gráficos, como botões, campos de texto e janelas.
- Interação com o usuário através de cliques de mouse e entradas de teclado.
- Implementação de lógica para processar e responder às interações do usuário.
- Utilização de bibliotecas gráficas como Tkinter, PyQt ou Kivy.

## Instalação

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

2. Instale o Kivy

   2.1. Instale as dependências

   Antes que o Kivy possa ser instalado, o Python e o pip precisam ser pré-instalados. Em seguida, inicie um novo terminal que tenha Python disponível. No terminal, atualize o pip e outras dependências de instalação para que você tenha a versão mais recente da seguinte maneira (para usuários do Linux, pode ser necessário substituir python3 em vez de python e também adicionar um sinalizador --user nos comandos subsequentes fora do ambiente virtual):

   ```shell
   python -m pip install --upgrade pip setuptools virtualenv
   ```

   2.2. Crie um ambiente virtual

   Crie um novo ambiente virtual para o seu projeto Kivy. Um ambiente virtual evitará possíveis conflitos de instalação com outras versões e pacotes do Python. É opcional, mas altamente recomendado:

   ```shell
   python -m venv kivy_venv
   ```

   2.3 Ative o ambiente virtual

   Você terá que executar esta etapa no diretório atual sempre que iniciar um novo terminal. Isso configura o ambiente para que o novo Python kivy_venv seja usado:

   Para Windows CMD, na linha de comando:

   ```shell
   kivy_venv\Scripts\activate
   ```

   Se você estiver em um terminal bash no Windows, faça:

   ```shell
   source kivy_venv/Scripts/activate
   ```

   Se você estiver no Linux ou macOS, faça:

   ```shell
   source kivy_venv/bin/activate
   ```

   2.4 Instale o Kivy

   O mais simples é instalar a versão estável atual do kivy e, opcionalmente, kivy_examples das rodas PyPi fornecidas pela equipe kivy. Simplesmente faça:

   ```shell
   python -m pip install "kivy[base]" kivy_examples
   ```

   Pronto, agora o seu ambiente está configurado para rodar uma aplicação gráfica com o Kivy.

## Executar a aplicação

Execute qualquer arquivo .py pelo terminal com o comando:

    ```shell
    py nome_arquivo.py
    ```

    ou

    ```shell
    python nome_arquivo.py
    ```

    ou

    ```shell
    python3 nome_arquivo.py
    ```
