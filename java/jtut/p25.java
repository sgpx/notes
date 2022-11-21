import java.util.regex.Matcher;
import java.util.regex.Pattern;

class p25 {
	public static void main(String[] args){

		String line = "hey zey";
		String pattern = "[h|z]ey";
		Pattern p = Pattern.compile(pattern);
		Matcher m = p.matcher(line);

		if(m.find())
		{
			System.out.println("Found value: " + m.group(0) );
		}
	}
}
