# Challenge IBM - Sprint 3 - Grupo 6 :rooster:

- Fabrício Saavedra - 97631
- Guilherme Akio - 98582
- Guilherme Morais - 551981
- Matheus Motta - 550352
- Vinicius Buzato - 99125
___
## Problema e projeto de solução

Os alagamentos urbanos representam um problema grave para muitas cidades, trazendo prejuízos financeiros, problemas de saúde pública e impactos ambientais. Além disso, esses eventos podem levar ao deslocamento de pessoas e aumentar a vulnerabilidade de populações mais carentes. Com o agravamento das mudanças climáticas, a tendência é que as enchentes urbanas se tornem cada vez mais frequentes e intensas em algumas regiões.

Nesse contexto, apresentamos a solução de um serviço web que permite ao usuário consultar informações sobre a previsão de alagamentos em sua cidade. O usuário pode verificar, por meio do índice pluviométrico, se há risco de alagamento em determinada região e, caso necessário, receber alertas de segurança pelo próprio site.

A partir do nosso projeto, o Galo Weather, o usuário pode planejar suas atividades com antecedência, evitando áreas de risco e ajustando sua rotina de acordo com a previsão do tempo. Além disso, a prefeitura da cidade também pode ser alertada sobre a possibilidade de alagamento, possibilitando a atuação rápida em áreas de risco e reduzindo os prejuízos para a população.

Portanto, a solução apresentada não só atua na prevenção de alagamentos urbanos, mas também contribui para a segurança e qualidade de vida da população. Ao investir em tecnologias inovadoras e soluções inteligentes para o enfrentamento dos desafios urbanos, é possível construir cidades mais sustentáveis e preparadas para os desafios do futuro.
___
## Funcionalidades implementadas

Consulta de bairros com maior risco de alagamento: o usuário poderá consultar uma lista de bairros pré-determinados para saber se há chance de alagamento, recebendo uma mensagem personalizada com a estimativa (ou não) de alagamento naquela região para o período.

O programa fornece essa resposta com base em dois valores manualmente inseridos: Índice Pluviométrico (no programa definido como "chuva_hoje") e a leitura feita por um sensor físico que monitora o estado de funcionamento de um bueiro de rua (no programa definido como "bueiro_entupido").

Alerta de algum bairro de risco: o usuário poderá também informar um local que está alagado no momento, para que no futuro a equipe responsável (prefeitura) possa direcionar seus esforços para minimizar as chances de novos alagamentos naquela região.

Os dados de consulta e notificação são armazenados e exibidos ao usuário na execução de cada atividade e também no fim do programa mostrando o hitórico de navegação.

