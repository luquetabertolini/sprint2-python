import json
import random
import time
from datetime import datetime


class ChargeGridIntelligence:

    def __init__(self, potencia_maxima_rede_kw=50.0):
        # Configuracoes do Pilar 1: Controle de Demanda
        self.potencia_maxima_rede = potencia_maxima_rede_kw
        self.veiculos_conectados = {}  # {id_vaga: {modelo, SOC_atual, taxa_kw}}

        # Configuracoes do Pilar 3: Tarifacao e Pagamento
        self.preco_por_kwh = 1.50  # Valor ficticio em R$

    # --- PILAR 1: CONTROLE DE DEMANDA ---
    def conectar_veiculo(self, id_vaga, modelo, soc_atual, potencia_desejada):
        """Simula a conexao de um EV e recalcula a distribuicao de carga dinamicamente."""
        self.veiculos_conectados[id_vaga] = {
            "modelo": modelo,
            "soc": soc_atual,
            "potencia_solicitada": potencia_desejada,
            "potencia_atual": potencia_desejada,
        }
        print(f"\n[CONEXAO] Veiculo {modelo} conectado na Vaga {id_vaga}.")
        self._ajustar_demanda_dinamica()

    def desconectar_veiculo(self, id_vaga):
        """Remove o veiculo e libera potencia para os demais."""
        if id_vaga in self.veiculos_conectados:
            veiculo = self.veiculos_conectados.pop(id_vaga)
            print(
                f"\n[DESCONEXAO] Veiculo {veiculo['modelo']} desconectado da Vaga {id_vaga}."
            )
            self._ajustar_demanda_dinamica()

    def _ajustar_demanda_dinamica(self):
        """Logica Algoritmica: Garante que a soma das potencias nao ultrapasse o limite da rede."""
        potencia_total_solicitada = sum(
            v["potencia_solicitada"] for v in self.veiculos_conectados.values()
        )

        print(
            f"[DEMANDA] Potencia Total Solicitada: {potencia_total_solicitada:.1f} kW / Limite: {self.potencia_maxima_rede:.1f} kW"
        )

        if potencia_total_solicitada > self.potencia_maxima_rede:
            print(
                "ALERTA: Alerta de Sobrecarga detectado! Aplicando Gerenciamento Inteligente..."
            )
            # Divisao igualitaria ou proporcional da potencia disponivel
            numero_veiculos = len(self.veiculos_conectados)
            potencia_balanceada = self.potencia_maxima_rede / numero_veiculos

            for id_vaga in self.veiculos_conectados:
                self.veiculos_conectados[id_vaga][
                    "potencia_atual"
                ] = potencia_balanceada
        else:
            # Rede suporta a carga total solicitada
            for id_vaga in self.veiculos_conectados:
                self.veiculos_conectados[id_vaga]["potencia_atual"] = (
                    self.veiculos_conectados[id_vaga]["potencia_solicitada"]
                )

        self._exibir_status_vagas()

    def _exibir_status_vagas(self):
        print("--- Status Atual das Vagas Comerciais ---")
        for vaga, dados in self.veiculos_conectados.items():
            print(
                f"  Vaga {vaga} | {dados['modelo']} | Bateria: {dados['soc']}% | Potencia Entregue: {dados['potencia_atual']:.1f} kW"
            )
        print("-----------------------------------------")

    # --- PILAR 2: PROTOCOLOS ABERTOS (SIMULACAO OCPP JSON) ---
    def simular_mensagem_ocpp(self, id_vaga, tipo_mensagem):
        """Demonstra interoperabilidade gerando pacotes textuais identicos ao padrao OCPP."""
        timestamp = datetime.now().isoformat()
        if tipo_mensagem == "BootNotification":
            payload = {
                "chargePointVendor": "GoodWe",
                "chargePointModel": "ChargeGrid-Comm-V1",
                "firmwareVersion": "2026.05.1",
            }
        elif tipo_mensagem == "StatusNotification":
            status = (
                "Occupied" if id_vaga in self.veiculos_conectados else "Available"
            )
            payload = {"connectorId": id_vaga, "status": status, "errorCode": "NoError"}

        ocpp_packet = [2, f"MSG_{random.randint(1000,9999)}", tipo_mensagem, payload]
        print(f"\n[OCPP OUT]: {json.dumps(ocpp_packet, indent=2)}")

    # --- PILAR 4: INTELIGENCIA ARTIFICIAL (PREVISAO DE PICO) ---
    def prever_demanda_ia(self, hora_atual):
        """Simula comportamento preditivo de IA baseado em padroes comerciais historicos."""
        print(f"\n[IA ANALYTICS] Executando analise preditiva para as {hora_atual:02d}:00h...")
        # Logica simulada: Horarios comerciais de pico (ex: 12h as 14h e 18h as 20h)
        if 12 <= hora_atual <= 14 or 18 <= hora_atual <= 21:
            probabilidade_pico = random.randint(85, 98)
            print(
                f"   -> Alerta de Inteligencia: Alta probabilidade de pico detectada ({probabilidade_pico}%)."
            )
            print(
                "   -> Acao Recomendada: Restringir recargas nao urgentes para preservar a rede."
            )
        else:
            print(
                "   -> Status da Rede: Estavel. Sem previsoes de picos criticos para as proximas horas."
            )

    # --- PILAR 3: TARIFACAO E PAGAMENTO ---
    def simular_checkout_pagamento(self, id_vaga, tempo_recarga_horas):
        """Calcula o consumo energetico final e simula a interface financeira do app."""
        if id_vaga not in self.veiculos_conectados:
            print("Vaga vazia. Nenhum checkout pendente.")
            return

        veiculo = self.veiculos_conectados[id_vaga]
        kwh_consumido = veiculo["potencia_atual"] * tempo_recarga_horas
        valor_total = kwh_consumido * self.preco_por_kwh

        print(f"\n[APP MOBILE - FATURAMENTO] Checkout Vaga {id_vaga}")
        print(f"   Veiculo: {veiculo['modelo']}")
        print(f"   Energia Consumida: {kwh_consumido:.2f} kWh")
        print(f"   Tarifa Comercial: R$ {self.preco_por_kwh:.2f} / kWh")
        print(f"   VALOR TOTAL A PAGAR: R$ {valor_total:.2f}")
        print("   [APP] Gerando codigo Pix para pagamento digital... Sucesso!")

        self.desconectar_veiculo(id_vaga)


