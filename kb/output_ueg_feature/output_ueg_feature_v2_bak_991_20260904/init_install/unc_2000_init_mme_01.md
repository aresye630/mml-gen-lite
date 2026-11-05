# 公共参数配置（MME）

- 操作场景
- 必备事项
- 操作步骤

## 操作场景

本章节用于指导MME的公共数据配置，包括PLMN、MMEID等。

以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- 已经获取网设LLD文档。

数据

**说明** 

如下数据仅为举例，请注意修改成局点规划的数据。

| 类别        | 参数名称                 | DC1取值样例   | DC2取值样例   | 获取方法   | 说明                                                                                                                                                                                             |
|:----------|:---------------------|:----------|:----------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET CPSYS | 系统描述（DESC）           | HCGPBER1  | HCGPBER1  | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 系统标识（ID）             | 0         | 0         | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 系统名称（NM）             | HCGPBER1  | HCGPBER1  | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 服务描述（SRV）            | prsBER1   | prsBER1   | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 移动网号（MNC）            | 03        | 03        | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 移动国家码（MCC）           | 123       | 123       | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 协议版本（PROVER）         | R4        | R4        | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 核心网标识（CNID）          | 0         | 0         | 整网规划   | 配置系统基本信息。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                                  |
| SET CPSYS | 设备能力（CAP）            | 255       | 0         | 整网规划   | 主备场景下：主用的CAP值为255，备用的CAP值为0。 负荷分担场景下：两套UEG的CAP值均为255。                                                                                                                                          |
| ADD HPLMN | 移动国家码（MCC）           | 123       | 123       | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 移动网号（MNC）            | 03        | 03        | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 国家码（CC）              | 86        | 86        | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 是否允许SM业务（SM）         | YES       | YES       | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 最大承载数（MAXSMNUM）      | 7         | 7         | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 是否允许SMS业务（SMS）       | NO        | NO        | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 协议类型（S5S8TYPE）       | GTP       | GTP       | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD HPLMN | 运营商名称（PLMNN）         | noname_1  | noname_1  | 整网规划   | 配置用户的归属PLMN。 园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。                                                                                                                                               |
| ADD MMEID | 移动国家码（MCC）           | 123       | 123       | 整网规划   | 配置MMEID。                                                                                                                                                                                       |
| ADD MMEID | 移动网号（MNC）            | 03        | 03        | 整网规划   | 配置MMEID。                                                                                                                                                                                       |
| ADD MMEID | MME组识别码（MMEGI）       | 8001      | 8001      | 整网规划   | 配置MMEID。                                                                                                                                                                                       |
| ADD MMEID | MME编码（起始值）（MMEC）     | 01        | 02        | 整网规划   | 配置MMEID。                                                                                                                                                                                       |
| SET EMM   | T3412（min）（T3412）    | 15        | 15        | 固定取值   | 该命令中T3412固定设置为15min，其余参数保持初始值设置。 UEG1联动复位后，连接态用户可以快速接入UEG2，但空闲态用户需依靠TAU/SR流程向UEG2发送上行信令来恢复业务，系统默认周期TAU时长较长（5G业务50min，4G业务54min）。由于2B用户量少，可以通过调低周期TAU的时长来触发空闲态用户的业务快速恢复（MME/AMF上TAU周期修改为15min）。 |
| SET EMM   | 移动可达定时器（min）（RCHTMR） | 20        | 20        | 固定取值   | 该命令中T3412固定设置为15min，其余参数保持初始值设置。 UEG1联动复位后，连接态用户可以快速接入UEG2，但空闲态用户需依靠TAU/SR流程向UEG2发送上行信令来恢复业务，系统默认周期TAU时长较长（5G业务50min，4G业务54min）。由于2B用户量少，可以通过调低周期TAU的时长来触发空闲态用户的业务快速恢复（MME/AMF上TAU周期修改为15min）。 |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置系统基本信息。

   ```
   //DC1
   SET CPSYS:DESC="HCGPBER1",ID=0,NM="HCGPBER1",SRV="prsBER1",MCC="123",MNC="03",PROVER=R4,CNID=0,CAP=255; 
   //DC2
   SET CPSYS:DESC="HCGPBER1",ID=0,NM="HCGPBER1",SRV="prsBER1",MCC="123",MNC="03",PROVER=R4,CNID=0,CAP=0;
   ```
3. 配置Home PLMN。

   ```
   //DC1
   ADD HPLMN:MCC="123",MNC="03",CC="86",SM=YES,MAXSMNUM=7,SMS=NO,S5S8TYPE=GTP,PLMNN="noname_1";  
   //DC2
   ADD HPLMN:MCC="123",MNC="03",CC="86",SM=YES,MAXSMNUM=7,SMS=NO,S5S8TYPE=GTP,PLMNN="noname_1";
   ```
4. 配置MMEID。

   ```
   //DC1
   ADD MMEID:MCC="123",MNC="03",MMEGI="8001",MMEC="01";
   //DC2
   ADD MMEID:MCC="123",MNC="03",MMEGI="8001",MMEC="02";
   ```
5. 设置移动性管理EMM（EPS Mobility Management）参数，将周期TAU的时长设置为15min。

   ```
   //DC1
   SET EMM:T3412=15,RCHTMR=20;
   //DC2
   SET EMM:T3412=15,RCHTMR=20;
   ```