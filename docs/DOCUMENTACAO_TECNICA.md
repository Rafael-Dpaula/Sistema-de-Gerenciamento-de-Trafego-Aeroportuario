# Prompt utilizado para geração desta documentação:
Você atuará como um Arquiteto de Software Sênior, Analista de Sistemas, Engenheiro de Software e Especialista em Engenharia Reversa.

Sua missão é analisar integralmente um projeto orientado a objetos em Python e produzir uma documentação técnica completa, detalhada e definitiva do sistema.

O objetivo desta documentação é eliminar a necessidade de futuras explicações humanas sobre o projeto.

Após ler o código-fonte, qualquer desenvolvedor ou agente de IA deverá ser capaz de:

* compreender completamente a arquitetura;
* compreender todas as decisões de modelagem;
* compreender os padrões de projeto utilizados;
* compreender o fluxo operacional do sistema;
* compreender as responsabilidades de cada módulo;
* compreender como as classes se comunicam;
* compreender o estado atual do desenvolvimento;
* identificar facilmente pontos de melhoria;
* continuar o desenvolvimento sem auxílio do autor original.

---

# CONTEXTO DO PROJETO

O projeto consiste em um Sistema de Gerenciamento de Tráfego Aéreo desenvolvido em Python utilizando Programação Orientada a Objetos.

O sistema foi desenvolvido com forte foco acadêmico e arquitetural.

O principal objetivo não é criar uma simulação gráfica, mas modelar corretamente o domínio aeroportuário utilizando conceitos avançados de orientação a objetos.

Durante o desenvolvimento foram aplicados diversos padrões de projeto e princípios de engenharia de software.

---

# PADRÕES DE PROJETO IDENTIFICADOS

O sistema utiliza:

## State Pattern

Responsável pelo controle dos estados operacionais das aeronaves.

As aeronaves não alteram comportamento através de condicionais.

O comportamento muda dinamicamente através da troca de estados.

Estados atualmente identificados:

* EmSolo
* AguardandoDecolagem
* Decolando
* EmVoo
* SolicitandoPouso
* Pousando
* EmEmergencia

Cada estado implementa:

* solicitarPouso()
* solicitarDecolagem()
* pousar()
* decolar()
* declararEmergencia()

Cada operação retorna um objeto contendo:

* próximo estado
* mensagem operacional

A aeronave recebe esse retorno e realiza a troca de estado.

---

## Observer Pattern

As aeronaves funcionam como Subjects.

O ControleVoo funciona como Observer.

Mudanças de estado notificam automaticamente os observadores cadastrados.

Objetivo principal:

* monitoramento das aeronaves;
* gerenciamento de prioridades;
* tratamento automático de emergências.

Atualmente o Observer é utilizado principalmente para emergências, porém sua arquitetura permite expandir para:

* solicitações de pouso;
* solicitações de decolagem;
* registro de eventos;
* histórico operacional.

---

## Singleton Pattern

ControleVoo é implementado como Singleton.

Objetivo:

Garantir existência de apenas um centro controlador de tráfego aéreo.

Características:

* instância única;
* reutilização global;
* inicialização protegida.

---

## Factory Method

Criação de aeronaves centralizada.

A Factory recebe parâmetros e retorna instâncias concretas.

Tipos atualmente previstos:

* Comercial
* Privado
* Transporte

Objetivo:

Desacoplar criação e utilização das aeronaves.

---

# DECISÕES ARQUITETURAIS IMPORTANTES

O documento deve destacar explicitamente as seguintes decisões tomadas durante o desenvolvimento:

## ControleVoo NÃO controla infraestrutura física

O ControleVoo conhece:

* aeronaves;
* filas de pouso;
* filas de decolagem;
* eventos operacionais.

O ControleVoo NÃO conhece:

* pistas;
* plataformas;
* aeroporto.

Motivo:

Separação de responsabilidades.

---

## Aeroporto controla infraestrutura física

O Aeroporto é responsável por:

* armazenar pistas;
* armazenar plataformas;
* disponibilizar pista livre;
* disponibilizar plataforma livre.

---

## CentroOperacional

Foi criada uma camada intermediária chamada CentroOperacional.

Objetivo:

Evitar acoplamento entre:

* Aeroporto
* ControleVoo

O CentroOperacional funciona como coordenador operacional.

Responsabilidades:

* autorizar pousos;
* autorizar decolagens;
* alocar pistas;
* alocar plataformas;
* processar movimentações de aeronaves.

Fluxo:

Aeronave
↓
ControleVoo
↓
CentroOperacional
↓
Infraestrutura física

---

## Composição

Aeroporto possui composição com:

* Pista
* Plataforma

As pistas e plataformas não existem sem o aeroporto.

---

# REGRAS DE ENCAPSULAMENTO

O projeto passou por uma refatoração.

Não utilizar atributos privados com "__atributo" como padrão principal.

Utilizar:

```python
_atributo
```

com acesso externo via properties.

Exemplo:

```python
@property
def identificador(self):
    return self._identificador
```

Motivo:

Evitar name mangling do Python.

Problema encontrado anteriormente:

```python
_Aviao__identificador
_Privado__identificador
```

A nova convenção utiliza:

```python
_identificador
```

em todas as classes.

---

