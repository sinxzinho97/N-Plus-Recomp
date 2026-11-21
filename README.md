# N+ Recomp

Crie APKs Android dedicados para jogos de Nintendo Switch usando os arquivos do seu próprio console. Você pode preparar tudo diretamente no celular ou no PC — nos dois casos, o aplicativo gerado inclui o mesmo menu no jogo com ajustes de vídeo, controles na tela, gerenciador de mods, backup de saves e diagnóstico.

> [!NOTE]
> Este projeto está focado na evolução do **N+ Recomp** em conjunto com as melhorias da base Android (**nx2android**). Nenhum jogo, firmware ou chave acompanha o repositório.

## Baixar a versão 3.3.0

| Download | Para quem é | Primeiro passo |
| --- | --- | --- |
| [Criador para Android](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.3.0/N-Plus-Recomp-3.3.0-android-arm64.apk) | Android 13 ou superior, ARM64 | Instale o APK e abra **Criar**. |
| [Criador para Windows](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.3.0/N-Plus-Recomp-3.3.0-windows-x64.zip) | Windows x64 | Extraia a pasta inteira e abra **N+ Recomp.exe**. |
| [Driver de vídeo N+ Turnip V7](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.3.0/n-plus-turnip-V7.zip) | Opcional, para aparelhos Android com GPU Qualcomm Adreno compatível | Mantenha o ZIP fechado e importe-o pelo menu do jogo. [Instalação e retorno ao driver do sistema](docs/DRIVER.md) |

Os hashes SHA-256 e as notas acompanham os downloads. [Página da versão](https://github.com/sinxzinho97/N-Plus-Recomp/releases/tag/v3.3.0)

## Principais recursos

- **Criação no celular ou no PC:** gere o APK do jogo diretamente no Android ou prepare no Windows (útil para jogos maiores) mantendo exatamente os mesmos recursos no jogo.
- **Recursos gráficos e de fluidez:** escolha entre nitidez com **FSR 1** ou **SGSR 1**, **escala de resolução de 0,5x a 2,0x**, **FPS adaptativo (ADPF)** para controlar aquecimento e **geração de quadros (LSFG 1.5x / 2x / 3x)** com controle de ritmo da taxa base.
- **Drivers Vulkan personalizados:** use o driver do sistema ou importe pacotes `.zip` do Turnip diretamente pelo menu do jogo, com cache de pipelines separado por driver e **Modo seguro** caso algum ajuste impeça o boot.
- **Mods, saves e assinaturas:** suporte a mods por pacote RomFS, patches de código e plugins ExeFS, além de importação/exportação de saves e transferência de chaves de assinatura entre PC e celular.
- **Diagnóstico integrado:** exporte um pacote ZIP com logs de execução, patches/mods ativos e estado do aparelho sem precisar de cabo ou adb.

## Antes de baixar

- **Requisitos no celular:** Android 13 ou superior, arquitetura **ARM64**. O driver opcional **Turnip V7** é destinado apenas a aparelhos com GPU **Qualcomm Adreno** compatível; em outras GPUs (como Mali/Xclipse) ou em caso de erro visual, mantenha o **Driver do sistema**.
- **Arquivos necessários:** tenha em mãos o backup do jogo e o arquivo `prod.keys` do seu próprio console (com updates e DLCs opcionais).
- **Expectativa de compatibilidade:** o comportamento varia bastante entre jogos, versões de update, processadores e drivers. Confira o catálogo antes de preparar e trate títulos experimentais como testes em andamento.
- **Primeira execução no PC:** na versão Windows, abra **Configuração → Baixar ferramentas faltantes** para baixar Android NDK, .NET SDK e ADB automaticamente; se **Android Java** aparecer pendente, instale o **JDK 17** e a **plataforma 36 do Android SDK com Build-Tools** (o Python já acompanha o ZIP).

## Como funciona

1. **Consulte o catálogo.** A versão 3.3.0 inclui **69 perfis**. Procure o jogo e confira a versão de referência e o estado do perfil. “Jogável” registra um resultado para aquela referência; jogos e updates fora da lista também podem ser tentados em caráter experimental. [Ver os 69 jogos e versões](docs/CATALOGO.md)
2. **Prepare o jogo.** Na aba **Criar**, selecione o jogo base e seu `prod.keys`. Adicione o update e as DLCs que quiser usar. O criador lê os arquivos, prepara os módulos e os gráficos e gera o APK e os dados do jogo (a primeira preparação costuma levar mais tempo). Se preparar no PC, copie para o celular o APK **e** a pasta de dados preparados. [Guia de uso](docs/USO.md)
3. **Atualize uma instalação existente.** A aba **Atualizar** permite trocar o motor e o menu de um APK quando ele é compatível com os dados já preparados. Para instalar por cima mantendo seu save, use a assinatura original pela aba **Assinaturas**.

## Perguntas rápidas (FAQ)

<details>
<summary>Preciso de PC para usar o N+ Recomp?</summary>

Não. Todo o processo pode ser feito pelo aplicativo Android na aba **Criar**. O criador para Windows é uma opção para quem prefere preparar jogos pesados mais rápido no computador e depois copiar o APK + dados para o celular.
</details>

<details>
<summary>Quando devo usar o Turnip V7 e como volto se der problema?</summary>

Comece testando com o **Driver do sistema** se o jogo já abrir bem, ou importe o **N+ Turnip V7** apenas em aparelhos Snapdragon/Adreno compatíveis que tenham falhas gráficas ou perda de desempenho. Se a tela ficar preta ou instável após trocar o driver, abra **Gráficos → Driver de vídeo Vulkan** e volte para o **Driver do sistema** ou para o **n-plus-turnip-V6** ([detalhes em docs/DRIVER.md](docs/DRIVER.md)).
</details>

<details>
<summary>Preciso refazer o jogo do zero quando sai uma nova versão do app?</summary>

Nem sempre. Quando o novo lançamento mantém compatibilidade com os dados já preparados, basta usar a aba **Atualizar** com a mesma assinatura da aba **Assinaturas** para atualizar apenas o APK. Quando há mudança estrutural ou exigência de nova preparação, o criador e as notas da versão avisam antes.
</details>

<details>
<summary>Onde envio resultados ou peço ajuda quando um jogo fecha ou trava?</summary>

No menu de pausa do jogo, toque em **Preferências e diagnóstico → Salvar diagnóstico (ZIP)** e abra uma issue no GitHub anexando o ZIP junto do nome do jogo, versão do update, modelo do celular, GPU e driver usado.
</details>

## Testou em outro aparelho?

Relatos positivos também ajudam tanto quanto relatos de bug — eles mostram quais combinações de aparelho, update e driver funcionam bem. [Como coletar e revisar o diagnóstico](docs/DIAGNOSTICOS.md) · [Registrar um problema ou resultado](https://github.com/sinxzinho97/N-Plus-Recomp/issues/new/choose)

## Créditos

O **N+ Recomp** é desenvolvido e mantido por **sinxzinho97**. Este trabalho se apoia na base Android do projeto **nx2android**, criado por **shirai91 (Tung Pham)**. O driver Vulkan opcional deriva do **Mesa Turnip**, desenvolvido pela comunidade **Mesa/Freedreno**. [nx2android](https://github.com/shirai91/nx2android) · [Créditos, licenças e fontes dos componentes](CREDITOS.md)
