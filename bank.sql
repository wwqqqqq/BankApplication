/*==============================================================*/
/* DBMS name:      ORACLE Version 12c                           */
/* Created on:     2018/5/16 19:15:15                           */
/*==============================================================*/


alter table ���
   drop constraint FK_���_���_����;

alter table ���
   drop constraint FK_���_���2_�ͻ�;

alter table �����˻�
   drop constraint FK_�����˻�_INHERITAN_�˻�;

alter table Ա��
   drop constraint FK_Ա��_��ְ_����;

alter table Ա��
   drop constraint FK_Ա��_����_Ա��;

alter table �ͻ�
   drop constraint FK_�ͻ�_�����_Ա��;

alter table �ͻ�
   drop constraint FK_�ͻ�_�����˻�����_Ա��;

alter table ����_����
   drop constraint FK_����_����_����_����_�ͻ�;

alter table ����_����
   drop constraint FK_����_����_����_����2_����;

alter table ����_����
   drop constraint FK_����_����_����_����3_֧��;

alter table ����_֧Ʊ
   drop constraint FK_����_֧Ʊ_����_֧Ʊ_�ͻ�;

alter table ����_֧Ʊ
   drop constraint FK_����_֧Ʊ_����_֧Ʊ2_֧��;

alter table ����_֧Ʊ
   drop constraint FK_����_֧Ʊ_����_֧Ʊ3_֧Ʊ;

alter table ֧Ʊ�˻�
   drop constraint FK_֧Ʊ�˻�_INHERITAN_�˻�;

alter table �˻�
   drop constraint FK_�˻�_����_֧��;

alter table ����
   drop constraint FK_����_���Ŵ���_֧��;

alter table ����֧��
   drop constraint FK_����֧��_֧������_����;

drop index ���2_FK;

drop index ���_FK;

drop table ��� cascade constraints;

drop table �����˻� cascade constraints;

drop index ����_FK;

drop index ��ְ_FK;

drop table Ա�� cascade constraints;

drop index �����˻�����_FK;

drop index �����_FK;

drop table �ͻ� cascade constraints;

drop index ����3_FK;

drop index ����2_FK;

drop index ����_FK;

drop table ����_���� cascade constraints;

drop index ����_֧Ʊ3_FK;

drop index ����_֧Ʊ2_FK;

drop index ����_֧Ʊ_FK;

drop table ����_֧Ʊ cascade constraints;

drop table ֧Ʊ�˻� cascade constraints;

drop table ֧�� cascade constraints;

drop index ����_FK2;

drop table �˻� cascade constraints;

drop index ���Ŵ���_FK;

drop table ���� cascade constraints;

drop index ֧������_FK;

drop table ����֧�� cascade constraints;

drop table ���� cascade constraints;

/*==============================================================*/
/* Table: ���                                                    */
/*==============================================================*/
create table ��� (
   �����                  CHAR(256)             not null,
   ���֤��_�ͻ�              CHAR(256)             not null,
   constraint PK_��� primary key (�����, ���֤��_�ͻ�)
);

/*==============================================================*/
/* Index: ���_FK                                                 */
/*==============================================================*/
create index ���_FK on ��� (
   ����� ASC
);

/*==============================================================*/
/* Index: ���2_FK                                                */
/*==============================================================*/
create index ���2_FK on ��� (
   ���֤��_�ͻ� ASC
);

/*==============================================================*/
/* Table: �����˻�                                                  */
/*==============================================================*/
create table �����˻� (
   �˻���                  CHAR(256)             not null,
   ֧����                  CHAR(256),
   ���                   FLOAT                 not null,
   ��������                 DATE                  not null,
   ����                   FLOAT                 not null,
   ��������                 CHAR(256)             not null,
   constraint PK_�����˻� primary key (�˻���)
);

/*==============================================================*/
/* Table: Ա��                                                    */
/*==============================================================*/
create table Ա�� (
   ���֤��_Ա��              CHAR(256)             not null,
   ���ź�                  CHAR(256)             not null,
   Ա��_���֤��_Ա��           CHAR(256),
   ��ʼ����������              DATE                  not null,
   ����_Ա��                CHAR(256)             not null,
   �绰����_Ա��              CHAR(256)             not null,
   ��ͥ��ַ_Ա��              CHAR(256)             not null,
   constraint PK_Ա�� primary key (���֤��_Ա��)
);