# PROBLEMAS JÁ ENFRENTADOS

O documento deve registrar as dificuldades encontradas durante o desenvolvimento.

## Import Circular

Problema ocorreu nos estados.

Exemplo:

```text
EmEmergencia -> Pousando
Pousando -> EmEmergencia
```

Solução adotada:

Imports locais dentro dos métodos.

Exemplo:

```python
def declararEmergencia(self):
    from Models.States.EmEmergencia import EmEmergencia
```

Essa decisão deve ser documentada.

---

# DOCUMENTAÇÃO OBRIGATÓRIA

Produza as seções abaixo.

NÃO omita nenhuma.

---

# 1. VISÃO GERAL DO SISTEMA

Explicar:

* objetivo;
* escopo;
* domínio de negócio;
* motivação.

---

# 2. ARQUITETURA GERAL

Explicar:

* camadas;
* componentes;
* responsabilidades.

Criar diagramas textuais.

Exemplo:

```text
Aeronave
   ↓
ControleVoo
   ↓
CentroOperacional
   ↓
Aeroporto
   ↓
Pistas / Plataformas
```

---

# 3. ÁRVORE COMPLETA DO PROJETO

Reconstruir toda a estrutura de diretórios.

Exemplo:

```text
Models/
├── Avioes/
├── Factory/
├── Observer/
├── States/
├── ...
```

---

# 4. INVENTÁRIO DE CLASSES

Para CADA classe encontrada informar:

* nome;
* objetivo;
* atributos;
* métodos;
* relacionamentos;
* dependências;
* observações.

---

# 5. DIAGRAMA TEXTUAL DE RELACIONAMENTOS

Explicar:

* associação;
* agregação;
* composição;
* dependência.

---

# 6. PADRÕES DE PROJETO

Explicar detalhadamente:

* onde estão;
* por que foram usados;
* vantagens obtidas.

---

# 7. STATE MACHINE

Gerar tabela completa contendo:

Estado Atual
Evento
Próximo Estado
Resultado

Mapear todas as transições.

---

# 8. FLUXO DE DECOLAGEM

Descrever passo a passo.

Desde:

Aeronave em solo

até:

Aeronave em voo.

---

# 9. FLUXO DE POUSO

Descrever passo a passo.

Desde:

Aeronave em voo

até:

Aeronave estacionada.

---

# 10. FLUXO DE EMERGÊNCIA

Descrever:

* declaração;
* priorização;
* impacto nas filas.

---

# 11. FLUXO OBSERVER

Explicar detalhadamente:

* quem observa;
* quem é observado;
* quando ocorre notificação.

---

# 12. FLUXO DE EXECUÇÃO

Explicar uma execução típica do sistema.

Criar um cenário completo.

Exemplo:

* criar aeroporto;
* criar infraestrutura;
* criar aeronave;
* solicitar decolagem;
* decolar;
* solicitar pouso;
* pousar.

---

# 13. ANÁLISE DE COESÃO E ACOPLAMENTO

Avaliar:

* pontos fortes;
* pontos fracos;
* riscos arquiteturais.

---

# 14. DÉBITOS TÉCNICOS

Listar:

* inconsistências;
* melhorias;
* funcionalidades incompletas.

---

# 15. ROADMAP DE CONTINUIDADE

Criar plano de evolução.

Prioridade Alta
Prioridade Média
Prioridade Baixa

Explicar exatamente o que deve ser implementado em seguida.

---

# 16. RESUMO EXECUTIVO

Gerar uma síntese final capaz de explicar toda a arquitetura para outro desenvolvedor em poucos minutos.

---

INSTRUÇÃO FINAL:

A documentação deve ser extremamente detalhada.

Assuma que o leitor nunca viu o projeto anteriormente.

Sempre explique:

* O QUE existe.
* POR QUE existe.
* COMO funciona.
* COMO interage com o restante do sistema.
* QUAIS consequências uma alteração causaria.

Nenhuma decisão arquitetural deve ficar sem justificativa.


# Documentação Técnica Definitiva — Sistema de Gerenciamento de Tráfego Aéreo (POO em Python)

> **Escopo desta documentação**: tornar o sistema completamente compreensível para qualquer desenvolvedor (ou agente de IA) que não viu o projeto antes, eliminando a necessidade de explicações adicionais “humanas”.
>
> **Projeto**: `SistemaGerenciamentoAeroporto/`
>
> **Linguagem/Estilo**: Programação Orientada a Objetos em Python, com uso de padrões clássicos (State, Observer, Singleton, Factory Method).
>
> **Importante**: esta documentação foi reconstruída com base no código-fonte atual presente em `SistemaGerenciamentoAeroporto/`.

---

# 1. VISÃO GERAL DO SISTEMA


## 1.1 Objetivo
O projeto modela o **domínio aeroportuário** e o **comportamento operacional de aeronaves** utilizando Programação Orientada a Objetos (POO) e padrões de projeto. O objetivo principal **não** é simular graficamente; é **modelar corretamente o domínio** e as decisões de arquitetura.

