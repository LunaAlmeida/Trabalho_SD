<h1>Trabalho Prático de Sistemas Distribuídos</h1>

### Algoritmo de Exclusão Mútua distribuído baseado no Token Ring e baseado em privilégio
Algoritmo baseado em ficha que circula ao redor do anel lógico, se o processo quer acessar a região crítica e tem a ficha, usa a região crítica e quando acaba passa a ficha, se não quer usar a região crítica passa a ficha.

> #### Descrição geral 
Esse trabalho tem como objetivo implementar uma simulação do funcionamento do algoritmo de exclusão mútua distribuído baseado no Token Ring e baseado em privilégio. Foi utilizada a linguagem Python e a biblioteca Tkinter para implementar a simulação.

> ####  Requistos funcionais
- [x] Possibilitar que o usuário escolha a quantidade de processos que serão simulados no sistema;
- [x] Simular o anel em que a ficha percorrerá;
- [x] Simular a ficha indo e voltando da região crítica;
- [x] Definir tempos aleatórios para cada processo passar na região crítica;
- [x] Ter um botão que passa de uma função para outra no código;
- [x] Ter um painel mostrando as informações:
  * Id do rocesso na região crítica;
  * A região crítica está sendo acessada;
  * A região crítica está sendo liberada;
  * Requisição foi atendida.
     
> ####  Softwares necessários
  - Python 3;
  - Biblioteca Tkinter que pode ser instalada com a seguinte instrução: pip install tk.

> ####  Como utilizar
  1. Baixe o código em sua máquina;
  2. Execute o código utilizando o comando _python main.py_;
  3. Escolha a quantidade dos processos que deseja simular;
  4. Clique no botão _Passar token_ para que a ficha seja passada de um processo para o outro.


> ####  Funcionamento
A ficha sempre começará no nó zero e aleatoriamente será decidido no código se ele deseja entrar ou não na região crítica. Se o processo decidir entrar na região crítica a ficha que é uma bolinha amarela se deslocará até a região crítica. Quando a ficha passa de um processo para outro este pisca na cor amarela. A ficha é passada automaticamente para o próximo processo se o processo anterior no anel acessou a região crítica. Os processos são identificados pelo seu número de identificação criado no início do código.

### Principais funções
1. **setup_initial_screen**: Gera a tela inicial em que são escolhidas as quantidades de processos;
2. **setup_simulation**: Define o tempo de acesso de cada processo na região crítica e chama a próxima tela onde ocorre a simulação;
3. **create_widgets**: Cria o anel, o quadrado que representa a região crítica e o botão onde será passada a ficha;
4. **update_info_panel**: Função responsável por atualizar as informações sobre o sistema no painel.

### Conclusão
Através da simulação pode-se ver o funcionamento do algoritmo de exclusão mútua distribuído baseado no Token Ring, ele é baseado em privilégio pois o processo que contém a ficha é o processo privilegiado que terá acesso a região crítica.
