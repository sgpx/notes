import java.util.Date;
import java.text.SimpleDateFormat;

class p20 {
	public static void main(String[] args){

		Date d1 = new Date();
		SimpleDateFormat f = new SimpleDateFormat("E yyyy.MM.dd");
		String s = f.format(d1);
		System.out.println(s);
	}
}
