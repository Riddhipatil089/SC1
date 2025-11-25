#Gaussian
x = 0:0.1:10; 
y = gaussmf(x,[1 4]); 
plot(x,y); 
xlabel('Gaussian MF, p = (x,[1 4])'); 
ylabel('Fuzziness'); 
ylim([-0.05 1.05]);

#trapazodial
x = 0:10; 
y = trapmf(x,[2 4 6 8]); 
plot(x,y); 
xlabel('trapezoidal MF,p = (x,[1 4 6 9])'); 
ylabel('Fuzziness'); 
ylim([-0.05,1,05]);


#triangular
x =0:0.1:10;  
y = trimf(x,[3 6 10]); 
plot(x, y); 
xlabel('triangular MF, p= x,[3,6,10]') 
ylabel('Fuzziness') 
ylim([-0.05 1.05]); 
