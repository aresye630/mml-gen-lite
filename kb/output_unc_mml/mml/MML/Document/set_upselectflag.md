# 设置UPF选择条件开关（SET UPSELECTFLAG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于设置SMF的整机UPF选择条件开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| N3UPFAPNFLAG   | ULISGWFLAG   | AMBRUPFFLAG   | UPFBLOCKFLAG   | ROAMTYPEFLAG   | NGLANUPFSELSW   | LEASEUPFFLAG   | LOCALITYFLAG   | PSAPOSPRIFLAG   | OVERLOADFLTFLAG   | PRIORITYFLAG   | OVERLOADALWFLAG   | LOADFLTFLAG   | LOCKAPNFLAG   | ACCLOCKAPNFLAG   | UPSRVSTATUSFLAG   |
|:---------------|:-------------|:--------------|:---------------|:---------------|:----------------|:---------------|:---------------|:----------------|:------------------|:---------------|:------------------|:--------------|:--------------|:-----------------|:------------------|
| DISABLE        | DISABLE      | DISABLE       | ENABLE         | DISABLE        | LOCALABILITY    | ENABLE         | DISABLE        | DISABLE         | DISABLE           | DISABLE        | DISABLE           | ENABLE        | DISABLE       | DISABLE          | DISABLE           |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------------|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N3UPFAPNFLAG    | I-UPF选择的APN开关            | 可选必选说明：可选参数  参数含义：该参数用于标识SMF选择IUPF时，是否将APN作为必选条件。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  如果需要基于APN条件选择IUPF，建议将此开关打开。在开关开启时，如果未配置UPF支持对应的APN (PNFDNN)，则SMF不会选择该UPF。此开关对整系统生效。在开关开启时，如果未配置UPF支持漫入用户的APN，漫入用户将会接入失败。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ULISGWFLAG      | 基于ULI For SGW选择SGW-U开关   | 可选必选说明：可选参数  参数含义：该参数用于控制GW-C在进行SGW-U选择时，在ULI为空时是否优先使用ULI For SGW进行选择。  数据来源：本端规划 取值范围： “DISABLE（关）”：当ULI信元为空，使用S11接口绑定UPF进行SGW-U选择。“ENABLE（开）”：当ULI信元为空，而ULI For Sgw信元可用时，优先使用ULI For Sgw信元作为位置进行SGW-U选择。如果ULI For Sgw信元也为空，使用S11接口绑定UPF进行SGW-U选择。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  4G切换场景下，如果需要在ULI信元为空时，优先使用ULI For SGW信元代替ULI信元进行UP选择，则使能此开关。                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AMBRUPFFLAG     | AMBR聚合UPF选择开关            | 可选必选说明：可选参数  参数含义：该参数用于标识同一用户的相同DNN下所有会话是否支持优选到相同的主锚点UPF。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| UPFBLOCKFLAG    | UPF选择临时抑制                | 可选必选说明：可选参数  参数含义：该参数用于标识UPF选择临时抑制功能是否打开，ENABLE标识开，DISABLE标识关，默认值为开。 此开关打开后，如果UPF在PDU会话建立流程中响应N4消息超时，则在随后的20s内优先选择其他可用UPF。如果无其他可用UPF，仍可选中该UPF做主锚点和接入UPF，但无法作为辅锚点UPF和ULCL UPF使用。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ROAMTYPEFLAG    | 基于用户漫游类型选择UPF开关          | 可选必选说明：可选参数  参数含义：该参数用于控制在Home Routed漫游场景，是否根据用户漫游类型过滤UPF列表。 通过ADD ROAMTYPEBINDUP增加UPF和用户漫游类型的绑定关系。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  在Home Routed漫游场景，如果希望能够根据用户的漫游类型进行UP选择，需要将此开关打开。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NGLANUPFSELSW   | 5G LAN UPF选择开关           | 可选必选说明：可选参数  参数含义：该参数用于标识5G LAN场景，SMF选择UPF的方式。  数据来源：本端规划 取值范围： “LOCALABILITY（本地能力）”：SMF基于本地配置的UPF 5G LAN支持能力（使用ADD UPNODE中的NGLANSW参数配置）选择UPF。“GCOMABILITY（动态能力）”：SMF基于UPF上报的5G LAN支持能力选择UPF。UPF通过N4偶联消息的GCOM（UPF Support of 5G Vn Group Communication）信元，将UPF支持的5G LAN能力上报携带给SMF。“LOCALANDGCOM（本地及动态能力）”：SMF基于本地配置的UPF 5G LAN支持能力和UPF上报的5G LAN支持能力协商选择UPF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  5G LAN场景选择UPF时：若要完全依赖UPF上报的5G LAN支持能力选择UPF，则置为GCOMABILITY；若要完全依赖SMF本地配置的UPF 5G LAN支持能力选择UPF，则置为LOCABILITY；若要同时依赖UPF上报的5G LAN支持能力和SMF本地配置的5G LAN支持能力选择UPF，则置为LOCALANDGCOM；例如，当UPF上报Support，SMF本地配置为Support时，该UPF可以被选中，当UPF上报Not Support，SMF本地配置为Support时，该UPF不能被选中。                                                                                                                      |
| LEASEUPFFLAG    | 租约UPF选择开关                | 可选必选说明：可选参数  参数含义：该参数用于标识SMF选择主锚点UPF时，是否将租约UPF作为选择条件。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  为了让SMF选择到租约UPF从而让租约地址生效，建议将此开关打开。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LOCALITYFLAG    | 位置区UPF优选开关               | 可选必选说明：可选参数  参数含义：该参数用于指示SMF选择UPF时是否优先选择UPF的位置区优先级高的UPF。 UPF的位置区优先级是通过ADD LOCBINDAREA命令配置的。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  为了让SMF支持优先选择地理位置较近的UPF时，建议将此开关打开。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSAPOSPRIFLAG   | 基于位置优选主锚点UPF开关           | 可选必选说明：可选参数  参数含义：标识基于位置优选主锚点UPF的开关控制，ENABLE标识开，DISABLE标识关，默认值为关。 查询不到APN级别的优选开关时，使用全局开关；否则使用APN级别的优选开关。 当此开关为ENABLE时，SMF优先选择支持位置与当前用户所在位置相匹配的UPF作为主锚点。 主锚点包括PSA UPF、PGW-U、GGSN。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OVERLOADFLTFLAG | 过载UPF过滤开关                | 可选必选说明：可选参数  参数含义：该参数用于控制SMF在进行UPF选择时是否基于UPF过载信息进行UPF过滤，过载信息来自于UPF向SMF上报的OCI信元。  数据来源：本端规划 取值范围： “DISABLE（关）”：关闭过载UPF过滤功能。“ENABLE（开）”：打开过载UPF过滤功能。相对于过载的UPF，UNC优选非过载的UPF。如果所有的UPF全部过载，UNC仍会选出UPF，不对UPF进行过滤。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PRIORITYFLAG    | 基于优先级优选UPF开关             | 可选必选说明：可选参数  参数含义：该参数用于控制SMF基于优先级选择UPF的功能是否开启。如果存在更细粒度的配置（APNUPSELPLY:PRIORITYFLAG、DNAIUPSELPLY:PRIORITYFLAG），在细粒度上会被对应的配置覆盖。  数据来源：本端规划 取值范围： “DISABLE（关）”：关闭UPF的优先级选择功能，UNC选择UPF时不考虑优先级配置。“ENABLE（开）”：打开UPF的优先级选择功能，UNC将基于UPF的APN/DNN优先级选主锚点，基于UPF的DNAI优先级选辅锚点，基于UPF的TAI/TAIRANGE/SMFSERVINGAREA优先级选接入锚点。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则： 可以使用不同粒度的配置打开基于优先级选择UPF的功能（UPSELECTFLAG:PRIORITYFLAG、APNUPSELPLY:PRIORITYFLAG、DNAIUPSELPLY:PRIORITYFLAG）。如果要使优先级优选容许过载UPF开关（UPSELECTFLAG:OVERLOADALWFLAG）、合一与优先级优选策略（APNUPSELPLY:COMBINEPRISTG）、选择合一UPF的优先级策略（APNUPSELPLY:COMBINEDSELSTG）生效，需要打开基于优先级选择UPF的功能。基于PNFPROFILE、PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF优先级需要在打开基于优先级选择UPF的功能后才生效。基于PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF特定容量需要在打开基于优先级选择UPF的功能后才生效。 |
| OVERLOADALWFLAG | 高优先级容许过载UPF开关            | 可选必选说明：该参数在"PRIORITYFLAG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指示SMF基于优先级选择UPF时，相对于优先级低的UPF列表，容许UNC选择最高优先级但全部过载的UPF列表。  数据来源：本端规划 取值范围： “DISABLE（关）”：UNC优先考虑UPF是否过载，在最高优先级全为过载UPF，但次一级优先级存在非过载UPF的情况下，UNC不选择最高优先级的UPF，选择次一级且非过载的UPF。“ENABLE（开）”：UNC优先考虑UPF的优先级，若最高优先级UPF列表中存在非过载的UPF，则选择最高优先级且非过载的UPF。若最高优先级UPF列表UPF全部过载，UNC仍选择最高优先级UPF，不选择次优先级的UPF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  若要使本开关功能生效，需要同时打开过载UPF过滤选择开关（UPSELECTFLAG:OVERLOADFLTFLAG）与优先级优选UPF开关（UPSELECTFLAG:PRIORITYFLAG）。                                                                                                                                                                                                                                                                                                    |
| LOADFLTFLAG     | 基于负载优选UPF开关              | 可选必选说明：可选参数  参数含义：该参数用于控制SMF是否打开基于UPF负载信息进行UPF优选的功能，ENABLE标识打开，DISABLE标识关闭，默认值为打开。如果存在更细粒度的配置（DNAIUPSELPLY:LOADFLTFLAG），在细粒度上会被对应的配置覆盖。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LOCKAPNFLAG     | 基于UPF上报的APN锁定信息选择UPF开关   | 可选必选说明：可选参数  参数含义：该参数用于控制UP选择时，是否基于UPF上报的APN锁定信息，选择APN未锁定的UPF。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  UP选择时，如果需要根据UPF上报的APN锁定信息，选择APN未锁定的UPF，则使能此开关。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ACCLOCKAPNFLAG  | 基于UPF上报的APN锁定信息选择接入UPF开关 | 可选必选说明：该参数在"LOCKAPNFLAG"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于控制接入UP选择时，是否基于UPF上报的APN锁定信息，选择APN未锁定的接入UPF。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  UP选择时，如果需要根据UPF上报的APN锁定信息，选择APN未锁定的接入UPF，则使能此开关。  若要使本开关功能生效，需要同时打开基于UPF上报的APN锁定信息选择UPF开关（UPSELECTFLAG:LOCKAPNFLAG）。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| UPSRVSTATUSFLAG | 基于UP服务状态选择UPF开关          | 可选必选说明：可选参数  参数含义：该参数用于控制SMF是否打开基于UPF上报的服务状态进行UPF选择的功能。  数据来源：本端规划 取值范围： DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPSELECTFLAG查询当前参数配置值。  配置原则：  UP选择时，如果需要根据UPF上报的服务状态进行UPF选择，则使能此开关。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## 使用实例

