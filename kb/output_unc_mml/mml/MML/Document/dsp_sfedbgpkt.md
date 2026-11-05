# 显示调测捕获报文（DSP SFEDBGPKT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来显示调测捕获报文。

#### 注意事项

- 该命令执行后立即生效。
- 报文头长度过长情形可能不会显示所有的报文内容。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                      |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------|
| RUNAME | 资源单元名称 | 可选必选说明：可选参数 参数含义：该参数用来表示资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～60。 默认值：无 配置原则： 区分大小写，不支持空格。使用DSP RU查看RU名称。 |

#### 使用实例

显示资源单元名称为“VNODE\_VNRS\_VNFC\_IPU\_0064”的所有过滤报文信息：

```
DSP SFEDBGPKT: RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```
RETCODE = 0  操作成功.                                                                                                     
                                                                                                                                    
结果如下                                                                                                            
------------------------                                                                                                            
返回结果  =                                                                                                                           
                                                                                                                                    
SFE packet number: 1                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Recv from PAE ExtPort packet: PktLen = 98 SP = 0                                                                                    
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 2                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Send to CP packet: PktLen = 98                                                                                                      
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 3                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Send to LDM packet: PktLen = 98                                                                                                     
FA 16 3E 28 B4 3D FA 16  3E 68 8C 11 08 00 45 00                                                                                    
00 54 01 08 00 00 FF 01  B6 9C 01 01 01 02 01 01                                                                                    
01 01                                                                                                                               
                                                                                                                                    
SFE packet number: 4                                                                                                                
(TIME08:48:25:392)SFE debug packet information:                                                                                     
Current Board : 64
Recv from LDM packet: PktLen = 98                                                                                                   
FA 16 3E 68 8C 11 FA 16  3E 28 B4 3D 08 00 45 00                                                                                    
00 54 02 7C 00 00 FF 01  B5 28 01 01 01 01 01 01                                                                                    
01 02                                                                                                                               
                                                                                                                              
(结果个数 = 1)                                                                                                             
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释            |
|:--------|:-----------------|
| 返回结果    | 调测捕获报文详细信息及报文内容。 |