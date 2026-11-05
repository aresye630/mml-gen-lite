# UEG 特性文档 — 5G 接口与特性名称映射

UEG v21.12.2 特性文档中，5G 核心网接口不总是以 "配置{Nx}接口数据" 命名，部分接口的配置分布在其他特性中。

## 已知映射

| 接口 | 特性名称 | 说明 |
|------|---------|------|
| N2 (AMF ↔ RAN) | *嵌入 AMF 特性中，无独立文档* | AMF 侧配置 |
| N3 (UPF ↔ RAN) | 配置Sa/N3/S1-U接口数据 | UPF 到 (R)AN 侧用户面 |
| N4 (SMF ↔ UPF) | 配置N4(N4/Sxa/Sxb)接口数据 | 控制面/用户面分离 |
| N6 (UPF ↔ DN) | 激活N6/Gi/SGi接口IPv6组网 | N6 接口 IPv6 组网，仅针对 UPF |
| N6 (UPF ↔ DN) | 配置N6侧免VxLAN隧道层二以太通信 | N6 侧免 VXLAN 隧道方案 |
| N8 (AMF ↔ UDM) | *嵌入 AMF+UDM 特性中* | — |
| N10 (SMF ↔ UDM) | *嵌入 SMF+UDM 特性中* | — |
| N11 (AMF ↔ SMF) | *嵌入 AMF+SMF 特性中* | — |
| N12 (AMF ↔ AUSF) | *嵌入 AMF+AUSF 特性中* | — |
| N14 (AMF ↔ AMF) | *嵌入 AMF 间特性中* | — |
| N15 (AMF ↔ PCF) | *嵌入 AMF+PCF 特性中* | — |
| N16 (SMF ↔ SMF) | *嵌入 SMF 间特性中* | — |
| N19 (UPF ↔ UPF) | 配置N19接口 | UPF 间 N19 隧道 |
| N26 (AMF ↔ MME) | 配置N26接口数据 | 4G/5G 互操作 |
| Nxuc (UPF ↔ UPF) | 配置Nxuc接口数据 | UPF 间用户面连接 |
| S1-MME (eNB ↔ MME) | 配置S1-MME接口数据 | 4G 控制面 |
| S1-U (eNB ↔ SGW-U) | 配置Sa/N3/S1-U接口数据 | 4G 用户面 |
| S5-S / S8-S (SGW-C ↔ PGW-C) | 配置Sc/N9c/S5-S/S8-S接口数据 | 4G 控制面 |
| S5-P / S8-P (SGW-U ↔ PGW-U) | 配置Pa(N9a/S5-P/S8-P/S2b)接口数据 | 4G 用户面 |
| S6a (MME ↔ HSS) | 配置S6a接口数据 | 4G 鉴权 |
| S10 (MME ↔ MME) | *与 N26 共用* | MME 间信令 |
| S11 (MME ↔ SGW-C) | 配置S11-C接口数据 | 4G 控制面 |
| S11-U (MME ↔ SGW-U) | 配置S11-U接口数据 | 4G 用户面 |

## 无独立特性的接口

以下接口的配置数据分散在对应 NF 的全局/公共特性中，无独立文档标题：
- N2, N8, N10, N11, N12, N14, N15, N16（AMF/SMF/UDM 内部配置）
- Gi/SGi（已归入 N6/Gi/SGi 接口 IPv6 组网特性）

## 注意事项

- N6 接口的基础配置（逻辑接口/VPN/路由）在 UEG 中没有独立的 "配置N6接口数据" 特性，但 UPF 到 DN 的配置通常参考 配置Sa/N3/S1-U接口数据 中的类似逻辑接口配置模式。
- v21.12.2 移除了部分旧版子目录（common/desc/feature/fenix/kite_l/om/sae/udm/upcc），接口对应的特性可能已被归并。
