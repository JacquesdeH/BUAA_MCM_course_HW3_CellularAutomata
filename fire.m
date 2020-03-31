% 元胞自动机：森林火灾模型% 规则：
% (1)正在燃烧的树变成空格位；
% (2)如果绿树格位的最近邻居中有一个树在燃烧，则它依概率q变成正在燃烧的树；
% (3)在空格位，树以概率p生长；
% (4)在最近的邻居中没有正在燃烧的树的情况下树在每一时步以概率f(闪
%? 电)变为正在燃烧的树。% 参考文献:% 祝玉学，赵学龙译，<<物理系统的元胞自动机模拟>>, p23
close all;
clc;
clear;
figure;
p=0.3;% 长树的概率p
q=0.5;%燃烧的概率
f=6e-5;% 概率f
axes;
rand('state',0);
set(gcf,'DoubleBuffer','on');
% S=round((rand(300)/2+0.5)*2);
S=round(rand(300)*2);
Sk=zeros(302);
Sk(2:301,2:301)=S;%%加边开始的森林初值
% 红色表示正在燃烧(S中等于2的位置)% 绿色表示绿树(S中等于1的位置)% 黑色表示空格位(S中等于0的位置)
C=zeros(302,302,3);
R=zeros(300);
G=zeros(300);
R(S==2)=1;
G(S==1)=1;
C(2:301,2:301,1)=R;
C(2:301,2:301,2)=G;
Ci=imshow(C);
ti=0;
tp=title(['T = ',num2str(ti)]);%%时间记录
while 1;
    ti=ti+1;
    St=Sk;%%St表示t时刻的森林情况
    St(Sk==2)=0;    % for rule (1) 
    Su=zeros(302);
    Sf=Sk;%%Sf表示模拟着火的过程
    Sf(Sf<1.5)=0;%%只留下着火点
    Sf=Sf/2;%%着火点变为1，此处Sf只有着火和空格两种
    Su(2:301,2:301)=Sf(1:300,1:300)+Sf(1:300,2:301)+Sf(1:300,3:302) +...
        Sf(2:301,1:300)+Sf(2:301,3:302)+Sf(3:302,1:300) + ...
        Sf(3:302,2:301)+Sf(3:302,3:302);%%平移后八个方向叠加，记录下su周围八个点，有多少个在燃烧
    St((Su>0.5)&(St==1)&(rand(302)<q))=2;%原来是错的St(Su>0.5)=2;%% for rule (2)Sf->su
    Se=Sk(2:301,2:301);%%Se中将初始的森林，空白处变为1，其他地方为0
    Se(Se<0.5)=4;%% 空白地方赋值为4
    Se(Se<3)=0;%%有树和着火赋值为0
    Se(Se>3)=1;%%空白地方赋值为1
    St(2:301,2:301)=St(2:301,2:301)+Se.*(rand(300)<p); %for rule (3)%长树，更新t时刻的森林St
    Ss=zeros(302);
    Ss(Sk==1)=1;%%讨论绿树情况
    Ss(2:301,2:301)=Ss(1:300,1:300)+Ss(1:300,2:301)+Ss(1:300,3:302) +...
        Ss(2:301,1:300)+Ss(2:301,3:302)+Ss(3:302,1:300) + ...
        Ss(3:302,2:301)+Ss(3:302,3:302);%%平移后八个方向叠加，记录下Ss周围八个点，有多少个绿树
    Ss(Ss<7.5)=0;
    Ss(Ss>7.5)=1;
    d=find(Ss==1 & Sk==1);
    for k=1:length(d);
        r=rand;
        St(d(k))=round(2*(r<=f)+(r>f));
    end% for rule (4)%%t时刻的着火还是没着火，记为1or2
    Sk=St;%更新t时刻的森林St
    R=zeros(302);
    G=zeros(302);
    R(Sk==2)=1;
    G(Sk==1)=1;
    C(:,:,1)=R;
    C(:,:,2)=G;
    set(Ci,'CData',C);
    set(tp,'string',['T = ',num2str(ti)])
    pause(0.2);
end

