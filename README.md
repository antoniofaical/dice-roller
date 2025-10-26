# Dice Roller CLI

Um pequeno projeto Python que simula rolagens de dados de RPG diretamente pelo terminal.  
Permite múltiplas expressões no formato `XdY`, como `2d6 + 1d8`, com totalização automática e interface simples.

---

## Demonstração

```bash
$ python dice_roller.py
----------------------------------------------------------------------------------------------------
Welcome to the Dice Roller! This program helps you quickly roll RPG dice!
Valid dice:
    [d4, d6, d8, d10, d12, d20]
Usage examples:
    Roll 2 four-sided dice →  '2d4'
    Roll 1 six-sided and 1 eight-sided die →  '1d6 + 1d8'
----------------------------------------------------------------------------------------------------

Enter the dice to roll (Ctrl+C to exit): 2d6 + 1d8

2d6: [3, 5] (sum = 8)
1d8: [7] (sum = 7)
----------------------------------------------------------------------------------------------------
```

---

## Funcionalidades

- Aceita múltiplas expressões separadas por `+`
- Valida formatos incorretos e tipos de dados inválidos
- Suporta abreviação (`d6` = `1d6`)
- Interface de terminal com instruções e separadores visuais
- Saída formatada com resultados individuais e soma total
- Encerramento elegante via `Ctrl+C`

---

## Aprendizados e tecnologias

Este projeto foi criado como parte da iniciativa **“1 Projeto por Semana”**, com foco em aprendizado incremental.  
Conceitos aplicados:
- Manipulação de strings e parsing de expressões
- Estrutura de funções e modularização de código
- Uso de bibliotecas padrão (`random`)
- Laços, condicionais e tratamento de erros (`try/except`)
- Boas práticas de UX em aplicações CLI

---

## Execução

### Pré-requisitos
- Python 3.8 ou superior

### Rodando localmente
```bash
git clone https://github.com/antoniofaical/dice-roller.git
cd dice-roller
python dice_roller.py
```

---

## Histórico de desenvolvimento

| Etapa | Commit | Descrição |
|:--:|:--|:--|
| 1 | `initial draft: basic dice roller logic` | Primeira versão funcional simples |
| 2 | `add support for multiple dice expressions and validation` | Parsing de múltiplos dados e checagem de entrada |
| 3 | `improve user interface and add friendly messages` | Interface amigável e loop contínuo |
| 4 | `refactor parsing and add support for single ‘d6’ format` | Parsing limpo e abreviação “d6” |
| 5 | `final polish: docstrings, constants, and graceful exit handling` | Código final limpo e documentado |

---

## Próximos passos (futuro)

- Adicionar modificadores (`2d6 + 3`)
- Implementar modo histórico de rolagens
- Suporte a execução via argumentos de linha de comando (`python dice_roller.py "2d6+1d8"`)
- Testes unitários com `pytest`
- Publicar como pacote `pip` minimalista

---

## Autor

**Antonio Elias Faiçal Jr.**  
Engenheiro e desenvolvedor com foco em Python, C++, web e eletrônica aplicada.  
🔗 [LinkedIn](https://www.linkedin.com/in/antoniofaical)  
💻 [GitHub](https://github.com/antoniofaical)

---

## Licença
Este projeto é de uso livre para fins educacionais.
