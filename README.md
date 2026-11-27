# N+ Recomp — Versão 3.7.0

O **N+ Recomp** prepara um aplicativo Android dedicado a cada jogo suportado a partir dos arquivos originais do jogador. Os criadores **Windows x64** e **Android 13+ (ARM64)** compartilham o mesmo catálogo, as mesmas referências de compatibilidade e o mesmo menu dentro do jogo.

## Downloads (`v3.7.0`)

| Plataforma / Item | Arquivo | Tamanho | Como usar |
| --- | --- | --- | --- |
| Android 13 ou superior (ARM64) | `N-Plus-Recomp-3.7.0-android-arm64.apk` | 110,43 MB | Instale o APK do criador (mantém a assinatura anterior para atualização direta). |
| Windows x64 | `N-Plus-Recomp-3.7.0-windows-x64.zip` | 608,53 MB | Extraia a pasta inteira e abra `N+ Recomp.exe`. |
| Driver de vídeo Adreno | `n-plus-turnip-V8.zip` | 2,66 MB | Opcional para GPUs Qualcomm Adreno compatíveis. Importe fechado (`.zip` ou `.rar`) pelo menu de vídeo do jogo ou durante a criação. |

Verifique a integridade dos downloads em [`SHA256SUMS.txt`](SHA256SUMS.txt):
- `N-Plus-Recomp-3.7.0-android-arm64.apk`: `076d70531625aea3945471e93a175bdb3683a2024558278a6354fce0e5d1c6aa`
- `N-Plus-Recomp-3.7.0-windows-x64.zip`: `7d330c3b780a0c844e2fef2215913bd739e33214234d395a262cfd84b8c80136`
- `n-plus-turnip-V8.zip`: `86e93ceeda63d5ab117012310c54b3e2839e229ad2185b3f1e5255bb5849c56d`

## Principais novidades da 3.7.0

- **Estabilidade Exynos + Snapdragon e driver Turnip V8**: melhorias de gerenciamento de VRAM nos hosts para Exynos/Xclipse 940, correções específicas em *Dragon Ball: Sparking! ZERO* (`2.0.73`) e driver `n-plus-turnip-V8.zip` atualizado.
- **Interface redesenhada e criação simplificada**: menos etapas na aba **Criar**, opções avançadas recolhidas, bloqueio de títulos fora do catálogo, confirmação para updates experimentais e remoção das abas `Assinaturas` e `Saves`.
- **Chaves de assinatura automáticas**: salvas e lidas automaticamente na pasta `keys` (`<destino>/keys/` no PC e `Android/media/org.nx2a.builder.mods/keys/` no celular) para manter atualizações compatíveis entre PC e Android.
- **Menu dentro do jogo renovado + `.zip`/`.rar` + vários mods**: seleção de múltiplos mods simultâneos em `.zip` ou `.rar`, importação de drivers em `.zip` ou `.rar` e ativação imediata logo após importar.

## Jogos funcionais (71 títulos verificados)

