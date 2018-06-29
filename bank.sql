/*==============================================================*/
/* DBMS name:      ORACLE Version 12c                           */
/* Created on:     2018/5/16 19:15:15                           */
/*==============================================================*/


alter table 借贷
   drop constraint FK_借贷_借贷_贷款;

alter table 借贷
   drop constraint FK_借贷_借贷2_客户;

alter table 储蓄账户
   drop constraint FK_储蓄账户_INHERITAN_账户;

alter table 员工
   drop constraint FK_员工_供职_部门;

alter table 员工
   drop constraint FK_员工_管理_员工;

alter table 客户
   drop constraint FK_客户_贷款负责_员工;

alter table 客户
   drop constraint FK_客户_银行账户负责_员工;

alter table 开户_储蓄
   drop constraint FK_开户_储蓄_开户_储蓄_客户;

alter table 开户_储蓄
   drop constraint FK_开户_储蓄_开户_储蓄2_储蓄;

alter table 开户_储蓄
   drop constraint FK_开户_储蓄_开户_储蓄3_支行;

alter table 开户_支票
   drop constraint FK_开户_支票_开户_支票_客户;

alter table 开户_支票
   drop constraint FK_开户_支票_开户_支票2_支行;

alter table 开户_支票
   drop constraint FK_开户_支票_开户_支票3_支票;

alter table 支票账户
   drop constraint FK_支票账户_INHERITAN_账户;

alter table 账户
   drop constraint FK_账户_开户_支行;

alter table 贷款
   drop constraint FK_贷款_发放贷款_支行;

alter table 贷款支付
   drop constraint FK_贷款支付_支付贷款_贷款;

drop index 借贷2_FK;

drop index 借贷_FK;

drop table 借贷 cascade constraints;

drop table 储蓄账户 cascade constraints;

drop index 管理_FK;

drop index 供职_FK;

drop table 员工 cascade constraints;

drop index 银行账户负责_FK;

drop index 贷款负责_FK;

drop table 客户 cascade constraints;

drop index 开户3_FK;

drop index 开户2_FK;

drop index 开户_FK;

drop table 开户_储蓄 cascade constraints;

drop index 开户_支票3_FK;

drop index 开户_支票2_FK;

drop index 开户_支票_FK;

drop table 开户_支票 cascade constraints;

drop table 支票账户 cascade constraints;

drop table 支行 cascade constraints;

drop index 开户_FK2;

drop table 账户 cascade constraints;

drop index 发放贷款_FK;

drop table 贷款 cascade constraints;

drop index 支付贷款_FK;

drop table 贷款支付 cascade constraints;

drop table 部门 cascade constraints;

/*==============================================================*/
/* Table: 借贷                                                    */
/*==============================================================*/
create table 借贷 (
   贷款号                  CHAR(256)             not null,
   身份证号_客户              CHAR(256)             not null,
   constraint PK_借贷 primary key (贷款号, 身份证号_客户)
);

/*==============================================================*/
/* Index: 借贷_FK                                                 */
/*==============================================================*/
create index 借贷_FK on 借贷 (
   贷款号 ASC
);

/*==============================================================*/
/* Index: 借贷2_FK                                                */
/*==============================================================*/
create index 借贷2_FK on 借贷 (
   身份证号_客户 ASC
);

/*==============================================================*/
/* Table: 储蓄账户                                                  */
/*==============================================================*/
create table 储蓄账户 (
   账户号                  CHAR(256)             not null,
   支行名                  CHAR(256),
   余额                   FLOAT                 not null,
   开户日期                 DATE                  not null,
   利率                   FLOAT                 not null,
   货币类型                 CHAR(256)             not null,
   constraint PK_储蓄账户 primary key (账户号)
);

/*==============================================================*/
/* Table: 员工                                                    */
/*==============================================================*/
create table 员工 (
   身份证号_员工              CHAR(256)             not null,
   部门号                  CHAR(256)             not null,
   员工_身份证号_员工           CHAR(256),
   开始工作的日期              DATE                  not null,
   姓名_员工                CHAR(256)             not null,
   电话号码_员工              CHAR(256)             not null,
   家庭地址_员工              CHAR(256)             not null,
   constraint PK_员工 primary key (身份证号_员工)
);

