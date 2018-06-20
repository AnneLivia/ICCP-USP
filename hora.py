seg = int(input("Por favor, entre com o número de segundos que deseja converter: "));

hora = seg//3600;
min = (seg - (hora * 3600)) // 60;
seg = seg - hora * 3600 - (min * 60);
dia = hora//24;
hora = (hora - 24)//24;
print(dia,"dias,",hora,"horas,",min,"minutos e",seg,"segundos.");