/*==============================================================*/
/* Index: ��ְ_FK                                                 */
/*==============================================================*/
create index ��ְ_FK on Ա�� (
   ���ź� ASC
);

/*==============================================================*/
/* Index: ����_FK                                                 */
/*==============================================================*/
create index ����_FK on Ա�� (
   Ա��_���֤��_Ա�� ASC
);

/*==============================================================*/
/* Table: �ͻ�                                                    */
/*==============================================================*/
create table �ͻ� (
   ���֤��_�ͻ�              CHAR(256)             not null,
   ���֤��_Ա��              CHAR(256),
   Ա��_���֤��_Ա��           CHAR(256),
   ����_�ͻ�                CHAR(256)             not null,
   ��ϵ�绰                 CHAR(256)             not null,
   ��ͥסַ                 CHAR(256)             not null,
   ��ϵ������                CHAR(256)             not null,
   ��ϵ���ֻ���               CHAR(256)             not null,
   "��ϵ��email"           CHAR(256)             not null,
   ��ϵ����ͻ��Ĺ�ϵ            CHAR(256)             not null,
   constraint PK_�ͻ� primary key (���֤��_�ͻ�)
);

/*==============================================================*/
/* Index: �����_FK                                               */
/*==============================================================*/
create index �����_FK on �ͻ� (
   Ա��_���֤��_Ա�� ASC
);

/*==============================================================*/
/* Index: �����˻�����_FK                                             */
/*==============================================================*/
create index �����˻�����_FK on �ͻ� (
   ���֤��_Ա�� ASC
);

/*==============================================================*/
/* Table: ����_����                                                 */
/*==============================================================*/
create table ����_���� (
   ���֤��_�ͻ�              CHAR(256)             not null,
   �˻���                  CHAR(256)             not null,
   ֧����                  CHAR(256)             not null,
   ��������������˻�����_����       DATE                  not null,
   constraint PK_����_���� primary key (���֤��_�ͻ�, ֧����)
);

/*==============================================================*/
/* Index: ����_FK                                                 */
/*==============================================================*/
create index ����_FK on ����_���� (
   ���֤��_�ͻ� ASC
);

/*==============================================================*/
/* Index: ����2_FK                                                */
/*==============================================================*/
create index ����2_FK on ����_���� (
   �˻��� ASC
);

/*==============================================================*/
/* Index: ����3_FK                                                */
/*==============================================================*/
create index ����3_FK on ����_���� (
   ֧���� ASC
);

/*==============================================================*/
/* Table: ����_֧Ʊ                                                 */
/*==============================================================*/
create table ����_֧Ʊ (
   ���֤��_�ͻ�              CHAR(256)             not null,
   ֧����                  CHAR(256)             not null,
   �˻���                  CHAR(256)             not null,
   ��������������˻�����_֧Ʊ       DATE                  not null,
   constraint PK_����_֧Ʊ primary key (���֤��_�ͻ�, ֧����)
);

/*==============================================================*/
/* Index: ����_֧Ʊ_FK                                              */
/*==============================================================*/
create index ����_֧Ʊ_FK on ����_֧Ʊ (
   ���֤��_�ͻ� ASC
);

/*==============================================================*/
/* Index: ����_֧Ʊ2_FK                                             */
/*==============================================================*/
create index ����_֧Ʊ2_FK on ����_֧Ʊ (
   ֧���� ASC
);

/*==============================================================*/
/* Index: ����_֧Ʊ3_FK                                             */
/*==============================================================*/
create index ����_֧Ʊ3_FK on ����_֧Ʊ (
   �˻��� ASC
);

/*==============================================================*/
/* Table: ֧Ʊ�˻�                                                  */
/*==============================================================*/
create table ֧Ʊ�˻� (
   �˻���                  CHAR(256)             not null,
   ֧����                  CHAR(256),
   ���                   FLOAT                 not null,
   ��������                 DATE                  not null,
   ͸֧��                  FLOAT                 not null,
   constraint PK_֧Ʊ�˻� primary key (�˻���)
);

/*==============================================================*/
/* Table: ֧��                                                    */
/*==============================================================*/
create table ֧�� (
   ֧����                  CHAR(256)             not null,
   ����                   CHAR(256)             not null,
   �ʲ�                   CHAR(256)             not null,
   constraint PK_֧�� primary key (֧����)
);