/*==============================================================*/
/* Index: 供职_FK                                                 */
/*==============================================================*/
create index 供职_FK on 员工 (
   部门号 ASC
);

/*==============================================================*/
/* Index: 管理_FK                                                 */
/*==============================================================*/
create index 管理_FK on 员工 (
   员工_身份证号_员工 ASC
);

/*==============================================================*/
/* Table: 客户                                                    */
/*==============================================================*/
create table 客户 (
   身份证号_客户              CHAR(256)             not null,
   身份证号_员工              CHAR(256),
   员工_身份证号_员工           CHAR(256),
   姓名_客户                CHAR(256)             not null,
   联系电话                 CHAR(256)             not null,
   家庭住址                 CHAR(256)             not null,
   联系人姓名                CHAR(256)             not null,
   联系人手机号               CHAR(256)             not null,
   "联系人email"           CHAR(256)             not null,
   联系人与客户的关系            CHAR(256)             not null,
   constraint PK_客户 primary key (身份证号_客户)
);

/*==============================================================*/
/* Index: 贷款负责_FK                                               */
/*==============================================================*/
create index 贷款负责_FK on 客户 (
   员工_身份证号_员工 ASC
);

/*==============================================================*/
/* Index: 银行账户负责_FK                                             */
/*==============================================================*/
create index 银行账户负责_FK on 客户 (
   身份证号_员工 ASC
);

/*==============================================================*/
/* Table: 开户_储蓄                                                 */
/*==============================================================*/
create table 开户_储蓄 (
   身份证号_客户              CHAR(256)             not null,
   账户号                  CHAR(256)             not null,
   支行名                  CHAR(256)             not null,
   所有者最近访问账户日期_储蓄       DATE                  not null,
   constraint PK_开户_储蓄 primary key (身份证号_客户, 支行名)
);

/*==============================================================*/
/* Index: 开户_FK                                                 */
/*==============================================================*/
create index 开户_FK on 开户_储蓄 (
   身份证号_客户 ASC
);

/*==============================================================*/
/* Index: 开户2_FK                                                */
/*==============================================================*/
create index 开户2_FK on 开户_储蓄 (
   账户号 ASC
);

/*==============================================================*/
/* Index: 开户3_FK                                                */
/*==============================================================*/
create index 开户3_FK on 开户_储蓄 (
   支行名 ASC
);

/*==============================================================*/
/* Table: 开户_支票                                                 */
/*==============================================================*/
create table 开户_支票 (
   身份证号_客户              CHAR(256)             not null,
   支行名                  CHAR(256)             not null,
   账户号                  CHAR(256)             not null,
   所有者最近访问账户日期_支票       DATE                  not null,
   constraint PK_开户_支票 primary key (身份证号_客户, 支行名)
);

/*==============================================================*/
/* Index: 开户_支票_FK                                              */
/*==============================================================*/
create index 开户_支票_FK on 开户_支票 (
   身份证号_客户 ASC
);

/*==============================================================*/
/* Index: 开户_支票2_FK                                             */
/*==============================================================*/
create index 开户_支票2_FK on 开户_支票 (
   支行名 ASC
);

/*==============================================================*/
/* Index: 开户_支票3_FK                                             */
/*==============================================================*/
create index 开户_支票3_FK on 开户_支票 (
   账户号 ASC
);

/*==============================================================*/
/* Table: 支票账户                                                  */
/*==============================================================*/
create table 支票账户 (
   账户号                  CHAR(256)             not null,
   支行名                  CHAR(256),
   余额                   FLOAT                 not null,
   开户日期                 DATE                  not null,
   透支额                  FLOAT                 not null,
   constraint PK_支票账户 primary key (账户号)
);

/*==============================================================*/
/* Table: 支行                                                    */
/*==============================================================*/
create table 支行 (
   支行名                  CHAR(256)             not null,
   城市                   CHAR(256)             not null,
   资产                   CHAR(256)             not null,
   constraint PK_支行 primary key (支行名)
);