Conceitos centrais:
- Aeronaves possuem **estados operacionais** (máquina de estados).
- Aeronaves executam ações operacionais (solicitar pouso/decolagem, pousar/decolar, declarar emergência).
- O comportamento muda **dinamicamente** pelo **State Pattern** (troca de objetos de estado), não por condicionais espalhadas.
- Mudanças de estado podem disparar notificações para um **centro de controle**, via **Observer Pattern**.
- Existe um **ControleVoo** que organiza **filas** e aplica prioridade para emergências.
- O aeroporto fornece **infraestrutura física** (pistas e plataformas) independentemente do controle.

## 1.2 Escopo
Inclui:
- Classe abstrata `Aviao` + tipos concretos: `Comercial`, `Privado`, `Transporte`
- Máquina de Estados em `Models/States/*`
- Observer com `Observer` e `ControleVoo`
- Singleton com `ControleVoo`
- Factory Method com `FactoryAviao`
- Infraestrutura física com:
  - `Aeroporto` (compõe `Pista` e `Plataforma`)
  - `Pista` e `Plataforma` (ocupação/liberação)
- `PlanoVoo` com validações de domínio
- Testes (principalmente roteiros com `print`)

## 1.3 Motivação
A arquitetura foi construída para:
- **Evitar condicionais** do tipo “se estado X então ...” dentro da aeronave.
- **Localizar regras** de transição em classes de estado.
- **Desacoplar** monitoramento de eventos do comportamento operacional.
- Garantir um único controlador global com o **Singleton**.
- Centralizar a criação e validação de aeronaves com **Factory Method**.
- Preparar evolução do domínio (novos estados, novos observadores, novas regras de filas) sem reescrever a estrutura base.

---

# 2. ARQUITETURA GERAL

## 2.1 Camadas e componentes (visão textual)

```text
[Runner / Entrada]
   - main.py (vazio no estado atual)
   - Tests/* (roteiros)

         ↓ usa

Model do Domínio
   - Aviao (abstrata) — State Pattern
   - Estados em Models/States/*

   - Observer/ControleVoo — Observer Pattern
   - ControleVoo organiza filas e prioriza emergências

Infraestrutura Física
   - Aeroporto (composição) → Pistas / Plataformas
   - Pista e Plataforma gerenciam ocupação/liberação

Serviços/Entidades do domínio
   - PlanoVoo (valida coerência do plano)
   - FactoryAviao (cria aeronaves)
```

## 2.2 Responsabilidades por componente

### 2.2.1 `Aviao` (a aeronave)
Responsabilidades:
- Manter o estado atual (`_status`)
- Receber eventos públicos (`solicitarPouso`, `solicitarDecolagem`, `pousar`, `decolar`, `declararEmergencia`)
- Delegar a decisão ao objeto de estado atual (State Pattern)
- Aplicar a troca de estado retornada pelo estado
- Notificar observadores sobre mudanças (Observer Pattern)

Consequência:
- Para alterar regras por estado, modifica-se apenas a classe do estado (não a classe `Aviao`).

### 2.2.2 Estados (máquina de estados)
Responsabilidades:
- Implementar transições para eventos disponíveis
- Definir “próximo estado” e mensagem operacional
- Para operações inválidas, retornar o **mesmo estado atual** e mensagem de erro

Consequência:
- O fluxo operacional é governado por objetos e transições, não por lógica condicional na aeronave.

### 2.2.3 `ControleVoo` (centro de controle)
Responsabilidades:
- Ser o **Observer** que recebe notificações das aeronaves
- Manter:
  - filas de pouso (`_filaPouso`)
  - filas de decolagem (`_filaDecolagem`)
- Reordenar prioridade em emergência:
  - quando uma aeronave entra em `EmEmergencia`, ela recebe prioridade máxima na fila de pouso

Consequência:
- O controle reage automaticamente a mudanças de estado, sem que `Aviao` saiba detalhes das filas.

### 2.2.4 `Aeroporto` (infraestrutura física)
Responsabilidades:
- Armazenar e compor:
  - `Pista`
  - `Plataforma`
- Disponibilizar pista/plataforma livre
- Possuir uma instância `controleVoo` (Singleton)

Consequência:
- Separação de responsabilidades:
  - Controle organiza tráfego e prioriza
  - Aeroporto provê recursos físicos

> Observação: o código não implementa explicitamente o fluxo “Controle autoriza → Aeroporto ocupa recurso” de forma automática; essa integração fica para uma camada runner/camada futura.

---

# 3. ÁRVORE COMPLETA DO PROJETO

A estrutura de diretórios reconstruída no projeto:

```text
SistemaGerenciamentoAeroporto/
├── main.py
├── docs/
│   ├── uml.png
│   ├── TODO.md
│   └── DOCUMENTACAO_TECNICA.md
├── Models/
│   ├── __init__.py
│   ├── Aeroporto.py
│   ├── CentroOperacional.py
│   ├── ControleVoo.py
│   ├── Pista.py
│   ├── Plataforma.py
│   ├── PlanoVoo.py
│   ├── Avioes/
│   │   ├── Aviao.py
│   │   ├── Comercial.py
│   │   ├── Privado.py
│   │   └── Transporte.py
│   ├── Factory/
│   │   └── FactoryAvioes.py
│   ├── Observer/
│   │   └── Observer.py
│   └── States/
│       ├── State_Aviao.py
│       ├── EmSolo.py
│       ├── AguardandoDecolagem.py
│       ├── Decolando.py
│       ├── EmVoo.py
│       ├── SolicitandoPouso.py
│       ├── Pousando.py
│       └── EmEmergencia.py
└── Tests/
    ├── __init__.py
    ├── test_aviao.py
    ├── test_controleVoo.py
    ├── test_pista.py
    ├── test_planoVoo.py
    └── test_plataforma.py
```

