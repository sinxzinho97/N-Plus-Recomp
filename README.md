# N+ Recomp

Prepare um aplicativo Android dedicado a cada jogo de Nintendo Switch usando os arquivos do seu próprio console. Você pode preparar o jogo no celular ou no PC. Nos dois casos, o APK gerado roda no Android e oferece o mesmo menu de vídeo, controles, mods, saves e diagnóstico.

## Baixar a versão 3.0.11

| Download | Para quem é | Primeiro passo |
| --- | --- | --- |
| [Criador para Android](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.0.11/N-Plus-Recomp-3.0.11-android-arm64.apk) | Android 13 ou superior, ARM64 | Instale o APK e abra **Criar**. |
| [Criador para Windows](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.0.11/N-Plus-Recomp-3.0.11-windows-x64.zip) | Windows x64 | Extraia a pasta inteira e abra **N+ Recomp.exe**. |
| [Driver de vídeo N+ Turnip V6](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.0.11/n-plus-turnip-V6.zip) | Opcional, para aparelhos Android com GPU Qualcomm Adreno compatível | Mantenha o ZIP fechado e importe-o pelo menu do jogo. [Instalação e retorno ao driver do sistema](docs/DRIVER.md) |

Os hashes SHA-256 e as notas acompanham os downloads. [Página da versão](https://github.com/sinxzinho97/N-Plus-Recomp/releases/tag/v3.0.11)

## Como funciona

1. **Consulte o catálogo.** A versão 3.0.11 inclui 62 perfis. Procure o jogo e confira a versão de referência e o estado do perfil. “Jogável” registra um resultado para aquela referência. O desempenho pode mudar com a atualização do jogo, o aparelho, a GPU e o driver. Jogos e updates fora da lista também podem ser tentados em caráter experimental. [Ver os 62 jogos e versões](docs/CATALOGO.md)
2. **Prepare o jogo.** Na aba **Criar**, selecione o jogo base e seu `prod.keys`. Adicione o update e as DLCs que quiser usar. O criador lê os arquivos, prepara os módulos e os gráficos e gera o APK e os dados do jogo. A primeira preparação costuma levar mais tempo. Se for transferir do PC para o celular, leve o APK **e** os dados preparados. [Guia de uso](docs/USO.md)
3. **Atualize uma instalação existente.** A aba **Atualizar** permite trocar o motor e o menu de um APK quando ele é compatível com os dados já preparados. Para instalar a atualização por cima, use a assinatura original. A aba **Assinaturas** permite fazer backup privado e transferir chaves entre PC e celular.

**Primeira execução no PC.** Em **Configuração → Baixar ferramentas faltantes**, o criador pode obter o Android NDK, o .NET SDK e o ADB. Se a linha **Android Java** estiver pendente, instale também o JDK 17 e a plataforma 36 do Android SDK com Build-Tools. O Python acompanha o ZIP.

## Testou em outro aparelho?

Se o jogo fecha ao carregar um save, mostra falhas gráficas ou perde fluidez, conte em que momento acontece. No menu de pausa, abra **Preferências e diagnóstico → Salvar diagnóstico (ZIP)**. Informe o jogo e sua versão, modelo do aparelho, Android, processador/GPU e driver. Um relato positivo também ajuda a identificar quais combinações funcionam. [Como coletar e revisar o diagnóstico](docs/DIAGNOSTICOS.md) · [Registrar um problema ou resultado](https://github.com/sinxzinho97/N-Plus-Recomp/issues/new/choose)

## Créditos

O N+ Recomp é desenvolvido e mantido por **sinxzinho97**. Este trabalho só foi possível graças a **shirai91 (Tung Pham)**, autor da integração Android no **nx2android**, e a **seedds**, autor do motor e das ferramentas originais do **nxnative**. O driver opcional deriva do **Mesa Turnip**, desenvolvido pela comunidade Mesa/Freedreno. [nx2android](https://github.com/shirai91/nx2android) · [nxnative](https://github.com/seedds/nxnative) · [Créditos, licenças e fontes dos componentes](CREDITOS.md)