/*==============================================================*/
/* Table: 账户                                                    */
/*==============================================================*/
create table 账户 (
   账户号                  CHAR(256)             not null,
   支行名                  CHAR(256)             not null,
   余额                   FLOAT                 not null,
   开户日期                 DATE                  not null,
   constraint PK_账户 primary key (账户号)
);

/*==============================================================*/
/* Index: 开户_FK2                                                */
/*==============================================================*/
create index 开户_FK2 on 账户 (
   支行名 ASC
);

/*==============================================================*/
/* Table: 贷款                                                    */
/*==============================================================*/
create table 贷款 (
   贷款号                  CHAR(256)             not null,
   支行名                  CHAR(256)             not null,
   所贷金额                 FLOAT                 not null,
   constraint PK_贷款 primary key (贷款号)
);

/*==============================================================*/
/* Index: 发放贷款_FK                                               */
/*==============================================================*/
create index 发放贷款_FK on 贷款 (
   支行名 ASC
);

/*==============================================================*/
/* Table: 贷款支付                                                  */
/*==============================================================*/
create table 贷款支付 (
   贷款号                  CHAR(256)             not null,
   日期                   DATE                  not null,
   金额                   FLOAT                 not null,
   constraint PK_贷款支付 primary key (贷款号, 日期)
);

/*==============================================================*/
/* Index: 支付贷款_FK                                               */
/*==============================================================*/
create index 支付贷款_FK on 贷款支付 (
   贷款号 ASC
);

/*==============================================================*/
/* Table: 部门                                                    */
/*==============================================================*/
create table 部门 (
   部门名                  CHAR(256)             not null,
   部门号                  CHAR(256)             not null,
   部门类型                 CHAR(256)             not null,
   constraint PK_部门 primary key (部门号)
);

alter table 借贷
   add constraint FK_借贷_借贷_贷款 foreign key (贷款号)
      references 贷款 (贷款号);

alter table 借贷
   add constraint FK_借贷_借贷2_客户 foreign key (身份证号_客户)
      references 客户 (身份证号_客户);

alter table 储蓄账户
   add constraint FK_储蓄账户_INHERITAN_账户 foreign key (账户号)
      references 账户 (账户号);

/*alter table 员工
   add constraint FK_员工_供职_部门 foreign key (部门号)
      references 部门 (部门号);*/

alter table 员工
   add constraint FK_员工_管理_员工 foreign key (员工_身份证号_员工)
      references 员工 (身份证号_员工);

alter table 客户
   add constraint FK_客户_贷款负责_员工 foreign key (员工_身份证号_员工)
      references 员工 (身份证号_员工);

alter table 客户
   add constraint FK_客户_银行账户负责_员工 foreign key (身份证号_员工)
      references 员工 (身份证号_员工);

alter table 开户_储蓄
   add constraint FK_开户_储蓄_开户_储蓄_客户 foreign key (身份证号_客户)
      references 客户 (身份证号_客户);

alter table 开户_储蓄
   add constraint FK_开户_储蓄_开户_储蓄2_储蓄 foreign key (账户号)
      references 储蓄账户 (账户号);

alter table 开户_储蓄
   add constraint FK_开户_储蓄_开户_储蓄3_支行 foreign key (支行名)
      references 支行 (支行名);

alter table 开户_支票
   add constraint FK_开户_支票_开户_支票_客户 foreign key (身份证号_客户)
      references 客户 (身份证号_客户);

alter table 开户_支票
   add constraint FK_开户_支票_开户_支票2_支行 foreign key (支行名)
      references 支行 (支行名);

alter table 开户_支票
   add constraint FK_开户_支票_开户_支票3_支票 foreign key (账户号)
      references 支票账户 (账户号);

alter table 支票账户
   add constraint FK_支票账户_INHERITAN_账户 foreign key (账户号)
      references 账户 (账户号);

alter table 账户
   add constraint FK_账户_开户_支行 foreign key (支行名)
      references 支行 (支行名);

alter table 贷款
   add constraint FK_贷款_发放贷款_支行 foreign key (支行名)
      references 支行 (支行名);

alter table 贷款支付
   add constraint FK_贷款支付_支付贷款_贷款 foreign key (贷款号)
      references 贷款 (贷款号);

