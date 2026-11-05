# 配置网络切片信息

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

在基于切片部署组网内，需要配置切片选择数据，以保证5GC当初始AMF无法判断或者判断自己无法为UE提供切片服务，需要向NSSF进行查询获取切片配置信息，详细请参考配置切片选择数据。

可以配置候选AMF信息，如果当前AMF故障或其他不能提供服务的异常场景下，NSSF将切片信息返回至规划的候选AMF，保证业务正常，详细请参考配置候选AMF信息。

## 必备事项

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经获取网设LLD文档。

数据

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CFGSNSSAI** | 索引（INDEX） | 1 | 本端规划 | 配置运营商支持的切片配置信息。 |
|  | 移动国家码（MCC） | 123 | 全网规划 |  |
|  | 移动网号（MNC） | 03 |  |  |
|  | 切片服务类型（SST） | 1 |  |  |
|  | 切片细分标识（SD） | 010101 |  |  |
|  | 激活状态（ISACTIVE） | TRUE |  |  |
| **ADD TACGROUPINNSSF** | 索引（INDEX） | 1 | 本端规划 | 配置跟踪区域分组。 |
|  | 跟踪区域码分组名称（TACGROUPNAME） | TACGROUP01 | 全网规划 |  |
|  | TAC起始字符（TACSTART） | 290100 | 本端规划 |  |
|  | TAC结束字符（TACEND） | 290110 |  |  |
| **ADD AMFSETID** | 索引（INDEX） | 1 | 本端规划 | 配置AMF集合支持的切片信息。 |
|  | 切片服务类型（SST） | 1 | 全网规划 |  |
|  | 切片细分标识（SD） | 010101 |  |  |
|  | 移动国家码（MCC） | 123 |  |  |
|  | 移动网号（MNC） | 03 |  |  |
|  | 区域ID（REGIONID） | 01 |  |  |
|  | AMF集合标识（AMFSETID） | 001 |  |  |
|  | 跟踪区域码分组名称（TACGROUPNAME） | TACGROUP01 |  |  |
| **ADD CANDIDATEAMF** | 索引（INDEX） | 1 | 本端规划 | 配置候选AMF信息。 |
|  | AMF实例标识（AMFINSTANCEID） | bdc3f6f6-69ac-4c06-bfe5-030101000001 | 全网规划 |  |
|  | 移动国家码（MCC） | 123 |  |  |
|  | 移动网号（MNC） | 03 |  |  |
|  | 区域ID（REGIONID） | 01 |  |  |
|  | AMF集合标识（AMFSETID） | 001 |  |  |

## 操作步骤

**配置切片选择数据**

1. 进入“MML命令行-UNC”窗口。
2. 配置运营商支持的切片信息。

   ```
   ADD CFGSNSSAI: INDEX=1, MCC="123", MNC="03", SST=1, SD="010101", ISACTIVE=TRUE;
   ```
3. 配置AMF集合支持的切片信息。

   ```
   ADD TACGROUPINNSSF: INDEX=1, TACGROUPNAME="TACGROUP01", TACSTART="290100", TACEND="290110";
   ADD AMFSETID: INDEX=1, SST=1, SD="010101", MCC="123", MNC="03", REGIONID="01", AMFSETID="001", TACGROUPNAME="TACGROUP01";
   ```

**配置候选AMF信息**

4. **可选：**配置候选AMF信息。

   ```
   ADD CANDIDATEAMF: INDEX=1, AMFINSTANCEID="bdc3f6f6-69ac-4c06-bfe5-030101000001", MCC="123", MNC="03", REGIONID="01", AMFSETID="001";
   ```

版权所有 © 华为技术有限公司
