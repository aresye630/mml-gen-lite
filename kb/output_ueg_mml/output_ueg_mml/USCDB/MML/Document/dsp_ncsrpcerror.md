# 显示最近的RPC和错误RPC响应报文信息（DSP NCSRPCERROR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示最近的解析正常但执行错误的RPC和RPC响应报文信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| BOARDTYPE       | OMU类型  | 可选必选说明：可选参数 参数含义：OMU类型。 数据来源：本端规划 取值范围：枚举类型。 master：主OMU。slave：备OMU。 默认值：master                              |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

显示最近的解析正常但执行错误的RPC和RPC响应报文信息：

```
DSP NCSRPCERROR:BOARDTYPE=master,SERVICEINSTANCE="vnfc";
```

```
RETCODE = 0  操作成功

结果如下:
---------
通道ID  会话ID  时间戳                     用户名        终端地址         RPC报文        RPC响应报文

134754  625     2024-02-29 17:51:27+08:00  internaluser  192.168.0.1  <?xml version="1.0" encoding="GBK"?>
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="249638">
  <edit-config>
    <target>
      <running/>
    </target>
    <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <DIAM_PROTO_MGMT xmlns="urn:Huawei:yang:huawei-DIAM_PROTO_MGMT">
        <DOMDMPEERs>
          <DOMDMPEER xc:operation="create">
            <FCOUTSWT>CLOSE</FCOUTSWT>
            <BINDINGFLAG>NO</BINDINGFLAG>
            <SPM>2097152</SPM>
            <DIAMPEERPPNAME>Default</DIAMPEERPPNAME>
            <DN>A</DN>
            <TIMEOUTPLC>DISCARD</TIMEOUTPLC>
            <PEERTIMER>0</PEERTIMER>
            <DIRPROXY>CLOSE</DIRPROXY>
            <DEVTPCHKINSWT>CLOSE</DEVTPCHKINSWT>
            <DEVTPCHKOUTSWT>CLOSE</DEVTPCHKOUTSWT>
            <OAPNAP>NO</OAPNAP>
            <IAPNAP>NO</IAPNAP>
            <DEVTP>1</DEVTP>
            <SLFFLAG>Not_query_the_SLF</SLFFLAG>
            <BWSWT>OFF</BWSWT>
            <INMDENTNM>A</INMDENTNM>
            <HN>A</HN>
            <RN>A</RN>
            <LKSSMOD>ROUND_ROBIN</LKSSMOD>
            <TOPHIDETAG>No</TOPHIDETAG>
            <FCINSWT>CLOSE</FCINSWT>
          </DOMDMPEER>
        </DOMDMPEERs>
      </DIAM_PROTO_MGMT>
    </config>
  </edit-config>
</rpc>
     <?xml version="1.0" encoding="GBK"?>
<rpc-reply message-id="249638" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" flow-id="64">
  <rpc-error>
    <error-type>application</error-type>
    <error-tag>operation-failed</error-tag>
    <error-severity>error</error-severity>
    <error-app-tag>4790</error-app-tag>
    <error-message xml:lang="ch">操作异常。</error-message>
    <error-info xmlns:nc-ext="urn:huawei:yang:huawei-ietf-netconf-ext">
      <nc-ext:error-info-code>4790</nc-ext:error-info-code>
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释              |
|:--------|:-------------------|
| 通道ID    | NETCONF通道标识。       |
| 会话ID    | NETCONF会话标识。       |
| 时间戳     | rpc-reply的发送时间。    |
| 用户名     | 创建NETCONF会话使用的用户名。 |
| 终端地址    | 客户端的IP地址。          |
| RPC报文   | RPC报文。             |
| RPC响应报文 | RPC响应报文。           |