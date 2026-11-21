# N+ Turnip V7

O N+ Turnip V7 é um driver Vulkan opcional para jogos Android criados pelo N+ Recomp. O jogo usa o driver do celular na primeira instalação. Você pode experimentar o V7 em um único jogo, comparar o resultado e voltar à configuração anterior (inclusive para o V6 ou para o driver do sistema) pelo menu. A troca também funciona em jogos preparados pelo criador do Windows.

## Quem pode usar

O ZIP contém uma biblioteca Android ARM64 para GPUs Qualcomm Adreno que usam o driver de kernel KGSL. O pacote declara Android 10 ou superior (API 29). Para usar o **criador** no celular, o requisito é Android 13 ou superior. Em aparelhos com GPU Mali, Immortalis, Xclipse ou PowerVR, use o driver do sistema.

O pacote tem como alvo as famílias Adreno 6xx, 7xx e 8xx. O modelo da GPU, o sistema do fabricante, a versão do jogo e a região do cenário influenciam o resultado. O V7 mantém todas as correções gráficas do V6 e adiciona compilação com **ThinLTO** para aliviar o custo de CPU no envio de comandos gráficos. Para avaliar FPS e estabilidade no seu aparelho, compare os drivers no mesmo trecho.

## Instalar ou voltar ao driver anterior

1. Baixe o driver e guarde o ZIP inteiro no celular. [Baixar n-plus-turnip-V7.zip](https://github.com/sinxzinho97/N-Plus-Recomp/releases/download/v3.2.8/n-plus-turnip-V7.zip)
2. Salve seu progresso. No menu do jogo, abra **Gráficos → Driver de vídeo Vulkan → Importar driver (.zip)**.
3. Escolha o ZIP, selecione **n-plus-turnip-V7** na lista e toque em **Reiniciar jogo**. A escolha vale para esse jogo. Os outros jogos continuam com o driver que você escolheu para cada um.
4. Como o cache de pipelines é separado por UUID do driver, a primeira abertura com o V7 reconstrói o cache; a partir da segunda abertura, o carregamento volta ao normal.
5. Para desfazer, selecione **n-plus-turnip-V6** (se ainda estiver importado) ou **Driver do sistema do celular** no mesmo menu e reinicie. Se a tela impedir o acesso ao menu, feche o jogo, mantenha o ícone dele pressionado e escolha **System driver**, se seu launcher mostrar esse atalho.

## O que mudou do V6 para o V7

A biblioteca usa a mesma base Turnip do Mesa 26.3.0 e se identifica como `26.3.0-recomp.7`:

- **Mantém todas as correções do V6:** reset leve do LRZ ao final de passes GMEM na Adreno 8xx (para reduzir piscadas de profundidade em jogos como *Tears of the Kingdom*), `GRAS_LRZ_COLOR_COMP_MASK`, prefetch de textura do V5, backend `IMapper5`/UBWC universal, recuperação do layout de display (S25 Ultra / Adreno 830) e alinhamento de 16 KiB.
- **Compilação com ThinLTO (`-Db_lto=true -Db_lto_mode=thin`):** otimização de link para reduzir o custo de CPU no caminho quente de submit do Turnip (descritores, draws e render passes) em jogos pesados. Como usa a opção experimental `allow-broken-lto` do Mesa, se qualquer jogo apresentar travamento, tela preta ou glitch novo com o V7, basta voltar ao V6 no mesmo menu e relatar o trecho.

## Informar um problema

Se notar piscadas, tela preta ou travadas, registre o trecho em que acontece e exporte o diagnóstico daquela sessão **antes de trocar o driver ou reiniciar o jogo**. Se puder comparar com o V6 ou com o driver do celular, repita o mesmo trecho com o mesmo save, resolução e limite de FPS e exporte um segundo diagnóstico. Na issue, identifique cada ZIP pelo driver, informe o modelo do aparelho, SoC/GPU, versão do Android, versão do N+ Recomp e versão do jogo. Um vídeo curto ajuda a mostrar falhas que o contador de FPS não revela. Revise os anexos antes de publicá-los e deixe de fora dados pessoais, chaves, jogos e saves.

## Origem, créditos e compilação

- A equipe Mesa/Freedreno desenvolve o Turnip. A soma publicada para a fonte 26.3.0 corresponde à usada na receita. [Documentação do Freedreno](https://docs.mesa3d.org/drivers/freedreno.html) · [Versão 26.3.0 e SHA-256 oficial](https://docs.mesa3d.org/relnotes/26.3.0.html) · [Licenças do Mesa](https://docs.mesa3d.org/license.html)
- O backend IMapper5 adapta o trabalho de **Leb-Sun**. A família de ajustes comunitários de resolve e máscara de cor LRZ para Adreno 8xx também tem contribuições de **Vauzi-17**, creditadas pelo Droid-Deck. [Créditos do Droid-Deck](https://github.com/Droid-Deck/Drivers#patches)
- **sinxzinho97 / N+ Recomp** mantém a variante e a integração com o menu. O pacote foi compilado com o Android NDK r28c e traz os avisos do Mesa e do NDK em `LICENSE.Mesa.txt` e `NOTICE.NDK.txt`. A origem e as somas estão em `NOTICE.txt`. [Perfil do mantenedor](https://github.com/sinxzinho97) · [Android NDK r28c](https://github.com/android/ndk/wiki/Unsupported-Downloads#r28c)

Para compilar em Linux x86-64, instale Python 3 com venv e pip, ferramentas de compilação C/C++, Ninja, pkg-config, Flex, Bison, glslang-tools, GNU patch, curl, tar, xz e unzip. Execute o comando na raiz dos fontes desta release.

```sh
bash driver/compilar-turnip.sh package v7
```

A receita confere os arquivos de origem, aplica o patch cumulativo e gera `driver/n-plus-turnip-V7.zip` com os avisos e a biblioteca. A soma do ZIP identifica o download da release. Horários dos arquivos e diferenças na ferramenta de compilação podem alterar o hash de uma nova compilação. [Patch aplicado ao Mesa](../driver/patches/mesa-26.3.0-nplus-v7.patch) · [Receita de compilação](../driver/compilar-turnip.sh)

| Arquivo desta release | SHA-256 |
| --- | --- |
| `n-plus-turnip-V7.zip` | `bdba49e020e196191760a1cd17710943cd1ac26f97cc896e4889494e5a55eedc` |
| `libvulkan_freedreno.so` dentro do ZIP | `9e170b541c16fb6ddcd82404857bef85b0bf7b79f798630f0edae6c0675fa052` |
| `mesa-26.3.0-nplus-v7.patch` | `43e35ddda1e8e99b65841f16046dde564b8393dd3da3e6fa0f6f5bdfbc9e229f` |