| Jogo | Versões de referência | Onde foi testado |
| --- | --- | --- |
| 13 Sentinels: Aegis Rim | 1.10 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| 13 Sentinels: Aegis Rim (Asia) | 1.00 | v0 Xiaomi 23117RK66C (Snapdragon 8 Gen 3, Adreno 750, Android 16) |
| Advance Wars 1+2: Re-Boot Camp | 1.0.0 | v0 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Animal Crossing: New Horizons | 3.0.3 | v2228224 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Blasphemous 2 | 1.0.8 | v524288 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Captain Toad: Treasure Tracker | 1.4.2 | v393216 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Cardfight!! Vanguard Dear Days 2 | 1.7.2 | v1441792 AYN Odin 2 (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Castlevania: Belmont's Curse | 1.1.0 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Celeste | 1.4.1.1 | v589824 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| DARK SOULS: REMASTERED | 1.0.3 | v196608 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Disco Elysium - The Final Cut | 1.0.7 | v0 (1.0.7) Sony XQ-DQ72 (Adreno 740) and OnePlus 15 (Snapdragon 8 Elite Gen 5), 2026-11-10 |
| Divinity: Original Sin 2 - Definitive Edition | 1.0.12 | v786432 Legion Y700 Gen 4 (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Donkey Kong Country Returns HD | 1.1.0 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| DRAGON BALL: Sparking! ZERO | 1.0.0, 2.0.73 | 1.0.0, 2.0.7 e 2.0.73 (início de gameplay) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8); 2.0.73: Batalha Personalizada e terreno em combate no Samsung Galaxy S25 FE (Exynos 2400, Xclipse 940, driver Samsung). |
| DRAGON QUEST XI S: Echoes of an Elusive Age – Definitive Edition | 1.0.4, 1.0.3 | 1.0.4 (início de gameplay) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8); referência anterior AYN Odin 2 (Adreno 740, Turnip). Versões 1.0.4 (v262144) e 1.0.3 (v196608) registradas com decodificador LZ5 embarcado. |
| FINAL FANTASY RESONANCE | 1.0.1 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| FINAL FANTASY RESONANCE (Asian release) | 1.0.1 | v65536 Lenovo Legion Y700 TB321FU (Snapdragon 8 Gen 3, Adreno 750, Android 16) |
| Fire Emblem Engage | 2.0.0 | v327680 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Fire Emblem: Three Houses | 1.2.0 | v327680 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| FM24 Touch | 1.0.1 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Football Manager 26 Touch | 1.0.2 | v131072 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Graveyard Keeper 2 | 1.0.4 | v262144 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Hades II | 1.0.141667, 0.0.126424 | v655360 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Hollow Knight: Silksong | 1.0.30000 | v655360 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Kirby and the Forgotten Land | 1.1.0 | v65536 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Kirby’s Return to Dream Land Deluxe | 1.0.0 | v0 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Layton's Mystery Journey: Katrielle and the Millionaires' Conspiracy DX+ | 1.1.0 | v65536 iQOO 9 V2171A (Snapdragon 8 Gen 1, Adreno 730, Android 15) |
| Lonely Mountains: Downhill | 1.0.5 | v0 Retroid Pocket 6 (QCS8550, Adreno 740, Android 13); PurpleVK-public git-62ac221a33 |
| Mario vs. Donkey Kong | 1.0.1 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| MEGAMAN BATTLE NETWORK LEGACY COLLECTION Vol.1 | 1.0.2 | v131072 (1.0.2) AYN Odin 2 (QCS8550, Adreno 740, Android 13, Turnip), 2026-11-14 |
| MEGAMAN BATTLE NETWORK LEGACY COLLECTION Vol.2 | 1.0.3 | v196608 (1.0.3) AYN Odin 2 (QCS8550, Adreno 740, Android 13, Turnip), 2026-11-13 |
| Metroid Dread | 2.1.0 | v327680 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Monster Hunter Rise | 16.0.2 | 16.0.2 (início de gameplay; criado do zero no celular) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8) |
| NEO: The World Ends with You | 1.03 | v196608 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| NOBUNAGA'S AMBITION: Shinsei | 1.0.1 | v65536 Lenovo Legion Y700 TB321FU (Snapdragon 8 Gen 3, Adreno 750, Android 16) |
| OCTOPATH TRAVELER 0 | 1.0.5 | v327680 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Paper Mario: The Origami King | 1.0.1 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Picross S＋ | 1.0.1 | v65536 Retroid Pocket 6 (Adreno 740, Android 13); PurpleVK-public git-62ac221a33 |
| Pokémon Brilliant Diamond | 1.3.0 | v393216 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Pokémon Legends: Arceus | 1.1.1 | v262144 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Pokémon Legends: Z-A | 2.0.2 | v393216 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Pokémon Mystery Dungeon Rescue Team DX | 1.0.2 | 1.0.2 AYN Odin 2 (Adreno 740, Turnip) |
| Pokémon Scarlet | 4.0.0, 1.0.0 | 1.0.0 e 4.0.0 (com mods) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830) |
| Pokémon Shield | 1.3.2 | v458752 AYN Odin 2 (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Pokémon Shining Pearl | 1.3.0 | 1.3.0 (início de gameplay) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8) |
| Pokémon Sword | 1.3.2 | v458752 AYN Odin 2 (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Pokémon Violet | 4.0.0 | 4.0.0 AYN Odin 2 (Adreno 740, Android 13, Turnip) |
| Rhythm Heaven Groove | 1.0.0 | v0 Xiaomi 15 (Snapdragon 8 Elite, Adreno 830, Android 16) |
| ROMANCE OF THE THREE KINGDOMS XIV | 1.1.1 | v786432 Xiaomi 2410DPN6CC haotian (Snapdragon 8 Elite, Adreno 830, Android 16) |
| South Park™: The Stick Of Truth™ | 1.0.0 | v0 Xiaomi Pad 5 21051182G (Snapdragon 860, Adreno 640, Android 13) |
| Super Mario 3D World + Bowser's Fury | 1.2.2 | v262144 AYN Thor (Snapdragon 8 Gen 2, Adreno 740, Android 13) |
| Super Mario Bros. Wonder | 1.0.0, 1.2.1 | v327680 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Super Mario Odyssey | 1.4.1 | v393216 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Super Robot Wars 30 | 1.2.3 | v655360 Lenovo Legion Y700 TB321FU (Snapdragon 8 Gen 3, Adreno 750, Android 16) |
| Tales of Berseria Remastered | 1.0.5 | v262144 (1.0.5) Sony XQ-DQ72 (Adreno 740) and OnePlus 15 (Snapdragon 8 Elite Gen 5) |
| Tales of Eternia Remastered | 2.0.0 | v65536 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| The Legend of Zelda: Breath of the Wild | 1.9.0, 1.6.0 | 1.6.0 e 1.9.0 (com mods) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8) |
| The Legend of Zelda: Echoes of Wisdom | 1.1.0 | v196608 Retroid Pocket 6 (Adreno 740, PurpleVK) |
| The Legend of Zelda: Link's Awakening | 1.1.0 | v131072 Lenovo TB323FU (Snapdragon 8 Elite Gen 5, Adreno 840, Android 16) |
| The Legend of Zelda: Tears of the Kingdom | 1.4.3, 1.2.1 | 1.2.1 e 1.4.3 (com mods) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8) |
| The World Ends with You -Final Remix- | 1.0.0 | v0 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Tomodachi Life: Living the Dream | 1.0.4 | v262144 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Ultra Kaiju Monster Rancher | 1.0.1 | v0 AYN Odin 2 (Snapdragon 8 Gen 2, Adreno 740, Turnip driver), tutorials and battles |
| UNDER NIGHT IN-BIRTH Exe:Late[cl-r] | 1.0.3 | v131072 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| UNDER NIGHT IN-BIRTH II Sys:Celes | 1.42 | v1179648 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Unpacking | 2.01 | v327680 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Untitled Goose Game | 1.1.2, 1.0.0 | v458752 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Viractal | 1.4.5 | v131072 Lenovo Legion Y700 TB322FC (Snapdragon 8 Elite, Adreno 830, Android 16) |
| Xenoblade Chronicles X: Definitive Edition | 1.0.2 | 1.0.2 (início de gameplay; criado do zero no celular) — Samsung Galaxy S25 Ultra (SM-S938B, Snapdragon 8 Elite, Adreno 830, N+ Turnip V8) |
| Xenoblade Chronicles: Definitive Edition | 2.0.0 | v262144 AYN Odin 2 (Snapdragon 8 Gen 2, Adreno 740, Android 13); Turnip (vulkan.ad07xx.so) |
| 歧路旅人0 OCTOPATH TRAVELER 0 | 1.0.5 | v327680 Xiaomi 23117RK66C (Android 16) |

## Como preparar ou atualizar

1. Na aba **Criar**, selecione o jogo base, eventuais updates/DLCs, seu arquivo `prod.keys` (e firmware quando necessário) e a pasta de destino.
2. Clique em **Criar** para gerar o APK do jogo usando a versão escolhida.
3. Para atualizar um jogo já criado no aparelho para o motor e menu mais recentes mantendo dados e assinatura, use a aba **Atualizar**.
4. Dentro do jogo, importe **mods** ou **drivers de vídeo** em arquivo fechado **`.zip` ou `.rar`**; ao concluir, confirme se deseja ativar na hora.

## Créditos

- Criação e manutenção do N+ Recomp: **sinxzinho97** ([github.com/sinxzinho97](https://github.com/sinxzinho97))
- Base de compatibilidade e integração Android: **nx2android**, por **shirai91** ([github.com/shirai91/nx2android](https://github.com/shirai91/nx2android))
