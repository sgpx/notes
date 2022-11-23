#include <stdio.h>
// temp_C / 100 = temp_F - 32 / 180
// c / 5 = (f - 32) / 9
float celsius_to_fahrenheit(float c)
{
	float f = (c * 9.0 / 5.0) + 32;
	return f;
}
float fahrenheit_to_celsius(float f)
{
	float c = ( f - 32.0 )*5.0/ 9.0;
	return c;
}

main()
{
	float c1 = 200;
	float f1 = celsius_to_fahrenheit(c1);
	printf("%f C = %f F\n",c1,f1);


	float f2 = 45;
	float c2 = fahrenheit_to_celsius(f2);
	printf("%f F = %f C\n",f2,c2);
	
}


// output
// 200.000000 C = 392.000000 F
// 45.000000 F = 7.222222 C
