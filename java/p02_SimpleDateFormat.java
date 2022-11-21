import java.text.SimpleDateFormat;
import java.text.ParseException;
import java.util.Date;

class Xyz
{
	public static void main(String[] args) throws ParseException
	{
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm");
		Date d1 = sdf.parse("1970-01-01 5:30");
		System.out.println(d1.getTime());
	}
}