# === EXECUCAO DA PROVA DE CONCEITO (SIMULACAO) ===
if __name__ == "__main__":
    # Inicializa o eletroposto comercial com limite de 50 kW
    sistema = ChargeGridIntelligence(potencia_maxima_rede_kw=50.0)

    # 1. Simulacao do pilar de IA (Analise de cenario)
    sistema.prever_demanda_ia(hora_atual=18)  # Horario de pico simulado
    time.sleep(1)

    # 2. Conectando Veiculos (Abaixo do limite da rede)
    sistema.conectar_veiculo(
        id_vaga=1, modelo="BYD Seal", soc_atual=45, potencia_desejada=22.0
    )
    # Simulando o envio de protocolo aberto OCPP padrao
    sistema.simular_mensagem_ocpp(id_vaga=1, tipo_mensagem="StatusNotification")
    time.sleep(1)

    sistema.conectar_veiculo(
        id_vaga=2, modelo="GWM Ora 3", soc_atual=20, potencia_desejada=22.0
    )
    time.sleep(1)

    # 3. Engenharia de Controle de Demanda entrando em acao (Ultrapassando o limite)
    sistema.conectar_veiculo(
        id_vaga=3, modelo="Volvo XC40", soc_atual=60, potencia_desejada=22.0
    )
    time.sleep(1)

    # 4. Simulacao de Tarifacao e Finalizacao de uso do Aplicativo
    sistema.simular_checkout_pagamento(id_vaga=1, tempo_recarga_horas=1.5)