- 为了使SMF支持优选地理位置较近的UPF场景下，设置位置区优先级为开，其余开关为关：

  ```
  SET UPSELECTFLAG: LOCALITYFLAG = ENABLE, N3UPFAPNFLAG = DISABLE, AMBRUPFFLAG = DISABLE, PSAPOSPRIFLAG = DISABLE;
  ```
- 为了开启过载UPF过滤功能，使能过载UPF过滤开关：

  ```
  SET UPSELECTFLAG: OVERLOADFLTFLAG = ENABLE;
  ```
- 为了开启优选级选择功能，使能基于优先级优选UPF开关：

  ```
  SET UPSELECTFLAG: PRIORITYFLAG = ENABLE;
  ```
- 在同时开启过载UPF过滤功能和开启优选级选择功能时，UNC选择UPF优先考虑过载：

  ```
  SET UPSELECTFLAG: OVERLOADFLTFLAG = ENABLE, PRIORITYFLAG = ENABLE, OVERLOADALWFLAG = DISABLE;
  ```
- 在同时开启过载UPF过滤功能和开启优选级选择功能时，UNC选择UPF优先考虑优先级。若最高优先级UPF列表UPF全部过载，UNC仍选择最高优先级UPF，不考虑次一级的UPF：

  ```
  SET UPSELECTFLAG: OVERLOADFLTFLAG = ENABLE, PRIORITYFLAG = ENABLE, OVERLOADALWFLAG = ENABLE;
  ```