/*==============================================================*/
/* Table: �˻�                                                    */
/*==============================================================*/
create table �˻� (
   �˻���                  CHAR(256)             not null,
   ֧����                  CHAR(256)             not null,
   ���                   FLOAT                 not null,
   ��������                 DATE                  not null,
   constraint PK_�˻� primary key (�˻���)
);

/*==============================================================*/
/* Index: ����_FK2                                                */
/*==============================================================*/
create index ����_FK2 on �˻� (
   ֧���� ASC
);

/*==============================================================*/
/* Table: ����                                                    */
/*==============================================================*/
create table ���� (
   �����                  CHAR(256)             not null,
   ֧����                  CHAR(256)             not null,
   �������                 FLOAT                 not null,
   constraint PK_���� primary key (�����)
);

/*==============================================================*/
/* Index: ���Ŵ���_FK                                               */
/*==============================================================*/
create index ���Ŵ���_FK on ���� (
   ֧���� ASC
);

/*==============================================================*/
/* Table: ����֧��                                                  */
/*==============================================================*/
create table ����֧�� (
   �����                  CHAR(256)             not null,
   ����                   DATE                  not null,
   ���                   FLOAT                 not null,
   constraint PK_����֧�� primary key (�����, ����)
);

/*==============================================================*/
/* Index: ֧������_FK                                               */
/*==============================================================*/
create index ֧������_FK on ����֧�� (
   ����� ASC
);

/*==============================================================*/
/* Table: ����                                                    */
/*==============================================================*/
create table ���� (
   ������                  CHAR(256)             not null,
   ���ź�                  CHAR(256)             not null,
   ��������                 CHAR(256)             not null,
   constraint PK_���� primary key (���ź�)
);

alter table ���
   add constraint FK_���_���_���� foreign key (�����)
      references ���� (�����);

alter table ���
   add constraint FK_���_���2_�ͻ� foreign key (���֤��_�ͻ�)
      references �ͻ� (���֤��_�ͻ�);

alter table �����˻�
   add constraint FK_�����˻�_INHERITAN_�˻� foreign key (�˻���)
      references �˻� (�˻���);

/*alter table Ա��
   add constraint FK_Ա��_��ְ_���� foreign key (���ź�)
      references ���� (���ź�);*/

alter table Ա��
   add constraint FK_Ա��_����_Ա�� foreign key (Ա��_���֤��_Ա��)
      references Ա�� (���֤��_Ա��);

alter table �ͻ�
   add constraint FK_�ͻ�_�����_Ա�� foreign key (Ա��_���֤��_Ա��)
      references Ա�� (���֤��_Ա��);

alter table �ͻ�
   add constraint FK_�ͻ�_�����˻�����_Ա�� foreign key (���֤��_Ա��)
      references Ա�� (���֤��_Ա��);

alter table ����_����
   add constraint FK_����_����_����_����_�ͻ� foreign key (���֤��_�ͻ�)
      references �ͻ� (���֤��_�ͻ�);

alter table ����_����
   add constraint FK_����_����_����_����2_���� foreign key (�˻���)
      references �����˻� (�˻���);

alter table ����_����
   add constraint FK_����_����_����_����3_֧�� foreign key (֧����)
      references ֧�� (֧����);

alter table ����_֧Ʊ
   add constraint FK_����_֧Ʊ_����_֧Ʊ_�ͻ� foreign key (���֤��_�ͻ�)
      references �ͻ� (���֤��_�ͻ�);

alter table ����_֧Ʊ
   add constraint FK_����_֧Ʊ_����_֧Ʊ2_֧�� foreign key (֧����)
      references ֧�� (֧����);

alter table ����_֧Ʊ
   add constraint FK_����_֧Ʊ_����_֧Ʊ3_֧Ʊ foreign key (�˻���)
      references ֧Ʊ�˻� (�˻���);

alter table ֧Ʊ�˻�
   add constraint FK_֧Ʊ�˻�_INHERITAN_�˻� foreign key (�˻���)
      references �˻� (�˻���);

alter table �˻�
   add constraint FK_�˻�_����_֧�� foreign key (֧����)
      references ֧�� (֧����);

alter table ����
   add constraint FK_����_���Ŵ���_֧�� foreign key (֧����)
      references ֧�� (֧����);

alter table ����֧��
   add constraint FK_����֧��_֧������_���� foreign key (�����)
      references ���� (�����);

