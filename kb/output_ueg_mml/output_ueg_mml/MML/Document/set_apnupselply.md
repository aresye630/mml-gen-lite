# 设置APN粒度的UP选择策略（SET APNUPSELPLY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于控制APN粒度的UP选择策略。

## 注意事项

- 该命令执行后立即生效。

- 如果没有更细粒度的配置，在此APN内，整机配置(UPSELECTFLAG)的UP选择策略被本配置覆盖。
- 在每次执行ADD CPAPN命令时会自动为本命令增加一条记录。

  记录中参数的初始设置值如下：

  PSAPOSPRIFLAG: INHERIT

  COMBINEPRISTG: COMBINEFIRST

  COMBINEDSELSTG: TAIPRI

  LOCS11SELSTG:PRIORITYFIRST

  ULISGWFLAG: INHERIT

  SHAREDPRIFLAG: DISABLE

  PRIORITYFLAG: INHERIT

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:---------------|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称                    | 可选必选说明：必选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无。  配置原则：  该参数使用ADD CPAPN命令配置生成。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSAPOSPRIFLAG  | 基于位置条件优选主锚点UPF的开关        | 可选必选说明：可选参数  参数含义：该参数用于指示APN粒度下基于位置优选主锚点UPF开关。 当此开关为ENABLE时，SMF优先选择支持位置与当前用户所在位置相匹配的UPF作为主锚点。 主锚点包括PSA UPF、PGW-U、GGSN。  数据来源：本端规划 取值范围： “INHERIT（继承全局）”：继承整机的基于位置优选主锚点UPF开关(UPSELECTFLAG:PSAPOSPRIFLAG)。DISABLE（关）ENABLE（开）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                     |
| ULISGWFLAG     | 基于ULI For SGW位置选择SGW-U开关 | 可选必选说明：可选参数  参数含义：该参数用于控制SMF在进行SGW-U选择时，在ULI信元为空时是否优先使用ULI For SGW进行选择。  数据来源：本端规划 取值范围： “INHERIT（继承全局）”：继承整机的基于ULI For SGW选择SGW-U开关(UPSELECTFLAG:ULISGWFLAG)。“DISABLE（关）”：当ULI信元为空，使用S11接口绑定UPF进行SGW-U选择。“ENABLE（开）”：当ULI信元为空，而ULI For Sgw信元可用时，优先使用Uli For Sgw信元作为位置进行SGW-U选择。如果Uli For Sgw信元也为空，使用S11接口绑定UPF进行SGW-U选择。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：  4G切换场景下，如果SMF需要在ULI信元为空时，优先使用ULI For SGW信元代替ULI信元进行UP选择，则使能此开关。                                                                                                                                                                                                                                       |
| SHAREDPRIFLAG  | 分流场景下共享UPF优选开关           | 可选必选说明：可选参数  参数含义：该参数用于指示在该APN下，SMF在分流场景下是否优选共享UPF。该优选策略属于合一优先选择，生效顺位与合一优先选择相同。  数据来源：本端规划 取值范围： DISABLE（关）“ENABLE（开）”：分流场景下优选共享UPF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRIORITYFLAG   | 基于优先级优选UPF开关             | 可选必选说明：可选参数  参数含义：该参数用于指示该APN下SMF基于优先级选择UPF的功能是否开启。  数据来源：本端规划 取值范围： “INHERIT（继承）”：继承整机的基于优先级优选UPF开关(UPSELECTFLAG:PRIORITYFLAG)。“DISABLE（关）”：关闭基于优先级选择UPF功能。“ENABLE（开）”：打开基于优先级选择UPF功能。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则： 可以使用不同粒度的配置打开基于优先级选择UPF的功能（UPSELECTFLAG:PRIORITYFLAG、APNUPSELPLY:PRIORITYFLAG、DNAIUPSELPLY:PRIORITYFLAG）。如果要使优先级优选容许过载UPF开关（UPSELECTFLAG:OVERLOADALWFLAG）、合一与优先级优选策略（APNUPSELPLY:COMBINEPRISTG）、选择合一UPF的优先级策略（APNUPSELPLY:COMBINEDSELSTG）生效，需要打开基于优先级选择UPF的功能。基于PNFPROFILE、PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF优先级需要在打开基于优先级选择UPF的功能后才生效。基于PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF特定容量需要在打开基于优先级选择UPF的功能后才生效。 |
| COMBINEPRISTG  | 合一与优先级优选策略               | 可选必选说明：可选参数  参数含义：该参数用于指示UNC选择UPF时优先选择合一部署UPF还是优选优先级最高的UPF。  数据来源：本端规划 取值范围： “COMBINEFIRST（合一优先）”：合一优选的级别高于优先级。“PRIORITYFIRST（优先级优先）”：优先级级别高于合一优选。若合一UPF同时具备最高优先级，则优选此类UPF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：  若要使本策略生效，需要打开基于优先级优选UPF开关（UPSELECTFLAG:PRIORITYFLAG或APNUPSELPLY:PRIORITYFLAG或DNAIUPSELPLY:PRIORITYFLAG）。                                                                                                                                                                                                                                                                                                                                            |
| COMBINEDSELSTG | 选择合一UPF的优先级策略            | 可选必选说明：可选参数  参数含义：该参数用于指示在该命令“APN”参数所指定的APN条件下，UNC优选主锚点与接入点合一UPF的优先级策略。  数据来源：本端规划 取值范围： “TAIPRI（按TAI/TAIRANGE/SMFSERVINGAREA优先级优选）”：UNC选择主锚点和接入锚点合一部署UPF时，按照UPF的TAI/TAIRANGE/SMFSERVINGAREA优先级优选。“APNPRI（按APN/DNN优先级优选）”：UNC选择主锚点和接入锚点合一部署UPF时，按照UPF的APN/DNN优先级优选。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：  若要使本策略生效，需要打开基于优先级优选UPF开关（UPSELECTFLAG:PRIORITYFLAG或APNUPSELPLY:PRIORITYFLAG或DNAIUPSELPLY:PRIORITYFLAG）。                                                                                                                                                                                                                                                    |
| LOCS11SELSTG   | 位置区S11口与优先级优选策略          | 可选必选说明：该参数在"COMBINEPRISTG"配置为"COMBINEFIRST"时为条件可选参数。  参数含义：该参数用于指示UNC选择UPF时优先选择位置区\S11口UPF还是优选优先级高的UPF。  数据来源：本端规划 取值范围： PRIORITYFIRST（优先级优先）LOCS11FIRST（位置区或S11口优先）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNUPSELPLY查询当前参数配置值。  配置原则：  若要使本策略生效，需要打开基于优先级优选UPF开关（UPSELECTFLAG:PRIORITYFLAG或APNUPSELPLY:PRIORITYFLAG或DNAIUPSELPLY:PRIORITYFLAG），设置up选择条件开关的第一优先级（UPSELEPRI:FIRSTPRIORITY）为合一的UPF，且设置合一与优先级优选策略（APNUPSELPLY:COMBINEPRISTG）为合一优先。                                                                                                                                                                                                                                                    |