---

# 4. INVENTÁRIO DE CLASSES

## 4.1 `Aviao(ABC)` — `Models/Avioes/Aviao.py`
**Objetivo**
- Classe base da aeronave.
- Implementa orquestração do State Pattern e disparo do Observer.

**Atributos**
- `_identificador` (str)
- `_modelo` (str)
- `_status: StateAviao` (instância de estado atual; inicia como `EmSolo()`)
- `_planoVoo: PlanoVoo | None`
- `_observadores: list[Observer]`

**Métodos**
- Setters:
  - `identificador` (strip, upper; valida não-nulo)
  - `modelo` (strip, upper; valida não-nulo)
  - `planoVoo` (deve ser `PlanoVoo` ou None)
- `definirPlano(plano: PlanoVoo)`
- `adicionarObserver(observador)`
- `removerObserver(observador)` *(validação incorreta; ver débitos técnicos)*
- `notificarObservers(mensagem)`
- `alterarStatus(estado: StateAviao)`:
  - atualiza `_status`
  - monta mensagem
  - chama `notificarObservers`
- delegações para o state:
  - `solicitarPouso()`
  - `solicitarDecolagem()`
  - `pousar()`
  - `decolar()`
  - `declararEmergencia()`

**Relacionamentos**
- “Subject lógico” do Observer: mantém lista de observadores e notifica.

**Dependências**
- `Models.States.State_Aviao.StateAviao`
- `Models.States.EmSolo.EmSolo`
- `Models.Observer.Observer.Observer`
- `Models.PlanoVoo.PlanoVoo`
- Estados concretos são instanciados/importados nos próprios estados.

**Observações**
- Não utiliza condicionais por estado.
- O estado decide a transição e retorna um objeto `informandoControle`.

---

## 4.2 `StateAviao(ABC)` e `informandoControle` — `Models/States/State_Aviao.py`
### `StateAviao(ABC)`
**Objetivo**
- Interface abstrata do State Pattern.

**Métodos abstratos**
- `solicitarPouso`
- `solicitarDecolagem`
- `decolar`
- `pousar`
- `declararEmergencia`

### `informandoControle`
**Objetivo**
- Estrutura de retorno do estado (próximo estado + mensagem).

**Atributos**
- `estado`
- `mensagem`

---

## 4.3 Estados concretos — `Models/States/*`
Todos herdam `StateAviao` e implementam os métodos.

### 4.3.1 `EmSolo`
- Transições:
  - `solicitarDecolagem` → `AguardandoDecolagem`
  - `declararEmergencia` → `EmEmergencia`
  - demais eventos → operação inválida (retorna `self`)

### 4.3.2 `AguardandoDecolagem`
- Transições:
  - `decolar` → `EmVoo`
  - `declararEmergencia` → `EmEmergencia`
  - demais → inválido (retorna `self`)

### 4.3.3 `Decolando`
- Transições:
  - `decolar` → `EmVoo`
  - `declararEmergencia` → `EmEmergencia`
  - demais → inválido (retorna `self`)

### 4.3.4 `EmVoo`
- Transições:
  - `solicitarPouso` → `SolicitandoPouso`
  - `declararEmergencia` → `EmEmergencia`
  - demais → inválido (retorna `self`)

### 4.3.5 `SolicitandoPouso`
- Transições:
  - `pousar` → `Pousando`
  - `declararEmergencia` → `EmEmergencia`
  - demais → inválido

### 4.3.6 `Pousando`
- Transições:
  - `pousar` → `EmSolo`
  - `declararEmergencia` → `EmEmergencia`
  - demais → inválido

### 4.3.7 `EmEmergencia`
- Transições:
  - `solicitarPouso` → `Pousando`
  - `declararEmergencia` → `EmEmergencia` (mantém)
  - demais eventos → inválido (retorna `self`)

**Observações comuns**
- Usam **imports locais** (dentro dos métodos) para instanciar próximos estados e mitigar import circular.

---

## 4.4 `Observer(ABC)` — `Models/Observer/Observer.py`
**Objetivo**
- Interface do Observer.

**Métodos**
- `atualizar(self, origem, mensagem)` (abstrato)

---

## 4.5 `ControleVoo(Singleton, Observer)` — `Models/ControleVoo.py`
**Objetivo**
- Centro controlador global.
- Observa aeronaves e organiza filas.
- Prioriza emergências.

**Implementação Singleton**
- `__new__` cria instância única.
- `__init__` inicializa estruturas apenas uma vez via flag `__inicializado`.

**Atributos**
- `_historicoContato: list[str]`
- `_aeronaves: list[Aviao]`
- `_filaPouso: list[Aviao]`
- `_filaDecolagem: list[Aviao]`
- `_rotulo` (setado quando passado `rotulo` no construtor)

