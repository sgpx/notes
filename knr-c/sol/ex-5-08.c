#include <stdio.h>

static char daytab[2][13] = {
	{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
	{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
};

int day_of_year(int year, int month, int day){
	int i, leap;
	leap = (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0);
	// error check
	if(year < 0) return 0;
	else if(month < 0 || month > 12) return 0;
	else if(day < 0 || day > daytab[leap][month])
		return 0;

	for(i = 1; i < month; i++)
		day += daytab[leap][i];

	printf("day %d of year %d\n", day, year);
	return day;
}

void month_day(int year, int yearday, int *pmonth, int *pday){
	int i, leap;
	leap = (year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0);
	// error check
	if(year < 0) return;
	else if(yearday > (leap ? 366 : 365)) return;

	for(i = 1; yearday > daytab[leap][i]; i++)
		yearday -= daytab[leap][i];

	*pmonth = i;
	*pday = yearday;
}

int main(){
	day_of_year(2022,13,5);
	int x = 1, y = 1;
	month_day(2022, 384, &x, &y);

	printf("m : %d, d: %d\n", x, y);
}


