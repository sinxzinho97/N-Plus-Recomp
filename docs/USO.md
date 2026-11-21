# Como criar, instalar e atualizar um jogo

O N+ Recomp prepara um jogo de Nintendo Switch como aplicativo para Android. Você pode fazer a preparação no celular ou em um PC com Windows. Na primeira instalação, o jogo precisa do APK e dos dados preparados. Depois, você pode atualizar só o APK para receber um novo motor ou menu.

## Instale o criador

- **No Android** baixe o APK do criador na página de releases e abra o arquivo. Se o sistema pedir autorização, permita que o aplicativo usado para abrir o APK faça a instalação. O criador para celular requer Android 13 ou posterior em um aparelho ARM64.
- **No Windows x64** baixe o ZIP do criador, extraia a pasta inteira e abra **N+ Recomp.exe**. Mantenha os arquivos que acompanham o executável na pasta extraída. Abra **Configuração** e use **Baixar ferramentas faltantes** para obter o Android NDK r27c, o .NET SDK 10 e o Android platform-tools. O ADB do platform-tools é usado para instalar por USB. Se você já tiver as ferramentas, pode indicar onde estão e usar **Salvar e conferir**.

Se a conferência do Windows ainda indicar que faltam ferramentas Java para o menu do jogo, instale um JDK 17 e use o SDK Manager do Android Studio para adicionar uma **Android SDK Platform** e o **Android SDK Build-Tools**. O criador procura `javac`, `android.jar` e `d8`. Se instalou em pastas personalizadas, indique o JDK em `JAVA_HOME` e o Android SDK em `ANDROID_HOME`, reabra o criador e repita a conferência.

## Crie o jogo pela primeira vez

1. Abra a aba **Criar** e selecione o arquivo base do seu jogo. O criador aceita NSP e XCI e pode descompactar NSZ e XCZ durante a preparação. Se você tiver um update ou DLC para esse mesmo jogo, selecione cada arquivo na opção correspondente.
2. Indique o `prod.keys` do seu próprio console para ler os arquivos. Alguns perfis também precisam de dados do firmware. O driver de vídeo é opcional e pode ser escolhido posteriormente no menu do jogo.
3. Na conferência, verifique o título e a versão detectados. Na dúvida, comece pela versão de referência. Para um título ou update fora do catálogo, o criador pode oferecer uma tentativa experimental. Consulte a [lista de perfis e versões](CATALOGO.md).
4. Escolha o destino. No Windows, a aba **Criar** permite escolher a pasta de saída. No Android, **Instalação padrão** entrega os dados ao jogo no mesmo aparelho. **Salvar APK + dados em uma pasta** prepara uma cópia para transferir. Confira o espaço livre indicado, especialmente para arquivos comprimidos.
5. Toque ou clique em **Criar aplicativo**. Acompanhe a etapa atual até o criador informar que terminou. No Android, a notificação permite acompanhar a preparação enquanto usa outro aplicativo.

## Instale o jogo

- **No mesmo celular em que você criou o jogo**, confirme a instalação do APK e abra o jogo uma vez. Na primeira abertura ele recebe os dados preparados pelo criador. Se a entrega for interrompida, use a opção de retomar.
- **Do PC para o celular por USB**, ative a depuração USB no aparelho, conecte o cabo e autorize o computador na tela do Android. Você pode marcar **Instalação padrão** antes da criação ou usar **Jogos criados** e **Instalar jogo selecionado no celular (USB)** depois.
- **Para transferir manualmente**, leve o APK e a pasta de dados completa para o celular. No Windows, **Jogos criados → Abrir pasta do jogo** localiza a saída. Instale o APK e, se o jogo pedir os arquivos na primeira abertura, toque em **Escolher pasta dos arquivos** e indique a pasta de dados que você copiou.

## Atualize o motor ou o menu de um jogo instalado

1. Instale a nova versão do criador e abra **Atualizar**. No Android, selecione o jogo instalado ou escolha o arquivo APK. No PC, selecione um jogo já criado, um APK salvo ou um jogo do celular conectado por USB.
2. Gere o APK atualizado. Esse procedimento mantém a versão do jogo e reaproveita os dados já preparados. Para mudar a versão do próprio jogo, volte à aba **Criar** e selecione o update desejado.
3. Instale o novo APK sobre o existente. O Android exige a assinatura original para aceitar a atualização e manter saves e configurações. Se você criou o APK em outro aparelho, exporte a chave correspondente pela aba **Assinaturas** no criador de origem e importe o arquivo JSON na mesma aba do outro criador. A importação acrescenta a chave à coleção existente.

Guarde o backup da assinatura em local privado. Quem possui essa chave pode assinar atualizações para os seus APKs. O arquivo `prod.keys` tem outra função e só é necessário ao ler os arquivos do console.

## Experimente o driver opcional

O **N+ Turnip V7** é distribuído separadamente para GPUs Adreno compatíveis. Para comparar com o driver do aparelho, abra o menu do jogo, entre em **Driver de vídeo Vulkan**, toque em **Importar driver (.zip)** e selecione o ZIP do driver, ainda compactado. Selecione o driver importado e reinicie o jogo quando solicitado. Use o mesmo save e as mesmas opções de vídeo para comparar imagem e fluidez na mesma área. Você pode voltar ao driver do sistema pelo mesmo menu.

Se o jogo fechar, apresentar falha gráfica ou tiver travadas frequentes, abra **Preferências e diagnóstico → Salvar diagnóstico (ZIP)** e descreva o ocorrido nas Issues do projeto. Inclua a versão do criador, o jogo e a versão do jogo, o aparelho, a GPU e o driver escolhido. Confira o conteúdo do ZIP antes de anexá-lo. Arquivos do jogo, saves pessoais, `prod.keys` e backups de assinatura devem ficar com você. [Como coletar o diagnóstico](DIAGNOSTICOS.md)
