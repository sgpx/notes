import java.util.Date;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class p21 {
	public static void main(String[] args) throws ParseException {

		SimpleDateFormat f = new SimpleDateFormat("yyyy.MM.dd");
		Date d1 = f.parse("2020.01.01");
		String s = d1.toString();
		System.out.println(s);
	}
}
