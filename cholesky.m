function [ ret ] = cholesky()
clc
clear
[A,b,n]=matriz;
for k = 1 : n
	acum = 0;
	for p = 1: k-1
		acum = acum + (l(k,p)*u(p,k));
	end
	l(k,k)= sqrt(A(k,k)-acum);
	u(k,k)= l(k,k);
	for i = k + 1: n
		acum = 0;
		for r = 1 : k -1
			acum = acum + (l(i,r)*u(r,k));
		end
		l(i,k)= (A(i,k) - acum)/l(k,k);
	end
	for j = k + 1 : n
		acum = 0;
		for s = 1 : k-1
			acum = acum + (l(k,s)*u(s,j));
		end
		u(k,j)= (A(k,j) - acum)/l(k,k);
	end
end
l = aumentar(l,n,b);
z = sustprogre(l,n);
u = aumentar(u,n,z);
x = sustregre(u,n);
disp (x)
endfunction
