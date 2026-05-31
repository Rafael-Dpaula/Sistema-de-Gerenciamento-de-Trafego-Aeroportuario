# Sistema de Gerenciamento de Tráfego Aeroportuário

## Descrição do Projeto

O Sistema de Gerenciamento de Tráfego Aeroportuário tem como objetivo simular o controle operacional de aeronaves em um aeroporto, permitindo o gerenciamento de pousos, decolagens, pistas, plataformas e planos de voo.

O sistema foi desenvolvido utilizando Programação Orientada a Objetos (POO) e padrões de projeto da Gang of Four (GoF), visando promover modularidade, reutilização de código e facilidade de manutenção.

---

## Objetivos

- Gerenciar aeronaves de diferentes categorias.
- Controlar pousos e decolagens.
- Gerenciar pistas e plataformas.
- Monitorar alterações de estado das aeronaves.
- Aplicar conceitos de Programação Orientada a Objetos.
- Implementar padrões de projeto GoF.

---

## Diagrama de Classes

![Diagrama UML](./docs/uml.png)

---

## Classes do Sistema

### Aeroporto

Responsável por representar o aeroporto e armazenar suas pistas e plataformas.

#### Atributos
- nome
- codigo
- cidade

#### Responsabilidades
- Gerenciar pistas.
- Gerenciar plataformas.

---

### Pista

Representa uma pista de pouso e decolagem.

#### Atributos
- codigo
- ocupada

#### Responsabilidades
- Indicar disponibilidade para pouso e decolagem.

---

### Plataforma

Representa uma posição de estacionamento de aeronaves.

#### Atributos
- numero
- ocupada

#### Responsabilidades
- Receber aeronaves após pouso.
- Disponibilizar aeronaves para decolagem.

---

### PlanoVoo

Representa as informações operacionais de um voo.

#### Atributos
- origem
- destino
- horarioPartida
- horarioChegada
- altitudeCruzeiro

#### Responsabilidades
- Armazenar informações de voo.
- Validar dados do plano de voo.

---

### Avião

Classe base para todas as aeronaves do sistema.

#### Atributos
- identificador
- modelo
- estado
- observadores

#### Responsabilidades
- Alterar estado operacional.
- Notificar observadores.
- Gerenciar plano de voo.

---

### Comercial

Especialização da classe Avião destinada ao transporte de passageiros.

#### Atributos
- companhiaAerea
- numeroPassageiros

---

### Privado

Especialização da classe Avião destinada ao uso particular.

#### Atributos
- proprietario

---

### Transporte

Especialização da classe Avião destinada ao transporte de cargas.

#### Atributos
- tipoCarga
- pesoCarga

---

### ControleDeVoo

Responsável pelo gerenciamento do tráfego aeroportuário.

#### Atributos
- aeronaves
- pistas
- filaPouso
- filaDecolagem

#### Responsabilidades
- Monitorar aeronaves.
- Autorizar pousos.
- Autorizar decolagens.
- Gerenciar filas de espera.
- Controlar utilização das pistas.

---

## Aplicação dos Pilares da POO

### Encapsulamento

Os atributos das classes são protegidos e manipulados por métodos específicos, garantindo maior segurança e controle sobre os dados.

### Herança

As classes Comercial, Privado e Transporte herdam características comuns da classe Avião, evitando duplicação de código.

### Polimorfismo

As aeronaves podem ser tratadas genericamente como objetos do tipo Avião, independentemente de sua especialização.

### Abstração

As classes representam entidades do mundo real, abstraindo apenas as características necessárias para o funcionamento do sistema.

---

## Padrões de Projeto Utilizados

### Factory Method

O padrão Factory Method foi utilizado para centralizar a criação de aeronaves.

A classe FactoryAvioes é responsável por instanciar os diferentes tipos de aeronaves (Comercial, Privado e Transporte), desacoplando a criação dos objetos do restante do sistema.

#### Benefícios
- Redução de dependências.
- Facilidade de expansão para novos tipos de aeronaves.
- Centralização da lógica de criação.

---

### Observer

O padrão Observer foi utilizado para permitir a comunicação entre as aeronaves e o Controle de Voo.

Quando uma aeronave altera seu estado operacional, ela notifica automaticamente os observadores registrados, permitindo que o Controle de Voo reaja aos eventos ocorridos.

#### Benefícios
- Baixo acoplamento.
- Comunicação automática entre objetos.
- Facilidade de expansão para novos observadores.

---

### State

O padrão State foi utilizado para representar os diferentes estados operacionais de uma aeronave.

Cada estado foi modelado como uma classe específica, permitindo alterar o comportamento da aeronave conforme seu estado atual.

#### Estados Implementados
- EmSolo
- AguardandoDecolagem
- EmVoo
- SolicitandoPouso
- Pousando

#### Benefícios
- Eliminação de grandes estruturas condicionais.
- Facilidade para adicionar novos estados.
- Melhor organização do comportamento da aeronave.

---

### Singleton

O padrão Singleton foi aplicado à classe ControleDeVoo.

Esse padrão garante que exista apenas uma instância responsável pelo gerenciamento do tráfego aeroportuário durante toda a execução do sistema.

#### Benefícios
- Controle centralizado.
- Consistência das informações.
- Evita múltiplas instâncias conflitantes.

---

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos
- UML
- Padrões de Projeto GoF

---

## Autor

- Rafael Albuquerque de Paula