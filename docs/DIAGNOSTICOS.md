# Como relatar erros e resultados de compatibilidade

Um relato é mais fácil de comparar quando identifica a versão do jogo e o ponto exato em que o problema aparece. Por exemplo, “o jogo abre o menu, carrega meu save e fecha alguns segundos depois que começo a andar” permite investigar uma etapa diferente de “o criador parou ao preparar os gráficos”.

## Se o problema ocorre dentro do jogo

1. Reproduza o problema e anote o local do jogo, a ação que o desencadeia e quanto tempo levou. Para quedas de FPS, diga se ocorreram só na primeira passagem pela área ou se voltaram ao repetir o trajeto.
2. No menu de pausa, abra **Preferências e diagnóstico → Salvar diagnóstico (ZIP)** e escolha onde salvar. Se o jogo fechou, exporte na primeira oportunidade. Quando aparecer a tela **Falha ao iniciar com mods**, você também pode usar **Exportar diagnóstico** nela.
3. Se for comparar drivers ou configurações, salve um ZIP para cada tentativa. Anote qual driver foi usado e reinicie o jogo após a troca. O diagnóstico reúne trechos limitados do registro atual e do anterior, quando disponíveis. Várias reaberturas podem substituir o registro da tentativa que você quer mostrar.

## Se o problema ocorre durante a criação

No criador **Windows**, abra **Mostrar diagnóstico e detalhes das etapas**. No criador **Android**, abra **Mostrar detalhes técnicos** na tela de andamento. Copie a mensagem de erro e a etapa em que parou. Se o próprio criador Android falhar ao abrir, use **Copiar erro**, quando disponível. Uma captura com o erro legível também serve quando o jogo ainda não chegou a ser criado.

## O que enviar

- Nome e versão do jogo, update utilizado e versão do N+ Recomp que gerou ou atualizou o APK.
- Modelo do celular, versão do Android, processador e GPU, se souber. Para falha no criador Windows, acrescente a versão do Windows.
- Driver do sistema ou nome e versão do ZIP. Informe também os mods ativos e as opções de vídeo alteradas, como modo portátil/TV, limite de FPS e shaders assíncronos.
- Passos para repetir, resultado esperado e observado. Se funcionou bem, diga quais áreas ou modos você jogou e por quanto tempo.

**O envio é manual e a issue fica pública.** Abra o ZIP e revise os textos antes de anexar. Remova nomes, caminhos de pastas e outras informações pessoais que apareçam no registro. Se preferir, cole apenas o trecho relevante já revisado. Guarde em particular as chaves `prod.keys`, backups de assinatura, ROMs, firmware, saves e APKs de jogos. Para investigar o mesmo erro em aparelhos diferentes, o modelo do celular e a versão do sistema bastam como identificação do aparelho.

[Abrir o formulário de relato](https://github.com/sinxzinho97/N-Plus-Recomp/issues/new/choose)
