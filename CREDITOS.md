# Quem fez o N+ Recomp

**shirai91 (Tung Pham)** criou o **nx2android**, que levou para o Android o trabalho do **nxnative**. **seedds** criou o **nxnative**, o motor e as ferramentas originais de preparação. Esses dois projetos tornaram possível criar aplicativos Android dedicados a cada jogo. O N+ Recomp incorporou a revisão `f3da64f` do nx2android. [nx2android](https://github.com/shirai91/nx2android) · [Revisão integrada](https://github.com/shirai91/nx2android/tree/f3da64f7816209491e66e902af52b00fd39ca4c8) · [nxnative](https://github.com/seedds/nxnative) · [Licença MIT original](licencas/nxnative-MIT.txt)

**sinxzinho97** mantém o N+ Recomp. Esta edição integra os criadores para Android e Windows, o menu dos jogos, a gestão de mods, controles, saves e drivers e as atualizações de motor. Os testes em aparelhos reais e os diagnósticos enviados pelos jogadores orientam as correções. [Perfil do mantenedor](https://github.com/sinxzinho97)

## Renderização e driver opcional

O tradutor de shaders usa trabalho dos colaboradores do **Ryujinx**. O motor também incorpora trabalho dos projetos **libadrenotools**, **Vulkan-Headers**, **bcdec**, **Zstandard** e **Fusion Pixel Font**, entre outros. Os avisos por componente e os créditos às adaptações de **MacNativeGames** e **deko3d** acompanham a árvore `nxnative/dm/third_party` no pacote Windows. O filtro **FidelityFX Super Resolution 1** usa código da **AMD**. [AMD FidelityFX FSR](https://github.com/GPUOpen-Effects/FidelityFX-FSR) · [Licença do FSR](licencas/AMD-FSR1-MIT.txt)

O **N+ Turnip V7** é uma variante do driver Vulkan **Turnip**, do projeto **Mesa/Freedreno**. O guia do driver identifica as contribuições comunitárias, a receita de compilação e os aparelhos para os quais se destina. [Créditos, fontes e uso do driver](docs/DRIVER.md)

## Fontes e licenças do pacote Windows

Depois de extrair o ZIP, abra a pasta `N-Plus-Recomp`. Os caminhos abaixo partem dessa pasta. O código da interface está em `gui`, o de preparação em `porter` e os scripts de empacotamento em `packaging`. As licenças dos componentes acompanham a distribuição.

| Componente distribuído | Onde obter os fontes e avisos |
| --- | --- |
| **Qt 6.12.0**, da The Qt Company e colaboradores. Inclui Base, Declarative, SVG, Image Formats, Virtual Keyboard e traduções. | [Fontes completos da versão (.tar.xz)](https://download.qt.io/official_releases/qt/6.12/6.12.0/single/qt-everywhere-src-6.12.0.tar.xz) · [Downloads por módulo](https://download.qt.io/official_releases/qt/6.12/6.12.0/submodules/) |
| **Qt for Python 6.12.0**, incluindo PySide6 e Shiboken. | [Fontes e scripts de compilação (.tar.xz)](https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.12.0-src/pyside-setup-everywhere-src-6.12.0.tar.xz) · [Opção ZIP e checksums](https://download.qt.io/official_releases/QtForPython/pyside6/PySide6-6.12.0-src/) |
| **Qt PDF 6.140.0**, distribuído pela wheel PySide6-Pdf 6.12.0.140. O módulo usa PDFium e componentes de Chromium. | [Fontes do Qt WebEngine com Qt PDF e terceiros (.tar.xz)](https://download.qt.io/official_releases/qtwebengine/6.140/6.140.0/src/qtwebengine-everywhere-src-6.140.0.tar.xz) · [Licenças de Qt PDF e componentes](https://doc.qt.io/qtpdf/qtpdf-licensing.html) |
| **PyInstaller 6.22.3**, da equipe PyInstaller. O carregador do executável foi compilado a partir da distribuição de fontes dessa versão. | `packaging/build_bootloader.py` e `licenses/PyInstaller-6.22.3/licenses/COPYING.txt` no ZIP. [Fontes oficiais](https://pypi.org/project/pyinstaller/6.22.3/#files) · [Exceção de licenciamento do bootloader](https://pyinstaller.org/en/stable/license.html) |
| **Decoder Kraken do Arceus**, derivado de **ooz**, de **Powzix**. O executável auxiliar roda em processo separado e recebe os dados pela entrada padrão. | O ZIP traz o fonte modificado completo, o histórico das adaptações e a GPLv3 ou posterior em `packaging/arceus-decoder`. Para recompilar no Windows x64 com o Visual C++ Build Tools e o Windows SDK, execute `python packaging/build_arceus_decoder.py` a partir de `N-Plus-Recomp`. [Revisão original de ooz](https://github.com/powzix/ooz/tree/05038060aa68f9187ae9923b2388ca8db40e58d1) |

As bibliotecas Qt e os plugins são carregados como arquivos separados sob `_internal`. Para experimentar uma compilação modificada, substitua as DLLs ou plugins correspondentes em uma cópia da pasta extraída, mantendo os caminhos e a compatibilidade binária x64. O ZIP contém os textos das licenças em `licenses/Qt` e os metadados das wheels em `licenses`. A edição aberta do Qt Virtual Keyboard tem licença GPLv3. As condições de uso variam por módulo. [Licenciamento do Qt](https://doc.qt.io/qt-6/licensing.html) · [Qt Virtual Keyboard](https://doc.qt.io/qt-6/qtvirtualkeyboard-index.html) · [Avisos de terceiros do Qt](licencas/Qt-avisos-terceiros.txt)

## Componentes do criador Android

O APK incorpora **CPython**, **Capstone**, **python-lz4/LZ4**, **PyYAML**, **OpenSSL**, **SQLite**, **LibHac** de Alex Barney, **SharpCompress** de Adam Hathcock e colaboradores, além de componentes da **Microsoft/.NET**, do **Ryujinx** e do ecossistema **Android/AOSP**. Seus avisos acompanham o APK. Para consultá-los em outro aparelho, abra o APK como ZIP, depois abra `assets/runtime/payload.zip` e entre em `licenses`. Os avisos do SharpCompress incluem a atribuição do UnRAR. [CPython](https://www.python.org/) · [Capstone](https://www.capstone-engine.org/) · [SharpCompress](https://github.com/adamhathcock/sharpcompress) · [.NET](https://github.com/dotnet/runtime)