## 使用实例

- APN配置位置优选锚点UPF的开关为ENABLE。

  ```
  SET APNUPSELPLY: APN="test",PSAPOSPRIFLAG=ENABLE;
  ```
- APN配置基于优选级优选UPF时优先考虑合一。
  在SMF选主锚点UPF和接入UPF时，UNC先基于合一优选，然后基于合一UPF的优先级策略进行优选。
  在已选定辅锚点的场景下，SMF需要选择主锚点时，SMF基于主辅合一优选主锚点。

  ```
  SET APNUPSELPLY: APN="test", COMBINEPRISTG=COMBINEFIRST;
  ```
- APN配置基于优选级优选UPF时优先考虑优先级。
  在SMF选主锚点UPF和接入UPF时，SMF基于APN/DNN优先级优选主锚点UPF，基于TAI/TAIRANGE/SMFSERVINGAREA优先级优选接入UPF。若合一UPF同时具备APN/DNN条件和TAI/TAIRANGE/SMFSERVINGAREA条件的最高优先级，则最优选此类合一UPF。
  在已选定辅锚点的场景下，SMF需要选择主锚点时，SMF基于APN/DNN优先级优选主锚点UPF。若合一UPF同时具备APN/DNN条件的最高优先级，则最优选此UPF。

  ```
  SET APNUPSELPLY: APN="test", COMBINEPRISTG=PRIORITYFIRST;
  ```
- APN配置在SMF选择主锚点和接入点已合一的UPF时，按照UPF的TAI/TAIRANGE/SMFSERVINGAREA优先级优选。

  ```
  SET APNUPSELPLY: APN="test", COMBINEDSELSTG=TAIPRI;
  ```
- APN配置在SMF选择主锚点和接入点已合一的UPF时，按照UPF的APN/DNN优先级优选。

  ```
  SET APNUPSELPLY: APN="test", COMBINEDSELSTG=APNPRI;
  ```
- APN配置在分流场景下,SMF优先选择共享UPF。

  ```
  SET APNUPSELPLY: APN="test", SHAREDPRIFLAG=ENABLE;
  ```
- APN配置SMF开启基于优先级选项UPF功能。

  ```
  SET APNUPSELPLY: APN="test", PRIORITYFLAG=ENABLE;
  ```