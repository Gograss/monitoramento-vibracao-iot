# monitoramento-vibracao-iot
Sistema IoT de Manutenção Preditiva em Motores Elétricos Low Cost utilizando ESP32 e MicroPython.
# Sistema IoT de Manutenção Preditiva em Motores Elétricos 🚀

Trabalho de Extensão acadêmico para a disciplina de Aplicações de Cloud, IoT e Indústria 4.0 em Python.

## 📋 Sobre o Projeto
Este projeto consiste em um sistema de telemetria IoT de baixo custo para monitorar a saúde de Motores de Indução Trifásicos em ambientes industriais. Utilizando conceitos de **Edge Computing**, o sistema lê sensores críticos e toma decisões locais de segurança antes do envio dos dados.

## 🛠️ Componentes Utilizados
* **ESP32 DevKit V1** (Microcontrolador com Wi-Fi)
* **Sensor DHT22** (Monitoramento de Temperatura)
* **Potenciômetro** (Simulador de Sensor de Vibração/Acelerômetro)
* **LED Difuso Vermelho & Resistor 220Ω** (Atuador para Alerta Local)

## 💻 Tecnologias
* **Linguagem:** Python (MicroPython)
* **Ambiente de Simulação:** Wokwi

## 🔧 Como Executar
1. Copie o conteúdo do arquivo `diagram.json` para o seu ambiente Wokwi ou abra o circuito físico.
2. Cole o código do arquivo `main.py` na aba correspondente do MicroPython.
3. Inicie a simulação. Altere os valores do potenciômetro (acima de 3000) ou do DHT22 (acima de 50°C) para ver o LED de alerta disparar no terminal.
