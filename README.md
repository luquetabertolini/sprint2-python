Sobre o Projeto
O ChargeGrid Intelligence e um ecossistema de software desenvolvido para o GoodWe Challenge 2026. O projeto foi concebido para viabilizar e acelerar a expansão das soluções de recarga da GoodWe do ambiente residencial para o cenário comercial de grande escala.

Esta Sprint 2 consolida-se na entrega de uma Prova de Conceito (PoC) funcional, desenvolvida inteiramente em Python. O foco central da solução e mitigar por completo os riscos de sobrecarga na rede elétrica de estabelecimentos comerciais causados pelo carregamento simultâneo de múltiplos veículos elétricos (EVs), garantindo ao mesmo tempo a interoperabilidade de dados e a automação financeira.

Arquitetura do Software e os 4 Pilares
O sistema foi construído utilizando o paradigma de Programação Orientada a Objetos (POO) e traduz de forma prática as resoluções propostas na fase de pesquisa:

Controle de Demanda (Algoritmo de Carga Dinâmica Equitativa):
Mecanismo de automação que monitoriza a soma da potência solicitada pelas vagas em tempo real. Se o consumo total ameaçar ultrapassar o limite físico configurado para o estabelecimento comercial (definido na simulação em 50.0 kW), o algoritmo intervém de forma autónoma. Ele recalcula o cenário e distribui a potência máxima permitida de forma rigorosamente igualitária entre todos os veículos ativos, impedindo que o disjuntor do prédio desarme.

Protocolos Abertos (Simulação OCPP JSON):
Para assegurar que as estações de recarga comerciais possam comunicar de forma universal com qualquer central de monitoramento de frotas do mercado, o software simula o padrão internacional OCPP (Open Charge Point Protocol). As alterações de status e registos do sistema são estruturadas e empacotadas nativamente em strings no formato JSON (simulando mensagens cruciais como BootNotification e StatusNotification).

Tarifação e Pagamento (Módulo Financeiro):
Módulo matemático embarcado focado no cálculo de consumo real em quilowatt-hora (kWh) atrelado ao tempo de permanência do veículo na vaga. O sistema simula a interface lógica de um aplicativo móvel corporativo, realizando a conversão exata da energia em valores monetários e gerando uma simulação de código Pix para a conclusão do pagamento digital.

Inteligência Artificial (Análise Preditiva de Cenário):
Mecanismo analítico simulado baseado em padrões cronológicos comerciais históricos. O algoritmo avalia proativamente o horário do sistema e emite alertas preditivos caso a recarga esteja prestes a ocorrer em janelas críticas de picos de consumo (como horários de almoço ou fim de expediente), sugerindo ações preventivas ao ecossistema.

Fluxo do Terminal na Execução da Simulação
Ao executar o comando, o terminal irá simular um cenário comercial real passo a passo de forma limpa:

Inicialização da IA: O sistema lê o horário comercial e emite um relatório preditivo sobre a estabilidade da rede.

Conexão Segura: Dois veículos elétricos (BYD Seal e GWM Ora 3) conectam-se às Vagas 1 e 2. Como a demanda combinada respeita o teto de 50 kW, o sistema entrega a carga total solicitada e dispara os pacotes JSON no padrão OCPP correspondentes.

Interceptação de Sobrecarga: Um terceiro veículo (Volvo XC40) conecta-se à Vaga 3. A demanda total iria para 66 kW. O algoritmo de Controle de Demanda intercepta o evento imediatamente, exibe um alerta de risco de sobrecarga e reajusta as três vagas de forma equitativa para 16.6 kW cada, protegendo o prédio.

Checkout Financeiro: O aplicativo simula o encerramento da recarga do primeiro veículo, realiza o cálculo de kWh x Preço e simula a emissão com sucesso do gateway de pagamento digital via Pix.

Equipe 1 (Turma 1CCPW)
Diego de Oliveira Brandão

Raphaello Caffettani

Cristhian Henrique Clementino

Fabio Pena Vieira

Lucca Bertolini