**Métodos**
- `atualizar(origem, notificacao)`:
  - imprime notificacao
  - se `origem._status` é `EmEmergencia`:
    - remove `origem` de `_filaPouso` se existir
    - insere na posição 0 (prioridade máxima)
- Filas:
  - `solicitarPouso(aviao)`
  - `solicitarDecolagem(aviao)`
  - `autorizarPouso(aviao)` (remove da fila)
  - `autorizarDecolagem(aviao)` (remove da fila)
- Gestão:
  - `adicionarAeronave(aviao)`
  - `removerAeronave(aviao)` *(inconsistências no fluxo; ver débitos técnicos)*

**Relacionamentos**
- Observa `Aviao` (via `atualizar`).

---

## 4.6 `Aeroporto`
**Objetivo**
- Controlar infraestrutura física:
  - armazenar pistas e plataformas
  - buscar recursos livres
- Possuir `controleVoo = ControleVoo()`.

**Atributos**
- `_controleVoo: ControleVoo`
- `_pistas: list[Pista]`
- `_plataformas: list[Plataforma]`
- `nome`, `codigo`, `cidade` com properties e validações

**Métodos**
- `adicionarPista`, `adicionarPlataforma`
- `removerPista`, `removerPlataforma`
- `buscarPistaDisponivel`, `buscarPlataformaDisponivel`

---

## 4.7 `Pista`
**Objetivo**
- Representar uma pista e sua ocupação.

**Atributos**
- `_codigo: int`
- `_aviao: Aviao | None`

**Métodos**
- `ocupar(aviao)` (falha se ocupada)
- `liberar()`
- `disponivel()`

---

## 4.8 `Plataforma`
**Objetivo**
- Representar uma plataforma e sua ocupação.

**Atributos**
- `_codigo: int`
- `_aviao: Aviao | None`

**Métodos**
- `ocupar(aviao)` (falha se ocupada)
- `liberar()`
- `disponivel()`

---

## 4.9 `PlanoVoo`
**Objetivo**
- Armazenar plano de voo e validar coerência.

**Atributos**
- `_origem`, `_destino: str`
- `_horarioPartida`, `_horarioChegada: time.struct_time` (parsed com `HH:MM`)
- `_altitudeCruzeiro: int`

**Métodos**
- setters com validações
- `validarPlano() -> bool`

---

## 4.10 `FactoryAviao(Factory Method)` — `Models/Factory/FactoryAvioes.py`
**Objetivo**
- Criar aeronaves desacoplando criação do uso.

**Método**
- `criarAviao(tipo: str, **kwargs)`
  - normaliza tipo
  - valida campos obrigatórios por tipo
  - retorna:
    - `Comercial`
    - `Privado`
    - `Transporte`

---

## 4.11 Classes concretas de aeronave
### 4.11.1 `Comercial(Aviao)`
- Atributos:
  - `_companhiaAerea`, `_numeroPassageiros`
- `__str__` inclui estado atual e plano.

### 4.11.2 `Privado(Aviao)`
- Atributos:
  - `_proprietario`, `_numeroPassageiros`
- `__str__` inclui estado atual e plano.

### 4.11.3 `Transporte(Aviao)`
- Atributos:
  - `_tipoCarga`, `_pesoCarga`
- `__str__` inclui estado atual e plano.

---

# 5. DIAGRAMA TEXTUAL DE RELACIONAMENTOS

## Associação (uso direto / referência)
```text
Aviao  --->  Observer (lista _observadores)
ControleVoo  -->  Observer (herda Observer)
```

## Agregação (estrutura com vida separada)
```text
ControleVoo  --->  listas de Aviao (_filaPouso, _filaDecolagem, _aeronaves)
```

## Composição (parte não existe sem o todo, no modelo pretendido)
```text
Aeroporto  --(composição)-->  Pista
Aeroporto  --(composição)-->  Plataforma
```

## Dependência (um componente precisa do outro)
```text
Aviao  --(depende)--> StateAviao e estados concretos
Estado concreto --(depende)--> outro estado concreto ao criar instância do próximo estado
ControleVoo --(depende)--> Aviao (fila e leitura de origem._status)
```

---

# 6. PADRÕES DE PROJETO

## 6.1 State Pattern

### Onde está
- `Models/States/State_Aviao.py` (interface)
- `Models/States/*.py` (implementações)
- `Models/Avioes/Aviao.py` (orquestra `_status`)

### Por que foi usado
- Remover condicionais do tipo “se status == ... então ...” da aeronave.
- Permitir evolução do comportamento por estado.

### Vantagens obtidas
- Coesão: regras por estado ficam isoladas.
- Extensibilidade: novos estados e transições podem ser adicionados sem refatorar a aeronave.

### Consequência de mudança
- Alterar uma transição impacta diretamente a operação para aquele fluxo.
- Adicionar um evento ao `StateAviao` exige implementar métodos em todos os estados.

---

## 6.2 Observer Pattern

### Onde está
- Interface: `Models/Observer/Observer.py`
- Observador: `Models/ControleVoo.py` (ControleVoo implementa atualizar)
- Sujeito: `Models/Avioes/Aviao.py` (notifica observers ao alterar status)

### Por que foi usado
- Centralizar reações a mudanças de estado no controle.
- Permitir prioridade automática (emergências) e expansão para outros tipos de eventos.

