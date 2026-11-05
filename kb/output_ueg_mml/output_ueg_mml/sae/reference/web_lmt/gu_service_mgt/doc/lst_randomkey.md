# 查询随机密钥功能(LST RANDOMKEY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询随机密钥功能。

- 若需要查询所有的随机密钥数据记录，请不要输入任何参数。
- 若需要查询某个密钥ID对应的随机密钥数据记录，请输入“密钥ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                       |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------|
| KEYID  | 密钥ID   | 可选必选说明：可选参数 参数含义：用于指定系统按照哪个密钥ID查询随机密钥数据记录；若不输入，则表示查询所有的随机密钥数据记录。 取值范围：1～3001，其中3001为系统自动生成。 默认值：无。 配置原则：无。 |

## 使用实例

1. 执行命令不携带“密钥ID”参数，系统已生成随机密钥，且密钥材料完整时返回：

   ```
   LST RANDOMKEY:;
   ```

   ```
   %%LST RANDOMKEY:;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
   KEYID   RANDOMKEY   RKEY        MKEY        WKEY
   1       TRUE        NORMAL      NORMAL      NORMAL
   2       TRUE        NORMAL      NORMAL      NORMAL
   3       TRUE        NORMAL      NORMAL      NORMAL

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 执行命令携带“密钥ID”参数，“密钥ID”为“1”，系统已生成随机密钥，且密钥材料完整时返回：

   ```
   LST RANDOMKEY:KEYID=1;
   ```

   ```
   %%LST RANDOMKEY:KEYID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
                            KEYID = 1
                        RANDOMKEY = TRUE
                             RKEY = NORMAL
                             MKEY = NORMAL
                             WKEY = NORMAL

   Total count = 5

   There is together 1 report

   ---    END
   ```
3. 执行命令不携带“密钥ID”参数，系统未生成随机密钥时返回：

   ```
   LST RANDOMKEY:;
   ```

   ```
   %%LST RANDOMKEY:;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
   KEYID   RANDOMKEY   RKEY        MKEY        WKEY

   Total count = 0

   There is together 1 report

   ---    END
   ```
4. 执行命令携带“密钥ID”参数，“密钥ID”为“1”，系统未生成随机密钥时返回：

   ```
   LST RANDOMKEY:KEYID=1;
   ```

   ```
   %%LST RANDOMKEY:KEYID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
                            KEYID = 1
                        RANDOMKEY = FALSE
    
   Total count = 2
    
   There is together 1 report

   ---    END
   ```
5. 执行命令不携带“密钥ID”参数，系统已生成随机密钥，但密钥材料不完整时返回：

   ```
   LST RANDOMKEY:;
   ```

   ```
   %%LST RANDOMKEY:;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
   KEYID   RANDOMKEY   RKEY        MKEY        WKEY
   1       TRUE        MISSING     NORMAL      NORMAL
   2       TRUE        NORMAL      NORMAL      NORMAL
   3       TRUE        MISSING     NORMAL      NORMAL
    
   Total count = 3
    
   There is together 1 report

   ---    END
   ```
6. 执行命令携带“密钥ID”参数，“密钥ID”为“1”，系统已生成随机密钥，但密钥材料不完整时返回：

   ```
   LST RANDOMKEY:KEYID=1;
   ```

   ```
   %%LST RANDOMKEY:KEYID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
                            KEYID = 1
                        RANDOMKEY = TRUE
                             RKEY = MISSING
                             MKEY = NORMAL
                             WKEY = NORMAL
    
   Total count = 5
    
   There is together 1 report
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**SET RANDOMKEY**

命令的参数说明。表1列出的是未包含在

**SET RANDOMKEY**

命令参数说明中的输出项。

| 参数标识      | 参数说明                                   |
|:----------|:---------------------------------------|
| RANDOMKEY | 表示是否有生成密钥。 TRUE：已生成随机密钥。FALSE：未生成随机密钥。 |
| RKEY      | 表示根密钥是否正常。 NORMAL：正常。MISSING：缺失。       |
| MKEY      | 表示主密钥是否正常。 NORMAL：正常。MISSING：缺失。       |
| WKEY      | 表示工作密钥是否正常。 NORMAL：正常。MISSING：缺失。      |