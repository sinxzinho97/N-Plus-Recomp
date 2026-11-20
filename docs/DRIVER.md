# N+ Turnip V6

O N+ Turnip V6 é um driver Vulkan opcional para jogos Android criados pelo N+ Recomp. O jogo usa o driver do celular na primeira instalação. Você pode experimentar o V6 em um único jogo, comparar o resultado e voltar à configuração anterior pelo menu. A troca também funciona em jogos preparados pelo criador do Windows.

## Quem pode usar

O ZIP contém uma biblioteca Android ARM64 para GPUs Qualcomm Adreno que usam o driver de kernel KGSL. O pacote declara Android 10 ou superior (API 29). Para usar o **criador** no celular, o requisito é Android 13 ou superior. Em aparelhos com GPU Mali, Immortalis, Xclipse ou PowerVR, use o driver do sistema.

O pacote tem como alvo as famílias Adreno 6xx, 7xx e 8xx. O modelo da GPU, o sistema do fabricante, a versão do jogo e a região do cenário influenciam o resultado. O objetivo do V6 é reduzir falhas visuais de profundidade, especialmente piscadas em jogos como *Tears of the Kingdom*. Para avaliar FPS e estabilidade no seu aparelho, compare os dois drivers no mesmo trecho.

## Instalar ou voltar ao driver do celular

1. Baixe o driver e guarde o ZIP inteiro no celular. [Baixar n-plus-turnip-V6.zip](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.0.11/n-plus-turnip-V6.zip)
2. Salve seu progresso. No menu do jogo, abra **Gráficos → Driver de vídeo Vulkan → Importar driver (.zip)**.
3. Escolha o ZIP, selecione **n-plus-turnip-V6** na lista e toque em **Reiniciar jogo**. A escolha vale para esse jogo. Os outros jogos continuam com o driver que você escolheu para cada um.
4. Para desfazer, selecione **Driver do sistema do celular** no mesmo menu e reinicie. Se a tela impedir o acesso ao menu, feche o jogo, mantenha o ícone dele pressionado e escolha **System driver**, se seu launcher mostrar esse atalho.

## O que mudou

A biblioteca usa o Turnip do Mesa 26.3.0 e se identifica como `26.3.0-recomp.6`. A principal mudança do V5 para o V6 ocorre em GPUs Adreno 8xx. Ao terminar um passe de renderização na memória interna da GPU (GMEM), o driver reinicializa o controle do teste de profundidade (LRZ). Isso evita que o passe seguinte herde esse estado. O resto do patch do V5 foi mantido, incluindo o tratamento dos metadados de buffers de imagem do Android (IMapper5 e compressão UBWC), a recuperação de determinados buffers de tela na Adreno 830 e ajustes por modelo de GPU.

## Informar um problema

Se notar piscadas, tela preta ou travadas, registre o trecho em que acontece e exporte o diagnóstico daquela sessão **antes de trocar o driver ou reiniciar o jogo**. Se puder comparar com o driver do celular, repita o mesmo trecho com o mesmo save, resolução e limite de FPS e exporte um segundo diagnóstico. Na issue, identifique cada ZIP pelo driver, informe o modelo do aparelho, SoC/GPU, versão do Android, versão do N+ Recomp e versão do jogo. Um vídeo curto ajuda a mostrar falhas que o contador de FPS não revela. Revise os anexos antes de publicá-los e deixe de fora dados pessoais, chaves, jogos e saves.

## Origem, créditos e compilação

- A equipe Mesa/Freedreno desenvolve o Turnip. A soma publicada para a fonte 26.3.0 corresponde à usada na receita. [Documentação do Freedreno](https://docs.mesa3d.org/drivers/freedreno.html) · [Versão 26.3.0 e SHA-256 oficial](https://docs.mesa3d.org/relnotes/26.3.0.html) · [Licenças do Mesa](https://docs.mesa3d.org/license.html)
- O backend IMapper5 adapta o trabalho de **Leb-Sun**. A família de ajustes comunitários de resolve e máscara de cor LRZ para Adreno 8xx também tem contribuições de **Vauzi-17**, creditadas pelo Droid-Deck. [Créditos do Droid-Deck](https://github.com/Droid-Deck/Drivers#patches)
- **sinxzinho97 / N+ Recomp** mantém a variante e a integração com o menu, com assistência do Gemini na preparação do V6. O pacote foi compilado com o Android NDK r28c e traz os avisos do Mesa e do NDK em `LICENSE.Mesa.txt` e `NOTICE.NDK.txt`. A origem e as somas estão em `NOTICE.txt`. [Perfil do mantenedor](https://github.com/sinxzinho97) · [Android NDK r28c](https://github.com/android/ndk/wiki/Unsupported-Downloads#r28c)

Para compilar em Linux x86-64, instale Python 3 com venv e pip, ferramentas de compilação C/C++, Ninja, pkg-config, Flex, Bison, glslang-tools, GNU patch, curl, tar, xz e unzip. Execute o comando na raiz dos fontes desta release.

```sh
bash driver/compilar-turnip.sh package
```

A receita confere os arquivos de origem, aplica o patch cumulativo e gera `driver/n-plus-turnip-V6.zip` com os avisos e a biblioteca. A soma do ZIP identifica o download da release. Horários dos arquivos e diferenças na ferramenta de compilação podem alterar o hash de uma nova compilação. [Patch aplicado ao Mesa](../driver/patches/mesa-26.3.0-nplus-v6.patch) · [Receita de compilação](../driver/compilar-turnip.sh)

| Arquivo desta release | SHA-256 |
| --- | --- |
| `n-plus-turnip-V6.zip` | `2ece35d5ebb3300fc4144d8dcdfdff86cedd60cefb1b0d9b5a47e2b64f32c07e` |
| `libvulkan_freedreno.so` dentro do ZIP | `4e24e1b0df726564d7114b126cc423f0134001d49e169af458d24ff02c2fd266` |
| `mesa-26.3.0-nplus-v6.patch` | `ec43c6d103e1f8891650e187822875ea50ecd189f0e647dc3c40e8ab7e12b193` |