### Vantagens obtidas
- Desacoplamento entre “mudança de estado” e “lógica de priorização”.
- Reatividade e extensibilidade.

### Consequência de mudança
- Mudanças em `ControleVoo.atualizar` alteram o comportamento reativo (ex.: prioridade).

---

## 6.3 Singleton Pattern

### Onde está
- `ControleVoo` implementa Singleton via `__new__` e flag de inicialização.

### Por que foi usado
- Evitar múltiplos controles e filas inconsistentes.

### Vantagens obtidas
- Consistência global.

### Consequência de mudança
- Alterações na inicialização única podem causar inconsistência de filas e estado global.

---

## 6.4 Factory Method

### Onde está
- `Models/Factory/FactoryAvioes.py`

### Por que foi usado
- Desacoplar criação e validação de parâmetros das classes de aeronave.

### Vantagens obtidas
- Reduz erros ao criar aeronaves.
- Padroniza requisitos por tipo.

### Consequência de mudança
- Adicionar tipo novo exige:
  - criar classe
  - estender a factory

---

# 7. STATE MACHINE

## 7.1 Eventos definidos pela interface `StateAviao`
- `solicitarPouso`
- `solicitarDecolagem`
- `decolar`
- `pousar`
- `declararEmergencia`

## 7.2 Tabela completa de transições

| Estado Atual | Evento | Próximo Estado | Resultado (comportamento) |
|---|---|---|---|
| EmSolo | solicitarDecolagem | AguardandoDecolagem | Solicitação de decolagem aceita |
| EmSolo | solicitarPouso | EmSolo | Operação inválida |
| EmSolo | decolar | EmSolo | Operação inválida |
| EmSolo | pousar | EmSolo | Operação inválida |
| EmSolo | declararEmergencia | EmEmergencia | Emergência registrada |
| AguardandoDecolagem | solicitarDecolagem | AguardandoDecolagem | “Solicitação já registrada” |
| AguardandoDecolagem | solicitarPouso | AguardandoDecolagem | Operação inválida |
| AguardandoDecolagem | decolar | EmVoo | Decolagem realizada |
| AguardandoDecolagem | pousar | AguardandoDecolagem | Operação inválida |
| AguardandoDecolagem | declararEmergencia | EmEmergencia | Emergência registrada |
| Decolando | solicitarDecolagem | Decolando | Operação inválida |
| Decolando | solicitarPouso | Decolando | Operação inválida |
| Decolando | decolar | EmVoo | Decolagem realizada |
| Decolando | pousar | Decolando | Operação inválida |
| Decolando | declararEmergencia | EmEmergencia | Emergência registrada |
| EmVoo | solicitarPouso | SolicitandoPouso | Solicitação de pouso aceita |
| EmVoo | solicitarDecolagem | EmVoo | Operação inválida |
| EmVoo | decolar | EmVoo | Operação inválida |
| EmVoo | pousar | EmVoo | Operação inválida |
| EmVoo | declararEmergencia | EmEmergencia | Emergência declarada |
| SolicitandoPouso | solicitarPouso | SolicitandoPouso | “Solicitação já registrada” |
| SolicitandoPouso | solicitarDecolagem | SolicitandoPouso | Operação inválida |
| SolicitandoPouso | decolar | SolicitandoPouso | Operação inválida |
| SolicitandoPouso | pousar | Pousando | Pouso autorizado |
| SolicitandoPouso | declararEmergencia | EmEmergencia | Emergência declarada |
| Pousando | solicitarPouso | Pousando | Operação inválida |
| Pousando | solicitarDecolagem | Pousando | Operação inválida |
| Pousando | decolar | Pousando | Operação inválida |
| Pousando | pousar | EmSolo | Pouso concluído |
| Pousando | declararEmergencia | EmEmergencia | Emergência registrada durante aproximação |
| EmEmergencia | solicitarPouso | Pousando | Pouso emergencial autorizado |
| EmEmergencia | solicitarDecolagem | EmEmergencia | Operação inválida |
| EmEmergencia | decolar | EmEmergencia | Operação inválida |
| EmEmergencia | pousar | EmEmergencia | Operação inválida (pouso emergencial antes) |
| EmEmergencia | declararEmergencia | EmEmergencia | Emergência já registrada (mantém) |

---

# 8. FLUXO DE DECOLAGEM

## 8.1 Estado inicial
- A aeronave inicia em `EmSolo()` dentro do construtor `Aviao.__init__`.

## 8.2 Passo a passo (do ponto de vista do State Machine)

1) **EmSolo**
- Evento: `solicitarDecolagem()`
- Transição:
  - `EmSolo.solicitarDecolagem()` → `AguardandoDecolagem`

2) **AguardandoDecolagem**
- Evento: `decolar()`
- Transição:
  - `AguardandoDecolagem.decolar()` → `EmVoo`

3) Estado final do fluxo:
- aeronave em `EmVoo`

## 8.3 Regra adicional importante (plano de voo)
No método público `Aviao.solicitarDecolagem()`:
- se `_planoVoo is None`, ele imprime um alerta e retorna `""` (não aplica transição).

Consequência:
- O runner deve chamar `aviao.definirPlano(...)` antes de solicitar a decolagem.

---

# 9. FLUXO DE POUSO

