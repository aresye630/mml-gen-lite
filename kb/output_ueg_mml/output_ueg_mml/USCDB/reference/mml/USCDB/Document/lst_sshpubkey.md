# 查询SSH公钥(LST SSHPUBKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询SSH公钥文件。

- 若需要查询全部SSH公钥文件，请不要输入任何参数。
- 若需要查询某一用户的公钥文件，请输入“用户名”参数。
- 若需要查询某一ID号的公钥文件，请输入“公钥ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                      |
|:-----------|:-------|:------------------------------------------|
| PUBKEYID   | 公钥ID   | 用于指示公钥在系统内的唯一标识。 取值范围：1～128 默认值：无。        |
| USERNAME   | 用户名    | 用于指示待查询用户的用户名。 取值范围：长度不超过31的字符串 默认值：无。    |
| PUBKEYFILE | 公钥文件名  | 用于指示待查询公钥文件的文件名。 取值范围：长度不超过128的字符串 默认值：无。 |

## 使用实例

1. 查询全部SSH公钥文件：

   ```
   LST SSHPUBKEY:;
   ```

   输出报文如下：

   ```
   %%LST SSHPUBKEY:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    公钥ID  用户名         公钥文件名            公钥描述

    1       dsa_user       id_dsa.pub            NULL
    2       ecdsa_user     id_ecdsa.pub          NULL
   (结果个数 = 2)

   ---    END
   ```
2. 查询用户“ecdsa\_user”的公钥文件。“用户名”为“ecdsa\_user”：

   ```
   LST SSHPUBKEY: USERNAME="ecdsa_user";
   ```

   输出报文如下：

   ```
   %%LST SSHPUBKEY: USERNAME="ecdsa_user";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
           公钥ID   =  2
           用户名   =  ecdsa_user
       公钥文件名   =  id_ecdsa.pub
         公钥描述   =  NULL
   (结果个数 = 1)

   ---    END
   ```
3. 查询“公钥ID”为“1”的公钥文件：

   ```
   LST SSHPUBKEY: PUBKEYID=1;
   ```

   输出报文如下：

   ```
   %%LST SSHPUBKEY: PUBKEYID=1;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
           公钥ID   =  1
           用户名   =  dsa_user
       公钥文件名   =  id_dsa.pub
         公钥描述   =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**LOD SSHPUBKEY**命令参数说明。