- 为了使SMF基于UPF上报的5G LAN支持能力选择UPF，设置5G LAN UPF选择开关为GCOMABILITY：

  ```
  SET UPSELECTFLAG: NGLANUPFSELSW = GCOMABILITY;
  ```
- 在4G切换场景下，如果需要在ULI信元为空时，优先使用ULIForSGW信元代替ULI信元进行UP选择，设置基于ULIForSGW选择SGW-U开关为ENABLE：

  ```
  SET UPSELECTFLAG: ULISGWFLAG = ENABLE;
  ```
- 在Home Routed漫游场景下，为了开启用户漫游类型过滤功能，使能基于用户漫游类型选择UPF开关：

  ```
  SET UPSELECTFLAG: ROAMTYPEFLAG = ENABLE;
  ```
- UP选择时，如果需要根据UPF上报的APN锁定信息，选择APN未锁定的锚点UPF和接入UPF，使能基于UPF上报的APN锁定信息选择UPF开关和基于UPF上报的APN锁定信息选择接入UPF开关：

  ```
  SET UPSELECTFLAG: LOCKAPNFLAG = ENABLE, ACCLOCKAPNFLAG = ENABLE;
  ```
- UP选择时，如果需要根据UPF上报的服务状态进行UPF选择，使能基于UP服务状态选择UPF开关：

  ```
  SET UPSELECTFLAG: UPSRVSTATUSFLAG = ENABLE;
  ```