## 9.1 Estado inicial
- Esperado: aeronave em `EmVoo`.

## 9.2 Passo a passo

1) **EmVoo**
- Evento: `solicitarPouso()`
- Transição:
  - `EmVoo.solicitarPouso()` → `SolicitandoPouso`

2) **SolicitandoPouso**
- Evento: `pousar()`
- Transição:
  - `SolicitandoPouso.pousar()` → `Pousando`

3) **Pousando**
- Evento: `pousar()`
- Transição:
  - `Pousando.pousar()` → `EmSolo`

## 9.3 Consequências (infraestrutura)
O estado `EmSolo` não “ocupa” automaticamente `Plataforma`.
A integração com infraestrutura (ex.: `aero.buscarPlataformaDisponivel()` e `plataforma.ocupar(aviao)`) depende do runner/camada futura.

---

# 10. FLUXO DE EMERGÊNCIA

## 10.1 Declaração de emergência
- Qualquer estado que implemente `declararEmergencia()` (e retorne `EmEmergencia`) fará:
  - `Aviao.alterarStatus(EmEmergencia())`
  - notificação via Observer (`notificarObservers`)

## 10.2 Impacto na priorização
Quando o status muda para `EmEmergencia`, o `ControleVoo.atualizar(...)` detecta:

- `type(origem._status).__name__ == "EmEmergencia"`
- então reordena a fila:
  - remove `origem` da fila de pouso se existir
  - insere em `_filaPouso` na posição 0

## 10.3 Efeito no fluxo de pouso
No estado `EmEmergencia`:
- evento `solicitarPouso()` → `Pousando` (pouso emergencial autorizado)
- em seguida, `pousar()` leva a `EmSolo`.

---

# 11. FLUXO OBSERVER

## 11.1 Quem observa?
- `ControleVoo` observa aeronaves.

## 11.2 Quem é observado?
- `Aviao` (não herda explicitamente Observer, mas funciona como “Subject lógico”):
  - mantém `_observadores`
  - chama `observer.atualizar(self, mensagem)` no método `alterarStatus`.

## 11.3 Quando ocorre notificação?
- Sempre que `Aviao.alterarStatus(...)` é executado:
  1) troca `_status`
  2) monta mensagem
  3) chama `notificarObservers(mensagem)`
  4) cada observador recebe `atualizar(self, mensagem)`

## 11.4 Consequência prática
- A prioridade em emergência acontece no método `ControleVoo.atualizar`, garantindo que mudança de estado “propague” para reorganização de filas.

---

# 12. FLUXO DE EXECUÇÃO

Cenário completo (comportamento esperado usando as APIs reais):

## 12.1 Criar infraestrutura
1) Criar `Aeroporto`
2) Criar recursos:
   - `Pista(codigo)`
   - `Plataforma(codigo)`
3) Adicionar ao aeroporto:
   - `aero.adicionarPista(pista)`
   - `aero.adicionarPlataforma(plataforma)`

## 12.2 Criar aeronave
4) Criar aeronave via Factory:
   - `aviao = FactoryAviao.criarAviao(tipo="Comercial"|"Privado"|"Transporte", **kwargs)`

## 12.3 Definir plano e registrar observer
5) Definir plano:
   - `aviao.definirPlano(plano)`
6) Registrar observer:
   - `aviao.adicionarObserver(aero.controleVoo)`

## 12.4 Decolagem
7) `aviao.solicitarDecolagem()`
8) `aviao.decolar()`
9) Estado final: `EmVoo`

## 12.5 Solicitar pouso e pousar
10) `aviao.solicitarPouso()`
11) `aviao.pousar()` (autoriza e muda para `Pousando`)
12) `aviao.pousar()` (conclui e muda para `EmSolo`)

## 12.6 (Opcional) Integrar infraestrutura
- Após `EmSolo`:
  - buscar plataforma livre e ocupar/liberar via runner:
    - `plataforma = aero.buscarPlataformaDisponivel()`
    - `plataforma.ocupar(aviao)`

Observação:
- Esse passo não é automático no código atual.

---

# 13. ANÁLISE DE COESÃO E ACOPLAMENTO

## 13.1 Pontos fortes
- **State Pattern**:
  - Alta coesão: regras por estado.
  - Baixo acoplamento na aeronave: `Aviao` não precisa saber regras específicas.
- **Observer Pattern**:
  - `Aviao` notifica; `ControleVoo` reage.
  - Facilita expansão do controle.
- **Singleton**:
  - garante consistência do centro controlador.
- **Composição (Aeroporto)**:
  - separa infraestrutura física do controle.

## 13.2 Pontos fracos / riscos arquiteturais
1) **Acoplamento ao estado interno**:
   - `ControleVoo.atualizar` acessa `origem._status`.
   - Embora funcione, é dependência estrutural do estado interno.

2) **Mensagens com placeholder incorreto**:
   - nos estados, mensagens usam `"{self.__identificador}"` como string literal, e `Aviao` usa `_identificador` (não `__identificador`).
   - Consequência: mensagens podem ser incorretas/inconsistentes.

3) **Integração falta entre filas e infraestrutura**:
   - Controle organiza filas; Aeroporto fornece recursos.
   - Não existe “ponte” automática entre “autorizar” e “ocupar pista/plataforma” em um componente central (ex.: CentroOperacional).
   - Consequência: lógica de alocação fica no runner futuro.

