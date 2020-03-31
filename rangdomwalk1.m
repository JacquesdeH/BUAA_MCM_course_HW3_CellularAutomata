%一间封闭的空房间, 一个人在里面随意移动
%状态变化规则：
%1.四周没有墙壁时，以等概率方式移动到周围8个位置之一；
%2.位于墙角时，以等概率方式移动到周围3个位置之一；
%3.位于墙边非墙角时，以等概率方式移动到周围5个位置之一
close all;
clc;
clear;
M=22;%房间大小M行,包括两行墙
N=18;%房间大小N列,包括两列墙
%房间状态初始化
R=ones(M,N);
R(1,:)=0;
R(M,:)=0;
R(:,1)=0;
R(:,N)=0;
G=R;
B=R;
i=unidrnd(M-2)+1;%随机选取初始位置行标
j=unidrnd(N-2)+1;%随机选取初始位置列标
G(i,j)=0;
B(i,j)=0;
ima=cat(3,R,G,B);
imshow(ima,'InitialMagnification','fit');%初始状态图显示

neighbour=[-1 -1;-1 0;-1 1;0 -1;0 1;1 -1;1 0;1 1];%当前位置邻域
%i,j始终表示人所在位置的坐标
for t=1:50
     G(i,j)=1;   %更改当前人所在位置为白色
     B(i,j)=1;   %更改当前人所在位置为白色
     if 2<i && i<M-1 && 2<j && j<N-1  %人在内部
         r=unidrnd(8);        
     elseif i==2 && j==2   %人在左上墙角
         r=randsrc(1,1,[5 7 8]);
     elseif i==2 && j==N-1   %人在右上墙角
         r=randsrc(1,1,[4 6 7]);
     elseif i==M-1 && j==2   %人在左下墙角
         r=randsrc(1,1,[2 3 5]);
     elseif i==M-1 && j==N-1   %人在右下墙角
         r=randsrc(1,1,[1 2 4]);
     elseif i==2 && 2<j && j<N-1  %人在上墙边非墙角
         r=randsrc(1,1,[4 5 6 7 8]);
     elseif i==M-1 && 2<j && j<N-1  %人在下墙边非墙角
         r=randsrc(1,1,[1 2 3 4 5]);
     elseif 2<i && i<M-1 && j==2  %人在左墙边非墙角
         r=randsrc(1,1,[2 3 5 7 8]);
     else 2<i && i<M-1 && j==N-1  %人在右墙边非墙角
         r=randsrc(1,1,[1 2 4 6 7]);
     end
     i=i+neighbour(r,1); %更新位置坐标
     j=j+neighbour(r,2); %更新位置坐标
     G(i,j)=0;  %更新当前人所在位置为红色
     B(i,j)=0;  %更新当前人所在位置为红色
     ima=cat(3,R,G,B);
     imshow(ima,'InitialMagnification','fit');
     pause(0.2);
end