4) **Estado `Decolando` pode não ser alcançável por fluxo público**
   - O fluxo de decolagem descrito por transições públicas tende a ser:
     - `EmSolo -> AguardandoDecolagem -> EmVoo`
   - `Decolando` existe, mas pode depender de uso direto (lacuna de modelagem).

---

# 14. DÉBITOS TÉCNICOS

## 14.1 Bugs/Problemas encontrados no código
- `Aviao.removerObserver`:
  - usa `if (observador, Observer):` em vez de `isinstance(observador, Observer)`
  - isso não valida corretamente o tipo.
- `ControleVoo.removerAeronave`:
  - há inconsistências de fluxo/prints; a remoção pode ocorrer fora de uma condição esperada.
- Mensagens dos estados:
  - placeholder e interpolação inconsistentes (strings com `{}` que não são f-strings).

## 14.2 Convenções de encapsulamento vs realidade atual
O enunciado exigiu:
- preferir `_atributo` em vez de `__atributo` para evitar name mangling.

Na prática:
- `Aviao` usa `_identificador`, `_modelo` → alinhado com a convenção.
- Porém, os estados usam `self.__identificador` nas mensagens → incongruência.

## 14.3 Import circular (decisão registrada)
O projeto adota **imports locais dentro de métodos** dos estados para instanciar próximos estados.
Consequência:
- reduz risco de import circular ao carregar módulos que referenciam uns aos outros.

---

# 15. ROADMAP DE CONTINUIDADE

## Prioridade Alta
1) **Corrigir interpolação de mensagens nos estados**
   - trocar `"... {self.__identificador} ..."` por f-string ou forma correta via `_identificador`
   - consequência: logs e feedback operacional passam a refletir dados reais.

2) **Corrigir `Aviao.removerObserver`**
   - usar `isinstance(observador, Observer)`.

3) **Criar ponte operacional completa entre Controle e Infraestrutura**
   - implementar uma coordenação (idealmente no `CentroOperacional.py`, se seguir a arquitetura pretendida) que faça:
     - ao autorizar pouso/decolagem:
       - alocar pista/plataforma no `Aeroporto`
     - ao iniciar/terminar operações:
       - liberar recursos ao concluir.

4) **Garantir que `Decolando` seja alcançável (se for necessário no modelo)**
   - definir um evento/transição explícito para chegar a `Decolando`
   - ou remover o estado se não fizer parte do domínio operacional atual.

## Prioridade Média
5) **Adicionar asserts e testes reais**
   - converter roteiros em `pytest` com asserts verificando:
     - estado atual
     - reorganização de filas
     - disponibilidade/ocupação de recursos

6) **Diminuir acoplamento `ControleVoo` → `origem._status`**
   - criar um método público para consulta do estado (ex.: `origem.status_atual()` retornando o nome)
   - consequência: reduz dependência de atributo interno.

## Prioridade Baixa
7) **Limpeza de imports e padronização**
   - reduzir `from Models.States import *` quando não necessário
   - padronizar validações e mensagens de erro.

---

# 16. RESUMO EXECUTIVO

Este projeto é um **modelo orientado a objetos** do domínio aeroportuário com foco arquitetural.

- **Aeronaves (`Aviao`)** são objetos que mantêm um estado operacional (`_status`). Elas respondem a eventos delegando para o objeto de estado atual. A transição é realizada substituindo o objeto de estado retornado pelo estado atual (**State Pattern**).
- **Estados (`Models/States/*`)** implementam regras de transição para eventos (`solicitarPouso`, `solicitarDecolagem`, `decolar`, `pousar`, `declararEmergencia`). Para operações inválidas, retornam o próprio estado e uma mensagem.
- **Observer (`Observer` + `ControleVoo`)**: ao trocar de estado, a aeronave notifica observadores. O `ControleVoo` é um **Singleton** que organiza filas e aplica prioridade: quando a aeronave entra em `EmEmergencia`, ela é movida para prioridade máxima na fila de pouso.
- **Infraestrutura (`Aeroporto`, `Pista`, `Plataforma`)**: o aeroporto compõe pistas e plataformas, controla ocupação e disponibilidade e provê métodos para buscar recursos livres. O código atual não realiza a alocação automaticamente; isso deve ser integrado por uma camada coordenadora (ex.: runner futuro ou `CentroOperacional`).
- **Factory Method (`FactoryAviao`)**: cria aeronaves com validação de campos obrigatórios, evitando que o código externo instancie classes diretamente e reduzindo erros de inicialização.
- **Fluxos principais**:
  - Decolagem: `EmSolo → AguardandoDecolagem → EmVoo` (dependente de plano definido)
  - Pouso: `EmVoo → SolicitandoPouso → Pousando → EmSolo`
  - Emergência: qualquer estado que aceite transição para `EmEmergencia` reordena fila de pouso e direciona para pouso emergencial.

Com isso, outro desenvolvedor pode:
- entender a arquitetura e responsabilidades;
- localizar o comportamento no State Machine;
- entender como a priorização de emergências ocorre via Observer;
- e identificar lacunas para evolução (especialmente integração de filas com alocação de infraestrutura).
